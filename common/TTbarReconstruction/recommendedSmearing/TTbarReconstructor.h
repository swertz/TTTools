#pragma once

#include <cp3_llbb/TTAnalysis/interface/Types.h>
#include <cp3_llbb/TTAnalysis/interface/NeutrinosSolver.h>

#include <iostream>
#include <algorithm>
#include <utility>

#include <Math/Vector4D.h>
#include <Math/LorentzVector.h>

//#define RECO_DEBUG

#define PRINT_VECTOR(vec) std::cout << "Vector " << #vec << ": " << vec << std::endl;

#define PRINT_VECTORS(vec) \
  PRINT_VECTOR(vec) \
  PRINT_VECTOR(gen_##vec)

#define myLorentzVector ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiE4D<float>>

// Needed because it is defined in TTAnalyzer.cc, which is not compiled here
float TTAnalysis::DeltaEta(const myLorentzVector& v1, const myLorentzVector& v2) {
    return std::abs(v1.Eta() - v2.Eta());
}

class TTbarSolution {
  public:

    TTbarSolution():
      t_px(0), t_py(0), t_pz(0),
      tbar_px(0), tbar_py(0), tbar_pz(0),
      nSols(0), weight(0), chosenDiLepDiJetMETidx(-1)
      {}
    
    TTbarSolution(
        double t_px, double t_py, double t_pz,
        double tbar_px, double tbar_py, double tbar_pz):
      t_px(t_px), t_py(t_py), t_pz(t_pz),
      tbar_px(tbar_px), tbar_py(tbar_py), tbar_pz(tbar_pz),
      nSols(0), weight(0), chosenDiLepDiJetMETidx(-1)
      {}
    
    TTbarSolution(const TTAnalysis::TTBar& tt):
      t_px(tt.top1_p4.Px()), t_py(tt.top1_p4.Py()), t_pz(tt.top1_p4.Pz()),
      tbar_px(tt.top2_p4.Px()), tbar_py(tt.top2_p4.Py()), tbar_pz(tt.top2_p4.Pz()),
      nSols(0), weight(0), chosenDiLepDiJetMETidx(-1)
      {}

    ~TTbarSolution() {}

    TTbarSolution& operator+=(const TTbarSolution& sol){
      t_px += sol.t_px; t_py += sol.t_py; t_pz += sol.t_pz;
      tbar_px += sol.tbar_px; tbar_py += sol.tbar_py; tbar_pz += sol.tbar_pz;
      nSols += sol.nSols;
      return *this;
    }

    friend TTbarSolution operator*(const double w, const TTbarSolution& sol){
      TTbarSolution tempSol(
          w*sol.t_px, w*sol.t_py, w*sol.t_pz,
          w*sol.tbar_px, w*sol.tbar_py, w*sol.tbar_pz);
      return tempSol;
    }

    TTbarSolution& operator*=(const double w){
      t_px *= w; t_py *= w; t_pz *= w;
      tbar_px *= w; tbar_py *= w; tbar_pz *= w;
      return *this;
    }

    void BuildTopLorentzVectors(const double t_mass=172.5){
      const double t_E = sqrt( pow(t_mass, 2) + pow(t_px, 2) + pow(t_py, 2) + pow(t_pz, 2) );
      p4_t.SetPxPyPzE(t_px, t_py, t_pz, t_E);
    
      const double tbar_E = sqrt( pow(tbar_mass, 2) + pow(tbar_px, 2) + pow(tbar_py, 2) + pow(tbar_pz, 2) );
      p4_tbar.SetPxPyPzE(tbar_px, tbar_py, tbar_pz, tbar_E);
    }
    
    double t_px, t_py, t_pz;
    double tbar_px, tbar_py, tbar_pz;
    uint32_t nSols;
    double weight;

    LorentzVector p4_t, p4_tbar;
    int16_t chosenDiLepDiJetMETidx;
};


class TTbarReconstructor {
  public:
    
    TTbarReconstructor(
        SmearingFunction& electronEnergySmearing, 
        SmearingFunction& electronAngleSmearing, 
        SmearingFunction& muonEnergySmearing, 
        SmearingFunction& muonAngleSmearing, 
        SmearingFunction& bJetEnergySmearing, 
        SmearingFunction& bJetAngleSmearing, 
        SmearingFunction& WSmearing, 
        SmearingFunction& TopSmearing, 
        SmearingFunction& MlbWeighting, 
        uint32_t nTries
        ):
      muonSmearing(muonSmearing),
      electronSmearing(electronSmearing),
      bJetSmearing(bJetSmearing),
      WSmearing(WSmearing),
      TopSmearing(TopSmearing),
      nTries(nTries)
      {}

    TTbarSolution getSolution(
        std::vector<TTAnalysis::Lepton>& _leptons,
        std::vector<TTAnalysis::DiLepton>& _diLeptons,
        std::vector<TTAnalysis::Jet>& _jets,
        std::vector<TTAnalysis::DiJet>& _diJets,
        std::vector<TTAnalysis::DiLepDiJetMet>& _diLepDiJetsMet,
        std::vector<uint16_t>& selObj_CSVv2Ordered){

#ifdef RECO_DEBUG
        std::cout << "\nStarting event\n";
#endif
      
        double totWeight(0);
        TTbarSolution solution;

        for(uint32_t i = 0; i < nTries; ++i){

          double thisWeight(1);

          // Smear all quantities according to pre-defined distributions        
          double new_w_mass;
          thisWeight *= WSmearing.Evaluate(new_w_mass, myPSgen(myGenerator));
          double new_t_mass;
          thisWeight *= TopSmearing.Evaluate(new_t_mass, myPSgen(myGenerator));

#ifdef RECO_DEBUG
        std::cout << "W/top masses: " << new_w_mass << "/" << new_t_mass << std::endl;
#endif

          myLorentzVector gen_lepton1_p4, gen_lepton2_p4, gen_bjet1_p4, gen_bjet2_p4;
          
          if(isElEl || isElMu)
            thisWeight *= electronSmearing.Evaluate(lepton1_p4, gen_lepton1_p4, myPSgen(myGenerator));
          if(isMuEl || isMuMu)
            thisWeight *= muonSmearing.Evaluate(lepton1_p4, gen_lepton1_p4, myPSgen(myGenerator));
          if(isElEl || isMuEl)
            thisWeight *= electronSmearing.Evaluate(lepton2_p4, gen_lepton2_p4, myPSgen(myGenerator));
          if(isElMu || isMuMu)
            thisWeight *= muonSmearing.Evaluate(lepton2_p4, gen_lepton2_p4, myPSgen(myGenerator));
            
          thisWeight *= bJetSmearing.Evaluate(bjet1_p4, gen_bjet1_p4, myPSgen(myGenerator));
          thisWeight *= bJetSmearing.Evaluate(bjet2_p4, gen_bjet2_p4, myPSgen(myGenerator));

#ifdef RECO_DEBUG
          PRINT_VECTORS(lepton1_p4)
          PRINT_VECTORS(lepton2_p4)
          PRINT_VECTORS(bjet1_p4)
          PRINT_VECTORS(bjet2_p4)
          PRINT_VECTOR(met_p4)
          std::cout << "Weight: " << thisWeight << std::endl;
#endif
      
          // Convention: first top = positive charge
          if(lepton1_charge < 0)
            std::swap(gen_lepton1_p4, gen_lepton2_p4);
          
          // Get neutrino solutions, reconstruct ttbar system
          NeutrinosSolver mySolver(new_t_mass, new_w_mass);
          std::vector<TTAnalysis::TTBar> this_ttbar;

          auto neutrinos = mySolver.getNeutrinos(
              NeutrinosSolver::LorentzVector(gen_lepton1_p4),
              NeutrinosSolver::LorentzVector(gen_lepton2_p4),
              NeutrinosSolver::LorentzVector(gen_bjet1_p4),
              NeutrinosSolver::LorentzVector(gen_bjet2_p4),
              NeutrinosSolver::LorentzVector(met_p4));

#ifdef RECO_DEBUG
        std::cout << "First permutation: " << neutrinos.size() << " solutions.\n";
#endif
        
          for(const auto& thisPair: neutrinos)
            this_ttbar.push_back( TTAnalysis::TTBar(1, myLorentzVector(gen_lepton1_p4+gen_bjet1_p4+myLorentzVector(thisPair.first)), myLorentzVector(gen_lepton2_p4+gen_bjet2_p4+myLorentzVector(thisPair.second))) );

          // Add this solution to the weighted average
          solution += thisWeight*TTbarSolution(this_ttbar.at(0));
          totWeight += thisWeight;
      }

      // No solutions found! Return dummy "invalid" solution
      if( solution.nSols == 0 )
        return solution;

      // Success: return valid solution 
      solution *= 1/totWeight;
      return solution;
    }
    
  private:

    SmearingFunction& electronEnergySmearing;
    SmearingFunction& electronAngleSmearing;
    SmearingFunction& muonEnergySmearing;
    SmearingFunction& muonAngleSmearing;
    SmearingFunction& bJetEnergySmearing;
    SmearingFunction& bJetAngleSmearing;
    SmearingFunction& WSmearing;
    SmearingFunction& TopSmearing;
    
    SmearingFunction& MlbWeighting;

    uint32_t nTries;
};

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

void fixMass(myLorentzVector& v, const double mass){
  const double pRatio = sqrt(pow(v.E(), 2) - pow(mass, 2))/v.P();
  v.SetPtEtaPhiE(v.Pt()*pRatio, v.Eta(), v.Phi(), v.E());
}

class TTbarSolution {
  public:

    TTbarSolution():
      t_px(0), t_py(0), t_pz(0),
      tbar_px(0), tbar_py(0), tbar_pz(0),
      nSols(0), weight(0), 
      diLepDiJetMetIdx(0), 
      diLepIdx(0), leptonTIdx(0), leptonTbarIdx(0),
      diJetIdx(0), jetTIdx(0), jetTbarIdx(0)
      {}
    
    TTbarSolution(
        double t_px, double t_py, double t_pz,
        double tbar_px, double tbar_py, double tbar_pz):
      t_px(t_px), t_py(t_py), t_pz(t_pz),
      tbar_px(tbar_px), tbar_py(tbar_py), tbar_pz(tbar_pz),
      nSols(0), weight(0), 
      diLepDiJetMetIdx(0), 
      diLepIdx(0), leptonTIdx(0), leptonTbarIdx(0),
      diJetIdx(0), jetTIdx(0), jetTbarIdx(0)
      {}
    
    TTbarSolution(const TTAnalysis::TTBar& tt):
      t_px(tt.top1_p4.Px()), t_py(tt.top1_p4.Py()), t_pz(tt.top1_p4.Pz()),
      tbar_px(tt.top2_p4.Px()), tbar_py(tt.top2_p4.Py()), tbar_pz(tt.top2_p4.Pz()),
      nSols(1), weight(0), 
      diLepDiJetMetIdx(0), 
      diLepIdx(0), leptonTIdx(0), leptonTbarIdx(0),
      diJetIdx(0), jetTIdx(0), jetTbarIdx(0)
      {}

    ~TTbarSolution() {}

    TTbarSolution& operator+=(const TTbarSolution& sol){
      t_px += sol.t_px; t_py += sol.t_py; t_pz += sol.t_pz;
      tbar_px += sol.tbar_px; tbar_py += sol.tbar_py; tbar_pz += sol.tbar_pz;
      nSols += sol.nSols;
      return *this;
    }

    friend TTbarSolution operator*(const double w, const TTbarSolution& sol){
      return TTbarSolution(
          w*sol.t_px, w*sol.t_py, w*sol.t_pz,
          w*sol.tbar_px, w*sol.tbar_py, w*sol.tbar_pz
          );
    }

    TTbarSolution& operator*=(const double w){
      t_px *= w; t_py *= w; t_pz *= w;
      tbar_px *= w; tbar_py *= w; tbar_pz *= w;
      return *this;
    }

    TTbarSolution& BuildTopLorentzVectors(const double t_mass=172.5){
      const double t_E = sqrt( pow(t_mass, 2) + pow(t_px, 2) + pow(t_py, 2) + pow(t_pz, 2) );
      p4_t.SetPxPyPzE(t_px, t_py, t_pz, t_E);
    
      const double tbar_E = sqrt( pow(tbar_mass, 2) + pow(tbar_px, 2) + pow(tbar_py, 2) + pow(tbar_pz, 2) );
      p4_tbar.SetPxPyPzE(tbar_px, tbar_py, tbar_pz, tbar_E);
      p4_ttbar = p4_t + p4_tbar;
      return *this;
    }
    
    double t_px, t_py, t_pz;
    double tbar_px, tbar_py, tbar_pz;
    uint32_t nSols;
    double weight;

    LorentzVector p4_t, p4_tbar, p4_ttbar;
    uint16_t diLepDiJetMetIdx, diLepIdx, leptonTIdx, leptonTbarIdx, diJetIdx, jetTIdx, jetTbarIdx;
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
        myLorentzVector& met_p4
        std::vector<uint16_t>& selObj_CSVv2Ordered){

#ifdef RECO_DEBUG
        std::cout << "\nStarting event\n";
#endif

      // Use a lambda to handle more easily the b-jet permutations
      auto doSmearing = [&](const uint16_t idx, const bool switchBJets) {

        const TTAnalysis::DiLepDiJetMet& _thisObj = _diLepDiJetsMet[idx];
        const bool isElEl = _diLeptons[ _thisObj.diLepIdx ].isElEl;
        const bool isElMu = _diLeptons[ _thisObj.diLepIdx ].isElMu;
        const bool isMuEl = _diLeptons[ _thisObj.diLepIdx ].isMuEl;
        const bool isMuMu = _diLeptons[ _thisObj.diLepIdx ].isMuMu;

        myLorentzVector lepton1_p4 = _leptons[ _diLeptons[ _thisObj.diLepIdx ].lidxs.first ].p4;
        myLorentzVector lepton2_p4 = _leptons[ _diLeptons[ _thisObj.diLepIdx ].lidxs.second ].p4;
        myLorentzVector bjet1_p4 = _jets[ _diJets[ _thisObj.diJetIdx ].jidxs.first ].p4;
        myLorentzVector bjet2_p4 = _jets[ _diJets[ _thisObj.diJetIdx ].jidxs.second ].p4;
      
        double totWeight(0);
        TTbarSolution solution;

        // Do smearing
        for(uint32_t i = 0; i < nTries; ++i){

          // Smear all quantities according to pre-defined distributions        
          double new_wplus_mass, new_wminus_mass;
          WSmearing.Evaluate(new_wplus_mass, true); 
          WSmearing.Evaluate(new_wminus_mass, true); 
          double new_t_mass, new_tbar_mass;
          TopSmearing.Evaluate(new_t_mass, true); 
          TopSmearing.Evaluate(new_tbar_mass, true); 

#ifdef RECO_DEBUG
        std::cout << "W+/top masses: " << new_wplus_mass << "/" << new_t_mass << std::endl;
        std::cout << "W-/anti-top masses: " << new_wminus_mass << "/" << new_tbar_mass << std::endl;
#endif

          myLorentzVector gen_lepton1_p4, gen_lepton2_p4, gen_bjet1_p4, gen_bjet2_p4;
          
          if(isElEl || isElMu){
            electronEnergySmearing.Evaluate(lepton1_p4, gen_lepton1_p4);
            electronAngleSmearing.Evaluate(lepton1_p4, gen_lepton1_p4);
          }
          if(isMuEl || isMuMu){
            muonEnergySmearing.Evaluate(lepton1_p4, gen_lepton1_p4);
            muonAngleSmearing.Evaluate(lepton1_p4, gen_lepton1_p4);
          }
          if(isElEl || isMuEl){
            electronEnergySmearing.Evaluate(lepton2_p4, gen_lepton2_p4);
            electronAngleSmearing.Evaluate(lepton2_p4, gen_lepton2_p4);
          }
          if(isElMu || isMuMu){
            muonEnergySmearing.Evaluate(lepton2_p4, gen_lepton2_p4);
            muonAngleSmearing.Evaluate(lepton2_p4, gen_lepton2_p4);
          }
          
          bJetEnergySmearing.Evaluate(bjet1_p4, gen_bjet1_p4);
          bJetEnergySmearing.Evaluate(bjet2_p4, gen_bjet2_p4);
          bJetAngleSmearing.Evaluate(bjet1_p4, gen_bjet1_p4);
          bJetAngleSmearing.Evaluate(bjet2_p4, gen_bjet2_p4);

          // Fix the lepton & b-quark mass to what we know they are
          fixMass(lepton1_p4, 0); 
          fixMass(lepton2_p4, 0); 
          fixMass(bjet1_p4, 4.8); 
          fixMass(bjet2_p4, 4.8); 

#ifdef RECO_DEBUG
          PRINT_VECTORS(lepton1_p4)
          PRINT_VECTORS(lepton2_p4)
          PRINT_VECTORS(bjet1_p4)
          PRINT_VECTORS(bjet2_p4)
          PRINT_VECTOR(met_p4)
#endif
      
          // Convention: first top = positive charge
          if(_leptons[ _diLeptons[ thisObj.diLepIdx ].lidxs.first ].charge  < 0)
            std::swap(gen_lepton1_p4, gen_lepton2_p4);

          if(switchBJets)
            std::swap(gen_bjet1_p4, gen_bjet2_p4);
          
          // Get neutrino solutions, reconstruct ttbar system
          NeutrinosSolver mySolver(new_t_mass, new_tbar_mass, new_wplus_mass, new_wminus_mass);
          std::vector<TTAnalysis::TTBar> this_ttbar;

          auto neutrinos = mySolver.getNeutrinos(
              NeutrinosSolver::LorentzVector(gen_lepton1_p4),
              NeutrinosSolver::LorentzVector(gen_lepton2_p4),
              NeutrinosSolver::LorentzVector(gen_bjet1_p4),
              NeutrinosSolver::LorentzVector(gen_bjet2_p4),
              NeutrinosSolver::LorentzVector(met_p4)
              );

#ifdef RECO_DEBUG
          std::cout << "Jet pair [" << idx << ": found " << neutrinos.size() << " solutions.\n";
#endif

          if(!neutrinos.size())
            continue;
        
          // Solve according to decreasing TT invariant mass
          for(const auto& thisPair: neutrinos)
            this_ttbar.push_back( TTAnalysis::TTBar(1, myLorentzVector(gen_lepton1_p4+gen_bjet1_p4+myLorentzVector(thisPair.first)), myLorentzVector(gen_lepton2_p4+gen_bjet2_p4+myLorentzVector(thisPair.second))) );
          std::sort(this_ttbar.begin(), this_ttbar.end(), [](const TTAnalysis:TTBar& a, const TTAnalysis::TTBar& b){ return a.p4.M() < b.p4.M(); } );

          // Evaluate Mlb templates and compute weight
          const double thisWeight = MlbWeighting.Evaluate((gen_lepton1_p4+gen_bjet1_p4).M()) * MlbWeighting.Evaluate((gen_lepton2_p4+gen_bjet2_p4).M());
          
          // Add this solution to the weighted average
          // This increments the nSols variable
          solution += thisWeight*TTbarSolution(this_ttbar.at(0));
          totWeight += thisWeight;
        }

        // If no solution is found, return dummy object
        if(!solution.nSols)
          return TTbarSolution();
      
        solution *= 1/totWeight;
        solution.weight = totWeight;

        // Retrieve all the objects used for this particular solution
        solution.diLepDiJetMetIdx = idx;
        
        solution.diLepIdx = thisObj.diLepIdx;
        if(_leptons[ _diLeptons[ thisObj.diLepIdx ].lidxs.first ].charge  > 0) {
          solution.leptonTIdx = _diLeptons[ thisObj.diLepIdx ].first;
          solution.leptonTbarIdx = _diLeptons[ thisObj.diLepIdx ].second;
        } else {
          solution.leptonTIdx = _diLeptons[ thisObj.diLepIdx ].second;
          solution.leptonTbarIdx = _diLeptons[ thisObj.diLepIdx ].first;
        }
        
        solution.diJetIdx = thisObj.diJetIdx;
        if(!switchBJets) {
          solution.jetTIdx = _diJets[ thisObj.diJetIdx ].first;
          solution.jetTbarIdx = _diJets[ thisObj.diJetIdx ].second;
        } else {
          solution.jetTIdx = _diJets[ thisObj.diJetIdx ].second;
          solution.jetTbarIdx = _diJets[ thisObj.diJetIdx ].first;
        }

        // Return solution, without forgetting to build the top 4-vectors
        return solution.BuildTopLorentzVectors();
      }

      std::vector<TTbarSolution> solCollection;

      // For all jet pairs, do the smearing
      for(uint16_t idx: selObj_CSVv2Ordered) {
        // Two jet permutations
        solCollection.append(doSmearing(idx, false));
        solCollection.append(doSmearing(idx, true));
      }
      
      // Sort solutions according to decreasing total weight
      std::sort(solCollection.begin(), solCollection.end(), [](const TTbarSolution& s1, const TTbarSolution& s2){ return s1.weight > s2.weight; });

      // Return solution with highest weight
      return solCollection[0];
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

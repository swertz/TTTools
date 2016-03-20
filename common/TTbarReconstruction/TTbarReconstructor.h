#pragma once

#include <cp3_llbb/TTAnalysis/interface/Types.h>
#include <cp3_llbb/TTAnalysis/interface/NeutrinosSolver.h>

#include <iostream>
#include <algorithm>
#include <utility>
#include <random>

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

// We need to average every quantity separately, not the 4-vectors, hence this agregate:
class TTbarSolution {
  public:

    TTbarSolution():
      t_pt(0), t_eta(0), t_phi(0), t_m(0), t_y(0), t_e(0),
      tbar_pt(0), tbar_eta(0), tbar_phi(0), tbar_m(0), tbar_y(0), tbar_e(0),
      ttbar_pt(0), ttbar_eta(0), ttbar_phi(0), ttbar_m(0), ttbar_y(0), ttbar_e(0),
      ttbar_DR(0), ttbar_DPhi(0), ttbar_DEta(0), nSols(0) {}
    
    TTbarSolution(
        double t_pt, double t_eta, double t_phi, double t_m, double t_y, double t_e,
        double tbar_pt, double tbar_eta, double tbar_phi, double tbar_m, double tbar_y, double tbar_e,
        double ttbar_pt, double ttbar_eta, double ttbar_phi, double ttbar_m, double ttbar_y, double ttbar_e,
        double ttbar_DR, double ttbar_DPhi, double ttbar_DEta):
      t_pt(t_pt), t_eta(t_eta), t_phi(t_phi), t_m(t_m), t_y(t_y), t_e(t_e),
      tbar_pt(tbar_pt), tbar_eta(tbar_eta), tbar_phi(tbar_phi), tbar_m(tbar_m), tbar_y(tbar_y), tbar_e(tbar_e),
      ttbar_pt(ttbar_pt), ttbar_eta(ttbar_eta), ttbar_phi(ttbar_phi), ttbar_m(ttbar_m), ttbar_y(ttbar_y), ttbar_e(ttbar_e),
      ttbar_DR(ttbar_DR), ttbar_DPhi(ttbar_DPhi), ttbar_DEta(ttbar_DEta), nSols(1) {}
    
    TTbarSolution(const TTAnalysis::TTBar& tt):
      t_pt(tt.top1_p4.Pt()), t_eta(tt.top1_p4.Eta()), t_phi(tt.top1_p4.Phi()), t_m(tt.top1_p4.M()), t_y(tt.top1_p4.Rapidity()), t_e(tt.top1_p4.E()),
      tbar_pt(tt.top2_p4.Pt()), tbar_eta(tt.top2_p4.Eta()), tbar_phi(tt.top2_p4.Phi()), tbar_m(tt.top2_p4.M()), tbar_y(tt.top2_p4.Rapidity()), tbar_e(tt.top2_p4.E()),
      ttbar_pt(tt.p4.Pt()), ttbar_eta(tt.p4.Eta()), ttbar_phi(tt.p4.Phi()), ttbar_m(tt.p4.M()), ttbar_y(tt.p4.Rapidity()), ttbar_e(tt.p4.E()),
      ttbar_DR(tt.DR_tt), ttbar_DPhi(tt.DPhi_tt), ttbar_DEta(tt.DEta_tt), nSols(1) {}

    ~TTbarSolution() {}

    TTbarSolution& operator+=(const TTbarSolution& sol){
      t_pt += sol.t_pt; t_eta += sol.t_eta; t_phi += sol.t_phi; t_y += sol.t_y; t_e += sol.t_e;
      tbar_pt += sol.tbar_pt; tbar_eta += sol.tbar_eta; tbar_phi += sol.tbar_phi; tbar_y += sol.tbar_y; tbar_e += sol.tbar_e;
      ttbar_pt += sol.ttbar_pt; ttbar_eta += sol.ttbar_eta; ttbar_phi += sol.ttbar_phi; ttbar_m += sol.ttbar_m; ttbar_y += sol.ttbar_y; ttbar_e += sol.ttbar_e;
      ttbar_DR += sol.ttbar_DR; ttbar_DPhi += sol.ttbar_DPhi; ttbar_DEta += sol.ttbar_DEta;
      nSols += sol.nSols;
      return *this;
    }

    friend TTbarSolution operator*(const double w, const TTbarSolution& sol){
      TTbarSolution tempSol(
          w*sol.t_pt, w*sol.t_eta, w*sol.t_phi, w*sol.t_m, w*sol.t_y, w*sol.t_e,
          w*sol.tbar_pt, w*sol.tbar_eta, w*sol.tbar_phi, w*sol.tbar_m, w*sol.tbar_y, w*sol.tbar_e,
          w*sol.ttbar_pt, w*sol.ttbar_eta, w*sol.ttbar_phi, w*sol.ttbar_m, w*sol.ttbar_y, w*sol.ttbar_e,
          w*sol.ttbar_DR, w*sol.ttbar_DPhi, w*sol.ttbar_DEta);
      return tempSol;
    }

    TTbarSolution& operator*=(const double w){
      t_pt *= w; t_eta *= w; t_phi *= w; t_y *= w; t_e *= w;
      tbar_pt *= w; tbar_eta *= w; tbar_phi *= w; tbar_y *= w; tbar_e *= w;
      ttbar_pt *= w; ttbar_eta *= w; ttbar_phi *= w; ttbar_m *= w; ttbar_y *= w; ttbar_e *= w;
      ttbar_DR *= w; ttbar_DPhi *= w; ttbar_DEta *= w;
      return *this;
    }
    
    double t_pt, t_eta, t_phi, t_m, t_y, t_e;
    double tbar_pt, tbar_eta, tbar_phi, tbar_m, tbar_y, tbar_e;
    double ttbar_pt, ttbar_eta, ttbar_phi, ttbar_m, ttbar_y, ttbar_e;
    double ttbar_DR, ttbar_DPhi, ttbar_DEta;
    uint32_t nSols;
};


class TTbarReconstructor {
  public:
    
    TTbarReconstructor(SmearingFunction& muonSmearing, SmearingFunction& electronSmearing, SmearingFunction& bJetSmearing, SmearingFunction& WSmearing, SmearingFunction& TopSmearing, uint32_t nTries):
      muonSmearing(muonSmearing),
      electronSmearing(electronSmearing),
      bJetSmearing(bJetSmearing),
      WSmearing(WSmearing),
      TopSmearing(TopSmearing),
      nTries(nTries),
      myPSgen(0,1)
    {}

    TTbarSolution getSolution(
        const myLorentzVector& lepton1_p4,
        const myLorentzVector& lepton2_p4,
        const myLorentzVector& bjet1_p4,
        const myLorentzVector& bjet2_p4,
        const myLorentzVector& met_p4,
        const bool isElEl, const bool isElMu, const bool isMuEl, const bool isMuMu,
        const int16_t lepton1_charge){

#ifdef RECO_DEBUG
        std::cout << "\nStarting event\n";
#endif
      
      if( (!isElEl && !isElMu && !isMuEl && !isMuMu) || (isElEl+isMuEl+isElMu+isMuMu) > 1){
        std::cout << "Error: channel is wrongly specified" << std::endl;
        return TTAnalysis::TTBar(0, myLorentzVector(), myLorentzVector());
      }

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

        // Do it again, swapping b and bbar
        std::swap(gen_bjet1_p4, gen_bjet2_p4);
        neutrinos = mySolver.getNeutrinos(
            NeutrinosSolver::LorentzVector(gen_lepton1_p4),
            NeutrinosSolver::LorentzVector(gen_lepton2_p4),
            NeutrinosSolver::LorentzVector(gen_bjet1_p4),
            NeutrinosSolver::LorentzVector(gen_bjet2_p4),
            NeutrinosSolver::LorentzVector(met_p4));

#ifdef RECO_DEBUG
        std::cout << "Second permutation: " << neutrinos.size() << " solutions.\n";
#endif
        
        for(const auto& thisPair: neutrinos)
          this_ttbar.push_back( TTAnalysis::TTBar(1, myLorentzVector(gen_lepton1_p4+gen_bjet1_p4+myLorentzVector(thisPair.first)), myLorentzVector(gen_lepton2_p4+gen_bjet2_p4+myLorentzVector(thisPair.second))) );

        // Sort the solutions according to invariant TTbar mass, to keep only the lowest mass
        std::sort(this_ttbar.begin(), this_ttbar.end(), [](const TTAnalysis::TTBar& a, const TTAnalysis::TTBar& b) { return a.p4.M() < b.p4.M(); } );

        if( !this_ttbar.size() )
          continue;

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

    SmearingFunction& muonSmearing;
    SmearingFunction& electronSmearing;
    SmearingFunction& bJetSmearing;
    SmearingFunction& WSmearing;
    SmearingFunction& TopSmearing;

    uint32_t nTries;

    std::uniform_real_distribution<double> myPSgen;
    std::mt19937_64 myGenerator;
};

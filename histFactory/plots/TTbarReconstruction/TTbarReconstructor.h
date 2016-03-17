#pragma once

#include <cp3_llbb/TTAnalysis/interface/Types.h>
#include <cp3_llbb/TTAnalysis/interface/NeutrinosSolver.h>

#include <iostream>
#include <algorithm>
#include <utility>
#include <random>

#include <Math/Vector4D.h>

//#define RECO_DEBUG

#define PRINT_VECTOR(vec) std::cout << "Vector " << #vec << ": " << vec << std::endl;

#define PRINT_VECTORS(vec) \
  PRINT_VECTOR(vec) \
  PRINT_VECTOR(gen_##vec)

// Needed because it is defined in TTAnalyzer.cc, which is not compiled here
float TTAnalysis::DeltaEta(const myLorentzVector& v1, const myLorentzVector& v2) {
    return std::abs(v1.Eta() - v2.Eta());
}

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

    TTAnalysis::TTBar getSolution(
        const myLorentzVector& lepton1_p4,
        const myLorentzVector& lepton2_p4,
        const myLorentzVector& bjet1_p4,
        const myLorentzVector& bjet2_p4,
        const myLorentzVector& met_p4,
        const bool isElEl, const bool isElMu, const bool isMuEl, const bool isMuMu){

#ifdef RECO_DEBUG
        std::cout << "\nStarting event\n";
#endif
      
      if( (!isElEl && !isElMu && !isMuEl && !isMuMu) || (isElEl+isMuEl+isElMu+isMuMu) > 1){
        std::cout << "Error: channel is wrongly specified" << std::endl;
        return TTAnalysis::TTBar(0, myLorentzVector(), myLorentzVector());
      }

      myLorentzVector top_p4, antiTop_p4;
      double totWeight(0);

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
        
        top_p4 += thisWeight * this_ttbar.at(0).top1_p4; 
        antiTop_p4 += thisWeight * this_ttbar.at(0).top2_p4; 
        totWeight += thisWeight;
      }

      // No solutions found! Return dummy solution with index set to 0
      if( totWeight == 0 )
        return TTAnalysis::TTBar(0, myLorentzVector(), myLorentzVector());

      top_p4 /= totWeight;
      antiTop_p4 /= totWeight;
      
      // Success: return solution with index set to 1
      return TTAnalysis::TTBar(1, top_p4, antiTop_p4);
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

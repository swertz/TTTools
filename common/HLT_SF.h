#include <vector>
#include <utility>

float get_HLT_SF_for_dilepton(bool isMC, bool isElEl, bool isMuEl, bool isElMu, bool isMuMu, float eta1, float eta2){
  
  if(!isMC)
    return 1;

  auto bin = [](float eta_leg1, float eta_leg2) -> std::pair<size_t, size_t> {
    size_t bin1 = std::abs(eta_leg1) <= 1.2 ? 0 : 1;
    size_t bin2 = std::abs(eta_leg2) <= 1.2 ? 0 : 1;

    return std::make_pair(bin1, bin2);
  };
    
  auto sel_bin = bin(eta1, eta2);

  if(isElEl){
    static std::vector< std::vector<float> > SF = { {0.953, 0.957}, {0.967, 0.989} };
    return SF[sel_bin.first][sel_bin.second];
  }
  if(isElMu || isMuEl){
    static std::vector< std::vector<float> > SF = { {0.966, 0.973}, {0.981, 0.984} };
    return SF[sel_bin.first][sel_bin.second];
  }
  if(isMuMu){
    static std::vector< std::vector<float> > SF = { {0.926, 0.943}, {0.958, 0.926} };
    return SF[sel_bin.first][sel_bin.second];
  }

  return 1.;
}

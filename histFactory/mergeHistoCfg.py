toJoin = [
        # Matching
        {
            "match": r"DR_b(bar)?_CAT.*", 
            "newName": "DR_gen_matched",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
        },
        {
            "match": r"DR_b(bar)?_vs_DRgen_CAT.*", 
            "newName": "DR_gen_vs_DR_matched",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
        },
        {
            "match": r"Matched_b(bar)?_CSVv2_.*", 
            "newName": "Matched_bORbbar_CSVv2",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
            "normalise": True
        },
        {
            "match": r"Matched_b_bbar_CSVv2_.*", 
            "newName": "Matched_bANDbbar_CSVv2",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
            "normalise": True
        },
        {
            "match": r"Matched_b(bar)?_Pt_.*", 
            "newName": "Matched_bORbbar_Pt",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
            "normalise": True
        },
        {
            "match": r"Matched_b_bbar_Pt_.*", 
            "newName": "Matched_bANDbbar_Pt",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
            "normalise": True
        },
        
        # GEN info
        {
            "match": r"gen_T(bar)?_DRbl_vs_TT_M_CAT.*", 
            "newName": "gen_DRbl_vs_TT_M",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
        },
        {
            "match": r"gen_T(bar)?_Mbl_CAT.*", 
            "newName": "gen_Mbl",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
            "normalise": True
        },
        {
            "match": r"gen_TT_Mbl_vs_Mbl_CAT.*", 
            "newName": "gen_Mbl_vs_Mbl",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
            "normalise": True
        },
        {
            "match": r"gen_T(bar)?_Mbl_vs_TT_M_CAT.*", 
            "newName": "gen_Mbl_vs_TT_M",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
            "normalise": True
        },
        {
            "match": r"gen_T(bar)?_MW_CAT.*", 
            "newName": "gen_MW",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
        },
        
        # TT reco
        {
            "match": r"llbbMet_RecoTop_(Anti)?Top_Pt_CAT.*", 
            "newName": "Reco_Top_Pt",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
        },
        {
            "match": r"llbbMet_RecoTop_(Anti)?Top_Eta_CAT.*", 
            "newName": "Reco_Top_Eta",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
        },
        {
            "match": r"llbbMet_RecoTop_(Anti)?Top_Rapidity_CAT.*", 
            "newName": "Reco_Top_Rapidity",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
        },
        {
            "match": r"llbbMet_RecoTop_TT_Pt_CAT.*", 
            "newName": "Reco_TTbar_Pt",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
        },
        {
            "match": r"llbbMet_RecoTop_TT_Eta_CAT.*", 
            "newName": "Reco_TTbar_Eta",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
        },
        {
            "match": r"llbbMet_RecoTop_TT_Rapidity_CAT.*", 
            "newName": "Reco_TTbar_Rapidity",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
        },
        {
            "match": r"llbbMet_RecoTop_nSols_CAT.*", 
            "newName": "Reco_nSols",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
        },
        {
            "match": r"llbbMet_RecoTop_TT_M_Resolution_CAT.*", 
            "newName": "Reco_TTbar_M_Resolution",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
        },
        {
            "match": r"llbbMet_RecoTop_TT_M_minus_Mgen_CAT.*", 
            "newName": "Reco_TTbar_M_minus_Mgen",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
        },
        {
            "match": r"llbbMet_RecoTop_TT_M_minus_Mgen_vs_Mgen_CAT.*", 
            "newName": "Reco_TTbar_M_minus_Mgen_vs_Mgen",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
        },
        {
            "match": r"llbbMet_RecoTop_TT_M_Resolution_vs_Mgen_CAT.*", 
            "newName": "Reco_TTbar_M_Resolution_vs_Mgen",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
        },
        {
            "match": r"llbbMet_minDRbl_vs_gen_TT_M_CAT.*", 
            "newName": "Reco_TTbar_M_minus_Mgen_vs_Mgen",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
        },

        # Lepton "TFs"
        {
            "match": r"EgenOverEreco_electron_t(bar)?_CAT.*", 
            "newName": "EgenOverEreco_electron",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
            "normalise": True,
        },
        {
            "match": r"EgenOverEreco_muon_t(bar)?_CAT.*", 
            "newName": "EgenOverEreco_muon",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
            "normalise": True,
        },
        {
            "match": r"EgenOverEreco_((muon)|(electron))_t(bar)?_CAT.*", 
            "newName": "EgenOverEreco_lepton",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
            "normalise": True,
        },
        {
            "match": r"EgenOverEreco_vs_Egen_electron_t(bar)?_CAT.*", 
            "newName": "EgenOverEreco_vs_Egen_electron",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
            "normalise": True,
        },
        {
            "match": r"EgenOverEreco_vs_Egen_muon_t(bar)?_CAT.*", 
            "newName": "EgenOverEreco_vs_Egen_muon",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
            "normalise": True,
        },
        {
            "match": r"EgenOverEreco_vs_Egen_((muon)|(electron))_t(bar)?_CAT.*", 
            "newName": "EgenOverEreco_vs_Egen_lepton",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
            "normalise": True,
        },
        {
            "match": r"Angle_electron_t(bar)?_CAT.*", 
            "newName": "Angle_electron",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
            "normalise": True,
        },
        {
            "match": r"Angle_muon_t(bar)?_CAT.*", 
            "newName": "Angle_muon",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
            "normalise": True,
        },
        {
            "match": r"Angle_((muon)|(electron))_t(bar)?_CAT.*", 
            "newName": "Angle_lepton",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
            "normalise": True,
        },

        # B-jet "TFs"
        {
            "match": r"EgenOverEreco_b(bar)?_CAT.*", 
            "newName": "EgenOverEreco_bJet",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
            "normalise": True,
        },
        {
            "match": r"EgenOverEreco_vs_Egen_b(bar)?_CAT.*", 
            "newName": "EgenOverEreco_vs_Egen_bJet",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
            "normalise": True,
        },
        {
            "match": r"Angle_b(bar)?_CAT.*", 
            "newName": "Angle_bJet",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
            "normalise": True,
        },
        {
            "match": r"Angle_vs_Eta_b(bar)?_CAT.*", 
            "newName": "Angle_vs_Eta_bJet",
            "veto": r"(.*ZVeto.*)|(.*_jj.*)|(.*_Met)",
            "normalise": True,
        },
    ]

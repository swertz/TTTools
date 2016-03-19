toJoin = [
        # Matching
        {
            "match": r"DR_b(bar)?_CAT.*", 
            "newName": "DR_gen_matched",
            "veto": r".*ZVeto.*",
        },
        {
            "match": r"DR_b(bar)?_vs_DRgen_CAT.*", 
            "newName": "DR_gen_vs_DR_matched",
            "veto": r".*ZVeto.*",
        },
        {
            "match": r"Matched_b(bar)?_CSVv2_.*", 
            "newName": "Matched_bbar_CSVv2",
            "veto": r".*ZVeto.*",
            "normalise": True
        },
        {
            "match": r"Matched_b(bar)?_Pt_.*", 
            "newName": "Matched_bbar_Pt",
            "veto": r".*ZVeto.*",
            "normalise": True
        },
    ]

#toJoin = [
#        # TT reco
#        {
#            "match": r"llbbMet_RecoTop_(Anti)?Top_Pt_CAT.*", 
#            "newName": "Reco_Top_Pt",
#            "veto": r".*ZVeto.*",
#        },
#        {
#            "match": r"llbbMet_RecoTop_(Anti)?Top_Eta_CAT.*", 
#            "newName": "Reco_Top_Eta",
#            "veto": r".*ZVeto.*",
#        },
#        {
#            "match": r"llbbMet_RecoTop_(Anti)?Top_Rapidity_CAT.*", 
#            "newName": "Reco_Top_Rapidity",
#            "veto": r".*ZVeto.*",
#        },
#        {
#            "match": r"llbbMet_RecoTop_TT_M_CAT.*", 
#            "newName": "Reco_TTbar_M",
#            "veto": r".*ZVeto.*",
#        },
#        {
#            "match": r"llbbMet_RecoTop_TT_Pt_CAT.*", 
#            "newName": "Reco_TTbar_Pt",
#            "veto": r".*ZVeto.*",
#        },
#        {
#            "match": r"llbbMet_RecoTop_TT_Eta_CAT.*", 
#            "newName": "Reco_TTbar_Eta",
#            "veto": r".*ZVeto.*",
#        },
#        {
#            "match": r"llbbMet_RecoTop_TT_Rapidity_CAT.*", 
#            "newName": "Reco_TTbar_Rapidity",
#            "veto": r".*ZVeto.*",
#        },
#        {
#            "match": r"llbbMet_RecoTop_nSols_CAT.*", 
#            "newName": "Reco_nSols",
#            "veto": r".*ZVeto.*",
#        },
#        {
#            "match": r"llbbMet_RecoTop_TT_M_Resolution_CAT.*", 
#            "newName": "Reco_TTbar_M_Resolution",
#            "veto": r".*ZVeto.*",
#        },
#        {
#            "match": r"llbbMet_RecoTop_TT_M_minus_Mgen_CAT.*", 
#            "newName": "Reco_TTbar_M_minus_Mgen",
#            "veto": r".*ZVeto.*",
#        },
#        {
#            "match": r"llbbMet_RecoTop_TT_M_minus_Mgen_vs_Mgen_CAT.*", 
#            "newName": "Reco_TTbar_M_minus_Mgen_vs_Mgen",
#            "veto": r".*ZVeto.*",
#        },
#    ]

tree = {
    "name": "t",
    "cut": "1.",
    "branches": [
            ## Event
            {
                "name": "event_run",
                "variable": "event_run",
                "type": "ULong64_t"
            },
            {
                "name": "event_lumi",
                "variable": "event_lumi",
                "type": "ULong64_t"
            },
            {
                "name": "event_event",
                "variable": "event_event",
                "type": "ULong64_t"
            },
            {
                "name": "event_is_data",
                "variable": "event_is_data",
                "type": "bool"
            },
            ## Leptons
            {
                "name": "lep1_p4",
                "variable": "lepton1->p4",
                "type": "myLorentzVector"
            },
            {
                "name": "lep1_iso",
                "variable": "lepton1->isoValue"
            },
            {
                "name": "lep2_p4",
                "variable": "lepton2->p4",
                "type": "myLorentzVector"
            },
            {
                "name": "lep2_iso",
                "variable": "lepton2->isoValue"
            },
            {
                "name": "ll_p4",
                "variable": "diLepton->p4",
                "type": "myLorentzVector"
            },
            {
                "name": "ll_DR",
                "variable": "diLepton->DR"
            },
            {
                "name": "ll_DEta",
                "variable": "diLepton->DEta"
            },
            {
                "name": "ll_DPhi",
                "variable": "std::abs(diLepton->DPhi)"
            },
            ## B-Jets
            {
                "name": "bJet1_p4",
                "variable": "bJet1->p4",
                "type": "myLorentzVector"
            },
            {
                "name": "bJet1_CSVv2",
                "variable": "bJet1->CSVv2",
            },
            {
                "name": "bJet2_p4",
                "variable": "bJet2->p4",
                "type": "myLorentzVector"
            },
            {
                "name": "bJet2_CSVv2",
                "variable": "bJet2->CSVv2",
            },
            {
                "name": "bb_p4",
                "variable": "diBJet->p4",
                "type": "myLorentzVector"
            },
            {
                "name": "bb_DR",
                "variable": "diBJet->DR",
            },
            {
                "name": "bb_DEta",
                "variable": "diBJet->DEta",
            },
            {
                "name": "bb_DPhi",
                "variable": "std::abs(diBJet->DPhi)",
            },
            ## Leptons & B-Jets
            {
                "name": "llbb_p4",
                "variable": "diLepDiBJet->p4",
                "type": "myLorentzVector"
            },
            {
                "name": "llbb_DR_ll_bb",
                "variable": "diLepDiBJet->DR_ll_jj",
            },
            #{
            #    "name": "llbb_DEta_ll_bb",
            #    "variable": "diLepDiBJet->DEta_ll_jj",
            #},
            #{
            #    "name": "llbb_DPhi_ll_bb",
            #    "variable": "std::abs(diLepDiBJet->DPhi_ll_jj)",
            #},
            {
                "name": "llbb_minDRbl",
                "variable": "diLepDiBJet->minDRjl",
            },
            {
                "name": "llbb_maxDRbl",
                "variable": "diLepDiBJet->maxDRjl",
            },
            #{
            #    "name": "llbb_minDEtabl",
            #    "variable": "diLepDiBJet->minDEtajl",
            #},
            #{
            #    "name": "llbb_maxDEtabl",
            #    "variable": "diLepDiBJet->maxDEtajl",
            #},
            #{
            #    "name": "llbb_minDPhibl",
            #    "variable": "std::abs(diLepDiBJet->minDPhijl)",
            #},
            #{
            #    "name": "llbb_maxDPhibl",
            #    "variable": "std::abs(diLepDiBJet->maxDPhijl)",
            #},
            ## MET
            {
                "name": "met_p4",
                "variable": "met_p4",
                "type": "myLorentzVector"
            },
            ## Leptons, B-Jets, MET
            {
                "name": "llbbMet_p4",
                "variable": "diLepDiBJetMet->p4",
                "type": "myLorentzVector"
            },
            #{
            #    "name": "llbbMet_minDPhi_j_Met",
            #    "variable": "std::abs(diLepDiBJetMet->minDPhi_j_Met)",
            #    "type": "myLorentzVector"
            #},
            ## Gen info
            {
                "name": "gen_isTTbar",
                "variable": "tt_gen_ttbar_decay_type > TTAnalysis::NotTT",
                "type": "bool"
            },
            {
                "name": "gen_isHadronicTTbar",
                "variable": "tt_gen_ttbar_decay_type == TTAnalysis::Hadronic",
                "type": "bool"
            },
            {
                "name": "gen_isSemiLepTTbar",
                "variable": "tt_gen_ttbar_decay_type == TTAnalysis::Semileptonic_e || tt_gen_ttbar_decay_type == TTAnalysis::Semileptonic_mu || tt_gen_ttbar_decay_type == TTAnalysis::Semileptonic_tau",
                "type": "bool"
            },
            {
                "name": "gen_isDiLepTTbar",
                "variable": "(tt_gen_ttbar_decay_type >= TTAnalysis::Dileptonic_mumu && tt_gen_ttbar_decay_type <= TTAnalysis::Dileptonic_mue) || tt_gen_ttbar_decay_type >= TTAnalysis::Dileptonic_tautau",
                "type": "bool"
            },
            {
                "name": "gen_hasTau",
                "variable": "tt_gen_ttbar_decay_type >= TTAnalysis::Semileptonic_tau",
                "type": "bool"
            },
            {
                "name": "gen_isSignal",
                "variable": "tt_gen_ttbar_decay_type >= TTAnalysis::Dileptonic_mumu && tt_gen_ttbar_decay_type <= TTAnalysis::Dileptonic_mue",
                "type": "bool"
            },
            {
                "name": "gen_T_p4",
                "variable": "tt_gen_t_beforeFSR >= 0 ? tt_genParticles[tt_gen_t_beforeFSR].p4 : myLorentzVector()",
                "type": "myLorentzVector"
            },
            {
                "name": "gen_Tbar_p4",
                "variable": "tt_gen_tbar_beforeFSR >= 0 ? tt_genParticles[tt_gen_tbar_beforeFSR].p4 : myLorentzVector()",
                "type": "myLorentzVector"
            },
            {
                "name": "gen_TT_p4",
                "variable": "tt_gen_ttbar_beforeFSR_p4",
                "type": "myLorentzVector"
            },
            {
                "name": "gen_TT_DR",
                "variable": "tt_gen_t_tbar_deltaR"
            },
            {
                "name": "gen_TT_DEta",
                "variable": "tt_gen_t_tbar_deltaEta"
            },
            {
                "name": "gen_TT_DPhi",
                "variable": "tt_gen_t_tbar_deltaPhi"
            },
            {
                "name": "gen_lepton_T_p4",
                "variable": "tt_gen_lepton_t_beforeFSR >= 0 ? tt_genParticles[tt_gen_lepton_t_beforeFSR].p4 : myLorentzVector()",
                "type": "myLorentzVector"
            },
            {
                "name": "gen_neutrino_T_p4",
                "variable": "tt_gen_neutrino_t_beforeFSR >= 0 ? tt_genParticles[tt_gen_neutrino_t_beforeFSR].p4 : myLorentzVector()",
                "type": "myLorentzVector"
            },
            {
                "name": "gen_W_T_p4",
                "variable": "(tt_gen_neutrino_t_beforeFSR >= 0 && tt_gen_lepton_t_beforeFSR >= 0) ? tt_genParticles[tt_gen_neutrino_t_beforeFSR].p4 + tt_genParticles[tt_gen_lepton_t_beforeFSR].p4 : myLorentzVector()",
                "type": "myLorentzVector"
            },
            {
                "name": "gen_b_p4",
                "variable": "tt_gen_b_beforeFSR >= 0 ? tt_genParticles[tt_gen_b_beforeFSR].p4 : myLorentzVector()",
                "type": "myLorentzVector"
            },
            {
                "name": "gen_lepton_Tbar_p4",
                "variable": "tt_gen_lepton_tbar_beforeFSR >= 0 ? tt_genParticles[tt_gen_lepton_tbar_beforeFSR].p4 : myLorentzVector()",
                "type": "myLorentzVector"
            },
            {
                "name": "gen_neutrino_Tbar_p4",
                "variable": "tt_gen_neutrino_tbar_beforeFSR >= 0 ? tt_genParticles[tt_gen_neutrino_tbar_beforeFSR].p4 : myLorentzVector()",
                "type": "myLorentzVector"
            },
            {
                "name": "gen_W_Tbar_p4",
                "variable": "(tt_gen_neutrino_tbar_beforeFSR >= 0 && tt_gen_lepton_tbar_beforeFSR >= 0) ? tt_genParticles[tt_gen_neutrino_tbar_beforeFSR].p4 + tt_genParticles[tt_gen_lepton_tbar_beforeFSR].p4 : myLorentzVector()",
                "type": "myLorentzVector"
            },
            {
                "name": "gen_bbar_p4",
                "variable": "tt_gen_bbar_beforeFSR >= 0 ? tt_genParticles[tt_gen_bbar_beforeFSR].p4 : myLorentzVector()",
                "type": "myLorentzVector"
            },
            {
                "name": "gen_DR_lepton_bbar_p4",
                "variable": "(tt_gen_bbar_beforeFSR >= 0 && tt_gen_lepton_tbar_beforeFSR >=0) ? ROOT::Math::VectorUtil::DeltaR(tt_genParticles[tt_gen_bbar_beforeFSR].p4, tt_genParticles[tt_gen_lepton_tbar_beforeFSR].p4) : -1",
            },
            {
                "name": "gen_DR_lepton_b_p4",
                "variable": "(tt_gen_b_beforeFSR >= 0 && tt_gen_lepton_t_beforeFSR >=0) ? ROOT::Math::VectorUtil::DeltaR(tt_genParticles[tt_gen_b_beforeFSR].p4, tt_genParticles[tt_gen_lepton_t_beforeFSR].p4) : -1",
            },
            ## Matching
            ## Simple reco TTbar
            {
                "name": "simpleRecoTop_T_p4",
                "variable": "tt_ttbar[leplepIDIsoBB][0].size() ? tt_ttbar[leplepIDIsoBB][0][0].top1_p4 : myLorentzVector()",
                "type": "myLorentzVector"
            },
            {
                "name": "simpleRecoTop_Tbar_p4",
                "variable": "tt_ttbar[leplepIDIsoBB][0].size() ? tt_ttbar[leplepIDIsoBB][0][0].top2_p4 : myLorentzVector()",
                "type": "myLorentzVector"
            },
            {
                "name": "simpleRecoTop_TT_p4",
                "variable": "tt_ttbar[leplepIDIsoBB][0].size() ? tt_ttbar[leplepIDIsoBB][0][0].p4 : myLorentzVector()",
                "type": "myLorentzVector"
            },
            {
                "name": "simpleRecoTop_TT_DR",
                "variable": "tt_ttbar[leplepIDIsoBB][0].size() ? tt_ttbar[leplepIDIsoBB][0][0].DR_tt : -1",
            },
            {
                "name": "simpleRecoTop_TT_DEta",
                "variable": "tt_ttbar[leplepIDIsoBB][0].size() ? tt_ttbar[leplepIDIsoBB][0][0].DEta_tt : -1",
            },
            {
                "name": "simpleRecoTop_TT_DPhi",
                "variable": "tt_ttbar[leplepIDIsoBB][0].size() ? std::abs(tt_ttbar[leplepIDIsoBB][0][0].DPhi_tt) : -1",
            },
            {
                "name": "simpleRecoTop_iValid",
                "variable": "tt_ttbar[leplepIDIsoBB][0].size() > 0",
                "type": "bool"
            },
            ## Full reco TTbar
            {
                "name": "recoTop_T_pt",
                "variable": "recoTTbar.nSols > 0 ? recoTTbar.t_pt : -1",
            },
            {
                "name": "recoTop_T_eta",
                "variable": "recoTTbar.nSols > 0 ? recoTTbar.t_eta : -10",
            },
            {
                "name": "recoTop_T_phi",
                "variable": "recoTTbar.nSols > 0 ? recoTTbar.t_phi : -10",
            },
            {
                "name": "recoTop_T_y",
                "variable": "recoTTbar.nSols > 0 ? recoTTbar.t_y : -10",
            },
            {
                "name": "recoTop_Tbar_pt",
                "variable": "recoTTbar.nSols > 0 ? recoTTbar.tbar_pt : -1",
            },
            {
                "name": "recoTop_Tbar_eta",
                "variable": "recoTTbar.nSols > 0 ? recoTTbar.tbar_eta : -10",
            },
            {
                "name": "recoTop_Tbar_phi",
                "variable": "recoTTbar.nSols > 0 ? recoTTbar.tbar_phi : -10",
            },
            {
                "name": "recoTop_Tbar_y",
                "variable": "recoTTbar.nSols > 0 ? recoTTbar.tbar_y : -10",
            },
            {
                "name": "recoTop_TT_m",
                "variable": "recoTTbar.nSols > 0 ? recoTTbar.ttbar_m : -1",
            },
            {
                "name": "recoTop_TT_pt",
                "variable": "recoTTbar.nSols > 0 ? recoTTbar.ttbar_pt : -1",
            },
            {
                "name": "recoTop_TT_eta",
                "variable": "recoTTbar.nSols > 0 ? recoTTbar.ttbar_eta : -10",
            },
            {
                "name": "recoTop_TT_phi",
                "variable": "recoTTbar.nSols > 0 ? recoTTbar.ttbar_phi : -10",
            },
            {
                "name": "recoTop_TT_y",
                "variable": "recoTTbar.nSols > 0 ? recoTTbar.ttbar_y : -10",
            },
            {
                "name": "recoTop_TT_DR",
                "variable": "recoTTbar.nSols > 0 ? recoTTbar.ttbar_DR : -1",
            },
            {
                "name": "recoTop_TT_DEta",
                "variable": "recoTTbar.nSols > 0 ? recoTTbar.ttbar_DEta : -1",
            },
            {
                "name": "recoTop_TT_DPhi",
                "variable": "recoTTbar.nSols > 0 ? recoTTbar.ttbar_DPhi : -1",
            },
            {
                "name": "recoTop_TT_nSols",
                "variable": "recoTTbar.nSols",
            },
        ],
    }


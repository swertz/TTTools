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
            {
                "name": "cut_isOS",
                "variable": "diLepton_isOS",
                "type": "bool"
            },
            {
                "name": "cut_Mll",
                "variable": "diLepton_Mll",
                "type": "bool"
            },
            {
                "name": "cut_ZVeto",
                "variable": "diLepton_ZVeto",
                "type": "bool"
            },
            {
                "name": "cut_HLT",
                "variable": "diLepton_HLT",
                "type": "bool"
            },
            {
                "name": "event_weight",
                "variable": "event_weight*event_pu_weight",
            },
            {
                "name": "sf_HLT",
                "variable": "sf_HLT",
            },
            {
                "name": "sf_leptons",
                "variable": "sf_diLepton",
            },
            {
                "name": "sf_bJets",
                "variable": "sf_diBJet",
            },
            {
                "name": "sf_comb",
                "variable": "sf_HLT*sf_diLepton*sf_diBJet",
            },
            {
                "name": "event_all",
                "variable": "event_weight * event_pu_weight * sf_HLT*sf_diLepton*sf_diBJet * ((diLepton_isOS && diLepton_Mll && diLepton_HLT) ? 1 : 0)",
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
                "name": "bJet1_hadronFlavor",
                "variable": "jet_hadronFlavor[fwk_jed1Idx]",
                "type": "int16_t",
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
                "name": "bJet2_hadronFlavor",
                "variable": "jet_hadronFlavor[fwk_jed2Idx]",
                "type": "int16_t",
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
            # Top, Tbar, TTbar
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
                "variable": "std::abs(tt_gen_t_tbar_deltaPhi)"
            },
            # Top decay
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
                "name": "gen_Mbl_T_p4",
                "variable": "(tt_gen_lepton_t_beforeFSR >= 0 && tt_gen_b_beforeFSR >= 0 ) ? (tt_genParticles[tt_gen_lepton_t_beforeFSR].p4 + tt_genParticles[tt_gen_b_beforeFSR].p4).M() : -1",
            },
            {
                "name": "gen_DR_lepton_b",
                "variable": "(tt_gen_b_beforeFSR >= 0 && tt_gen_lepton_t_beforeFSR >=0) ? ROOT::Math::VectorUtil::DeltaR(tt_genParticles[tt_gen_b_beforeFSR].p4, tt_genParticles[tt_gen_lepton_t_beforeFSR].p4) : -1",
            },
            # Tbar decay
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
                "name": "gen_Mbl_Tbar_p4",
                "variable": "(tt_gen_lepton_tbar_beforeFSR >= 0 && tt_gen_bbar_beforeFSR >= 0 ) ? (tt_genParticles[tt_gen_lepton_tbar_beforeFSR].p4 + tt_genParticles[tt_gen_bbar_beforeFSR].p4).M() : -1",
            },
            {
                "name": "gen_DR_lepton_bbar",
                "variable": "(tt_gen_bbar_beforeFSR >= 0 && tt_gen_lepton_tbar_beforeFSR >=0) ? ROOT::Math::VectorUtil::DeltaR(tt_genParticles[tt_gen_bbar_beforeFSR].p4, tt_genParticles[tt_gen_lepton_tbar_beforeFSR].p4) : -1",
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
                "name": "simpleRecoTop_valid",
                "variable": "tt_ttbar[leplepIDIsoBB][0].size() > 0",
                "type": "bool"
            },
            ## Full reco TTbar
            {
                "name": "recoTop_T_p4",
                "variable": "recoTTbar.nSols > 0 ? recoTTbar.t_p4 : myLorentzVector()",
                "type": "myLorentzVector"
            },
            {
                "name": "recoTop_Tbar_p4",
                "variable": "recoTTbar.nSols > 0 ? recoTTbar.tbar_p4 : myLorentzVector()",
                "type": "myLorentzVector"
            },
            {
                "name": "recoTop_TT_p4",
                "variable": "recoTTbar.nSols > 0 ? recoTTbar.ttbar_p4 : myLorentzVector()",
                "type": "myLorentzVector"
            },
            {
                "name": "recoTop_TT_DR",
                "variable": "recoTTbar.nSols > 0 ? ROOT::Math::VectorUtil::DeltaR(recoTTbar.t_p4, recoTTbar.tbar_p4) : -1",
            },
            {
                "name": "recoTop_TT_DEta",
                "variable": "recoTTbar.nSols > 0 ? TTAnalysis::DeltaEta(recoTTbar.t_p4, recoTTbar.tbar_p4) : -1",
            },
            {
                "name": "recoTop_TT_DPhi",
                "variable": "recoTTbar.nSols > 0 ? std::abs(ROOT::Math::VectorUtil::DeltaPhi(recoTTbar.t_p4, recoTTbar.tbar_p4)) : -1",
            },
            {
                "name": "recoTop_nSols",
                "variable": "recoTTbar.nSols",
            },
            {
                "name": "recoTop_weight",
                "variable": "recoTTbar.weight",
            },
            {
                "name": "recoTop_valid",
                "variable": "recoTop_valid",
                "type": "bool",
            },
            {
                "name": "recoTop_chosenOrdered",
                "variable": "chosenDiLepDiBJetsMet",
                "type": "uint16_t",
            },
        ],
    }


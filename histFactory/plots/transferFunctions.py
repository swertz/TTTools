import inspect
import os
import sys

# Get directory where script is stored to handle the import correctly
scriptDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(scriptDir)

from plotTools import *

## Lepton stuff

lep_t_matchingCuts = [
        'tt_gen_lepton_t_beforeFSR >= 0', 'tt_gen_matched_lepton_t >= 0', 
        'tt_gen_lepton_t_deltaR[ tt_gen_matched_lepton_t ] < 0.3',
        ('tt_gen_matched_lepton_t == tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.first || '
        'tt_gen_matched_lepton_t == tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.second'),
    ]
lep_tbar_matchingCuts = [
        'tt_gen_lepton_tbar_beforeFSR >= 0', 'tt_gen_matched_lepton_tbar >= 0', 
        'tt_gen_lepton_tbar_deltaR[ tt_gen_matched_lepton_tbar ] < 0.3',
        ('tt_gen_matched_lepton_tbar == tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.first || '
        'tt_gen_matched_lepton_tbar == tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.second'),
    ]

leptonTFs = [
        # Lepton energy ratios using matched leptons over whole eta range (caveat: after FSR!)
        {
            'name': 'EgenOverEreco_electron_t_CAT_#CAT_TITLE#',
            'variable': 'tt_genParticles[ tt_gen_lepton_t_beforeFSR ].p4.E() / tt_leptons[ tt_gen_matched_lepton_t ].p4.E()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#',
                'tt_leptons[ tt_gen_matched_lepton_t ].isEl',
                *lep_t_matchingCuts
                ),
            'binning': '(100, 0.8, 1.4)'
        },
        {
            'name': 'EgenOverEreco_electron_tbar_CAT_#CAT_TITLE#',
            'variable': 'tt_genParticles[ tt_gen_lepton_tbar_beforeFSR ].p4.E() / tt_leptons[ tt_gen_matched_lepton_tbar ].p4.E()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#',
                'tt_leptons[ tt_gen_matched_lepton_tbar ].isEl',
                *lep_tbar_matchingCuts
                ),
            'binning': '(100, 0.8, 1.4)'
        },
        {
            'name': 'EgenOverEreco_muon_t_CAT_#CAT_TITLE#',
            'variable': 'tt_genParticles[ tt_gen_lepton_t_beforeFSR ].p4.E() / tt_leptons[ tt_gen_matched_lepton_t ].p4.E()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#',
                'tt_leptons[ tt_gen_matched_lepton_t ].isMu',
                *lep_t_matchingCuts
                ),
            'binning': '(100, 0.8, 1.4)'
        },
        {
            'name': 'EgenOverEreco_muon_tbar_CAT_#CAT_TITLE#',
            'variable': 'tt_genParticles[ tt_gen_lepton_tbar_beforeFSR ].p4.E() / tt_leptons[ tt_gen_matched_lepton_tbar ].p4.E()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#',
                'tt_leptons[ tt_gen_matched_lepton_tbar ].isMu',
                *lep_tbar_matchingCuts
                ),
            'binning': '(100, 0.8, 1.4)'
        },
        
        # Correlation: Lepton energy ratios vs. generated energy using matched leptons over whole eta range (caveat: after FSR!)
        {
            'name': 'EgenOverEreco_vs_Egen_electron_t_CAT_#CAT_TITLE#',
            'variable': 'tt_genParticles[ tt_gen_lepton_t_beforeFSR ].p4.E() ::: tt_genParticles[ tt_gen_lepton_t_beforeFSR ].p4.E() / tt_leptons[ tt_gen_matched_lepton_t ].p4.E()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#',
                'tt_leptons[ tt_gen_matched_lepton_t ].isEl',
                *lep_t_matchingCuts
                ),
            'binning': '(50, 0, 500, 50, 0.8, 1.4)'
        },
        {
            'name': 'EgenOverEreco_vs_Egen_electron_tbar_CAT_#CAT_TITLE#',
            'variable': 'tt_genParticles[ tt_gen_lepton_tbar_beforeFSR ].p4.E() ::: tt_genParticles[ tt_gen_lepton_tbar_beforeFSR ].p4.E() / tt_leptons[ tt_gen_matched_lepton_tbar ].p4.E()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#',
                'tt_leptons[ tt_gen_matched_lepton_tbar ].isEl',
                *lep_tbar_matchingCuts
                ),
            'binning': '(50, 0, 500, 50, 0.8, 1.4)'
        },
        {
            'name': 'EgenOverEreco_vs_Egen_muon_t_CAT_#CAT_TITLE#',
            'variable': 'tt_genParticles[ tt_gen_lepton_t_beforeFSR ].p4.E() ::: tt_genParticles[ tt_gen_lepton_t_beforeFSR ].p4.E() / tt_leptons[ tt_gen_matched_lepton_t ].p4.E()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#',
                'tt_leptons[ tt_gen_matched_lepton_t ].isMu',
                *lep_t_matchingCuts
                ),
            'binning': '(50, 0, 500, 50, 0.8, 1.4)'
        },
        {
            'name': 'EgenOverEreco_vs_Egen_muon_tbar_CAT_#CAT_TITLE#',
            'variable': 'tt_genParticles[ tt_gen_lepton_tbar_beforeFSR ].p4.E() ::: tt_genParticles[ tt_gen_lepton_tbar_beforeFSR ].p4.E() / tt_leptons[ tt_gen_matched_lepton_tbar ].p4.E()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#',
                'tt_leptons[ tt_gen_matched_lepton_tbar ].isMu',
                *lep_tbar_matchingCuts
                ),
            'binning': '(50, 0, 500, 50, 0.8, 1.4)'
        },

        # Lepton angles using matched leptons over whole eta range (caveat: after FSR!)
        {
            'name': 'Angle_electron_t_CAT_#CAT_TITLE#',
            'variable': 'ROOT::Math::VectorUtil::Angle(tt_genParticles[ tt_gen_lepton_t_beforeFSR ].p4, tt_leptons[ tt_gen_matched_lepton_t ].p4)',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#',
                'tt_leptons[ tt_gen_matched_lepton_t ].isEl',
                *lep_t_matchingCuts
                ),
            'binning': '(50, 0, 0.005)'
        },
        {
            'name': 'Angle_electron_tbar_CAT_#CAT_TITLE#',
            'variable': 'ROOT::Math::VectorUtil::Angle(tt_genParticles[ tt_gen_lepton_tbar_beforeFSR ].p4, tt_leptons[ tt_gen_matched_lepton_tbar ].p4)',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#',
                'tt_leptons[ tt_gen_matched_lepton_tbar ].isEl',
                *lep_tbar_matchingCuts
                ),
            'binning': '(50, 0, 0.005)'
        },
        {
            'name': 'Angle_muon_t_CAT_#CAT_TITLE#',
            'variable': 'ROOT::Math::VectorUtil::Angle(tt_genParticles[ tt_gen_lepton_t_beforeFSR ].p4, tt_leptons[ tt_gen_matched_lepton_t ].p4)',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#',
                'tt_leptons[ tt_gen_matched_lepton_t ].isMu',
                *lep_t_matchingCuts
                ),
            'binning': '(50, 0, 0.005)'
        },
        {
            'name': 'Angle_muon_tbar_CAT_#CAT_TITLE#',
            'variable': 'ROOT::Math::VectorUtil::Angle(tt_genParticles[ tt_gen_lepton_tbar_beforeFSR ].p4, tt_leptons[ tt_gen_matched_lepton_tbar ].p4)',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#',
                'tt_leptons[ tt_gen_matched_lepton_tbar ].isMu',
                *lep_tbar_matchingCuts
                ),
            'binning': '(50, 0, 0.005)'
        },


    ]



## B-jet stuff

bjet_binningX = range(0, 200, 5) + range(200, 400, 20) + [400, 450, 500, 550, 600, 700, 800, 2000]
bjet_binningY = [-500, -400] + range(-300, -200, 50) + range(-200, -50, 10) + range(-50, 0, 5) + range(0, 50, 5) + range(50, 200, 10) + range(200, 300, 50) + [300, 400, 500]

bjet_BA_binningX = range(0, 200, 5) + range(200, 360, 20) + [360, 400, 1000] 
bjet_BA_binningY = range(-500, -200, 100) + range(-200, -100, 20) + range(-100, 0, 10) + range(0, 100, 10) + range(100, 200, 20) + range(200, 500, 100) + [500]

bjet_EC_binningX = range(0, 200, 10) + range(200, 500, 20) + [500, 550, 600, 800, 2000]
bjet_EC_binningY = range(-500, -200, 100) + range(-200, -50, 20) + range(-50, 0, 10) + range(0, 50, 10) + range(50, 200, 20) + range(200, 500, 100) + [500]

bjet_nBinsX = str(len(bjet_binningX)-1)
bjet_binningX = "{" + str(bjet_binningX).strip("[").strip("]") + "}"
bjet_nBinsY = str(len(bjet_binningY)-1)
bjet_binningY = "{" + str(bjet_binningY).strip("[").strip("]") + "}"

bjet_BA_nBinsX = str(len(bjet_BA_binningX)-1)
bjet_BA_binningX = "{" + str(bjet_BA_binningX).strip("[").strip("]") + "}"
bjet_BA_nBinsY = str(len(bjet_BA_binningY)-1)
bjet_BA_binningY = "{" + str(bjet_BA_binningY).strip("[").strip("]") + "}"

bjet_EC_nBinsX = str(len(bjet_EC_binningX)-1)
bjet_EC_binningX = "{" + str(bjet_EC_binningX).strip("[").strip("]") + "}"
bjet_EC_nBinsY = str(len(bjet_EC_binningY)-1)
bjet_EC_binningY = "{" + str(bjet_EC_binningY).strip("[").strip("]") + "}"

bMatchingCuts = [
                'tt_gen_b_beforeFSR >= 0',
                'tt_gen_matched_b_beforeFSR[#MIN_LEP_IDISO#] >= 0',
                
                ('( tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].jidxs.first == '
                    'tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_b_beforeFSR[#MIN_LEP_IDISO#] ] )'
                ' || '
                '( tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].jidxs.second == '
                    'tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_b_beforeFSR[#MIN_LEP_IDISO#] ] )'),
                
                'tt_gen_b_beforeFSR_deltaR[#MIN_LEP_IDISO#][ tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_b_beforeFSR[#MIN_LEP_IDISO#] ] ] < 0.5',
        ]
bbarMatchingCuts = [
                'tt_gen_bbar_beforeFSR >= 0',
                'tt_gen_matched_bbar_beforeFSR[#MIN_LEP_IDISO#] >= 0',

                ('( tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].jidxs.first == '
                    'tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_bbar_beforeFSR[#MIN_LEP_IDISO#] ] )'
                ' || '
                '( tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].jidxs.second == '
                    'tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_bbar_beforeFSR[#MIN_LEP_IDISO#] ] )'),
                
                'tt_gen_bbar_beforeFSR_deltaR[#MIN_LEP_IDISO#][ tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_bbar_beforeFSR[#MIN_LEP_IDISO#] ] ] < 0.5'
        ]

matchedBTFs = [
        # B-jet angles using matched b-quarks over whole eta range
        {
            'name': 'Angle_b_CAT_#CAT_TITLE#',
            'variable': 'ROOT::Math::VectorUtil::Angle(tt_genParticles[ tt_gen_b_beforeFSR ].p4, tt_selJets[ tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_b_beforeFSR[#MIN_LEP_IDISO#] ] ].p4)',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', *bMatchingCuts),
            'binning': '(100, 0, 0.2)'
        },
        {
            'name': 'Angle_bbar_CAT_#CAT_TITLE#',
            'variable': 'ROOT::Math::VectorUtil::Angle(tt_genParticles[ tt_gen_bbar_beforeFSR ].p4, tt_selJets[ tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_bbar_beforeFSR[#MIN_LEP_IDISO#] ] ].p4)',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', *bbarMatchingCuts),
            'binning': '(100, 0, 0.2)'
        },
        
        # Correlation: B-jet angles vs. generated energy using matched b-quarks over whole eta range
        {
            'name': 'Angle_b_vs_Egen_CAT_#CAT_TITLE#',
            'variable': 'tt_genParticles[ tt_gen_b_beforeFSR ].p4.E() ::: ROOT::Math::VectorUtil::Angle(tt_genParticles[ tt_gen_b_beforeFSR ].p4, tt_selJets[ tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_b_beforeFSR[#MIN_LEP_IDISO#] ] ].p4)',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', *bMatchingCuts),
            'binning': '(50, 0, 500, 50, 0, 0.2)'
        },
        {
            'name': 'Angle_bbar_vs_Egen_CAT_#CAT_TITLE#',
            'variable': 'tt_genParticles[ tt_gen_bbar_beforeFSR ].p4.E() ::: ROOT::Math::VectorUtil::Angle(tt_genParticles[ tt_gen_bbar_beforeFSR ].p4, tt_selJets[ tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_bbar_beforeFSR[#MIN_LEP_IDISO#] ] ].p4)',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', *bbarMatchingCuts),
            'binning': '(50, 0, 500, 50, 0, 0.2)'
        },
        
        # Correlation: B-jet angles vs. abs(eta) using matched b-quarks over whole eta range
        {
            'name': 'Angle_vs_Eta_b_CAT_#CAT_TITLE#',
            'variable': 'std::abs(tt_genParticles[ tt_gen_b_beforeFSR ].p4.Eta()) ::: ROOT::Math::VectorUtil::Angle(tt_genParticles[ tt_gen_b_beforeFSR ].p4, tt_selJets[ tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_b_beforeFSR[#MIN_LEP_IDISO#] ] ].p4)',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', *bMatchingCuts),
            'binning': '(50, 0, 2.5, 50, 0, 0.2)'
        },
        {
            'name': 'Angle_vs_Eta_bbar_CAT_#CAT_TITLE#',
            'variable': 'std::abs(tt_genParticles[ tt_gen_bbar_beforeFSR ].p4.Eta()) ::: ROOT::Math::VectorUtil::Angle(tt_genParticles[ tt_gen_bbar_beforeFSR ].p4, tt_selJets[ tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_bbar_beforeFSR[#MIN_LEP_IDISO#] ] ].p4)',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', *bbarMatchingCuts),
            'binning': '(50, 0, 2.5, 50, 0, 0.2)'
        },
        
        # B-jet energy ratios using matched b-quarks over whole eta range
        {
            'name': 'EgenOverEreco_b_CAT_#CAT_TITLE#',
            'variable': 'tt_genParticles[ tt_gen_b_beforeFSR ].p4.E() / tt_selJets[ tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_b_beforeFSR[#MIN_LEP_IDISO#] ] ].p4.E()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', *bMatchingCuts),
            'binning': '(100, 0, 3)'
        },
        {
            'name': 'EgenOverEreco_bbar_CAT_#CAT_TITLE#',
            'variable': 'tt_genParticles[ tt_gen_bbar_beforeFSR ].p4.E() / tt_selJets[ tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_bbar_beforeFSR[#MIN_LEP_IDISO#] ] ].p4.E()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', *bbarMatchingCuts),
            'binning': '(100, 0, 3)'
        },
        
        # Correlation: B-jet energy ratios vs. generated energy using matched b-quarks over whole eta range
        {
            'name': 'EgenOverEreco_vs_Egen_b_CAT_#CAT_TITLE#',
            'variable': 'tt_genParticles[ tt_gen_b_beforeFSR ].p4.E() ::: tt_genParticles[ tt_gen_b_beforeFSR ].p4.E() / tt_selJets[ tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_b_beforeFSR[#MIN_LEP_IDISO#] ] ].p4.E()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', *bMatchingCuts),
            'binning': '(50, 0, 500, 50, 0, 3)'
        },
        {
            'name': 'EgenOverEreco_vs_Egen_bbar_CAT_#CAT_TITLE#',
            'variable': 'tt_genParticles[ tt_gen_bbar_beforeFSR ].p4.E() ::: tt_genParticles[ tt_gen_bbar_beforeFSR ].p4.E() / tt_selJets[ tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_bbar_beforeFSR[#MIN_LEP_IDISO#] ] ].p4.E()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', *bbarMatchingCuts),
            'binning': '(50, 0, 500, 50, 0, 3)'
        },

        # B-jet transfer functions using matched b-quarks over whole eta range
        {
            'name': 'TF_b_E_CAT_#CAT_TITLE#',
            'variable': 'tt_genParticles[ tt_gen_b_beforeFSR ].p4.E() ::: tt_selJets[ tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_b_beforeFSR[#MIN_LEP_IDISO#] ] ].p4.E() - tt_genParticles[ tt_gen_b ].p4.E()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', *bMatchingCuts),
            'binning': '(' + bjet_nBinsX + ', ' + bjet_binningX + ', ' + bjet_nBinsY + ', ' + bjet_binningY + ')',
        },
        {
            'name': 'TF_bbar_E_CAT_#CAT_TITLE#',
            'variable': 'tt_genParticles[ tt_gen_bbar_beforeFSR ].p4.E() ::: tt_selJets[ tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_bbar_beforeFSR[#MIN_LEP_IDISO#] ] ].p4.E() - tt_genParticles[ tt_gen_bbar ].p4.E()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', *bbarMatchingCuts),
            'binning': '(' + bjet_nBinsX + ', ' + bjet_binningX + ', ' + bjet_nBinsY + ', ' + bjet_binningY + ')',
        },

        ## B-jet transfer functions using matched b-quarks in the barrel (|eta|<=1.3)
        #{
        #    'name': 'TF_BA_b_E_CAT_#CAT_TITLE#',
        #    'variable': 'tt_genParticles[ tt_gen_b_beforeFSR ].p4.E() ::: tt_selJets[ tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_b_beforeFSR[#MIN_LEP_IDISO#] ] ].p4.E() - tt_genParticles[ tt_gen_b ].p4.E()',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#',
        #        'abs(tt_selJets[ tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_b_beforeFSR[#MIN_LEP_IDISO#] ] ].p4.Eta())<=1.3',
        #        *bMatchingCuts,
        #        ),
        #    'binning': '(' + bjet_BA_nBinsX + ', ' + bjet_BA_binningX + ', ' + bjet_BA_nBinsY + ', ' + bjet_BA_binningY + ')',
        #},
        #{
        #    'name': 'TF_BA_bbar_E_CAT_#CAT_TITLE#',
        #    'variable': 'tt_genParticles[ tt_gen_bbar_beforeFSR ].p4.E() ::: tt_selJets[ tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_bbar_beforeFSR[#MIN_LEP_IDISO#] ] ].p4.E() - tt_genParticles[ tt_gen_bbar ].p4.E()',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#',
        #        'abs(tt_selJets[ tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_bbar_beforeFSR[#MIN_LEP_IDISO#] ] ].p4.Eta())<=1.3',
        #        *bbarMatchingCuts,
        #        ),
        #    'binning': '(' + bjet_BA_nBinsX + ', ' + bjet_BA_binningX + ', ' + bjet_BA_nBinsY + ', ' + bjet_BA_binningY + ')',
        #},

        ## B-jet transfer functions using matched b-quarks in the endcaps (|eta|>1.3)
        #{
        #    'name': 'TF_EC_b_E_CAT_#CAT_TITLE#',
        #    'variable': 'tt_genParticles[ tt_gen_b_beforeFSR ].p4.E() ::: tt_selJets[ tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_b_beforeFSR[#MIN_LEP_IDISO#] ] ].p4.E() - tt_genParticles[ tt_gen_b ].p4.E()',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#',
        #        'abs(tt_selJets[ tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_b_beforeFSR[#MIN_LEP_IDISO#] ] ].p4.Eta())>1.3',
        #        *bMatchingCuts,
        #        ),
        #    'binning': '(' + bjet_EC_nBinsX + ', ' + bjet_EC_binningX + ', ' + bjet_EC_nBinsY + ', ' + bjet_EC_binningY + ')',
        #},
        #{
        #    'name': 'TF_EC_bbar_E_CAT_#CAT_TITLE#',
        #    'variable': 'tt_genParticles[ tt_gen_bbar_beforeFSR ].p4.E() ::: tt_selJets[ tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_bbar_beforeFSR[#MIN_LEP_IDISO#] ] ].p4.E() - tt_genParticles[ tt_gen_bbar ].p4.E()',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#',
        #        'abs(tt_selJets[ tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_bbar_beforeFSR[#MIN_LEP_IDISO#] ] ].p4.Eta())>1.3',
        #        *bbarMatchingCuts,
        #        ),
        #    'binning': '(' + bjet_EC_nBinsX + ', ' + bjet_EC_binningX + ', ' + bjet_EC_nBinsY + ', ' + bjet_EC_binningY + ')',
        #},

        # DeltaR matching monitoring
        {
            'name': 'DR_b_CAT_#CAT_TITLE#',
            'variable': 'tt_gen_b_deltaR[#MIN_LEP_IDISO#][ tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_b[#MIN_LEP_IDISO#] ] ]',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', *bMatchingCuts).replace('0.3', '6').replace('_beforeFSR', ''), # replacement needed because of the DR<0.3 cut in the default cuts
            'binning': '(60, 0, 6)',
        },
        {
            'name': 'DR_b_vs_DRgen_CAT_#CAT_TITLE#',
            'variable': 'tt_gen_b_deltaR[#MIN_LEP_IDISO#][ tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_b[#MIN_LEP_IDISO#] ] ] ::: ROOT::Math::VectorUtil::DeltaR(tt_genParticles[ tt_gen_b ].p4, tt_genParticles[ tt_gen_bbar ].p4)',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'tt_gen_bbar>=0', *bMatchingCuts).replace('0.3', '6').replace('_beforeFSR', ''),
            'binning': '(60, 0, 6, 60, 0, 6)',
        },
        {
            'name': 'DR_bbar_CAT_#CAT_TITLE#',
            'variable': 'tt_gen_bbar_deltaR[#MIN_LEP_IDISO#][ tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_bbar[#MIN_LEP_IDISO#] ] ]',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', *bbarMatchingCuts).replace('0.3', '6').replace('_beforeFSR', ''),
            'binning': '(60, 0, 6)',
        },
        {
            'name': 'DR_bbar_vs_DRgen_CAT_#CAT_TITLE#',
            'variable': 'tt_gen_bbar_deltaR[#MIN_LEP_IDISO#][ tt_selJets_selID_DRCut[#MIN_LEP_IDISO#][ tt_gen_matched_bbar[#MIN_LEP_IDISO#] ] ] ::: ROOT::Math::VectorUtil::DeltaR(tt_genParticles[ tt_gen_b ].p4, tt_genParticles[ tt_gen_bbar ].p4)',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'tt_gen_b>=0', *bbarMatchingCuts).replace('0.3', '6').replace('_beforeFSR', ''),
            'binning': '(60, 0, 6, 60, 0, 6)',
        },

        # B selection monitoring: 1 if b-jets is matched to b from top decay, 0 otherwise
        {
            'name': 'Matched_b_CSVv2_CAT_#CAT_TITLE#',
            'variable': joinCuts(*bMatchingCuts) + ' ? 1 : 0', 
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#').replace('_beforeFSR', ''),
            'binning': '(2, 0, 2)',
        },
        {
            'name': 'Matched_bbar_CSVv2_CAT_#CAT_TITLE#',
            'variable': joinCuts(*bbarMatchingCuts) + ' ? 1 : 0', 
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#').replace('_beforeFSR', ''),
            'binning': '(2, 0, 2)',
        },
        # both b and bbar
        {
            'name': 'Matched_b_bbar_CSVv2_CAT_#CAT_TITLE#',
            'variable': joinCuts(*(bMatchingCuts + bbarMatchingCuts)) + ' ? 1 : 0', 
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#').replace('_beforeFSR', ''),
            'binning': '(2, 0, 2)',
        },
        # Also check using Pt-ordered b-jets
        {
            'name': 'Matched_b_Pt_CAT_#CAT_TITLE#',
            'variable': joinCuts(*bMatchingCuts).replace("CSVv2Ordered", "PtOrdered") + ' ? 1 : 0', 
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#').replace('_beforeFSR', ''), # JET_CAT_CUTS uses CSVv2-ordered b-jet pairs, but it only requires that there is a b-jet pair present, which is true or false independently of how they're ordered
            'binning': '(2, 0, 2)',
        },
        {
            'name': 'Matched_bbar_Pt_CAT_#CAT_TITLE#',
            'variable': joinCuts(*bbarMatchingCuts).replace("CSVv2Ordered", "PtOrdered") + ' ? 1 : 0', 
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#').replace('_beforeFSR', ''),
            'binning': '(2, 0, 2)',
        },
        # both b and bbar
        {
            'name': 'Matched_b_bbar_Pt_CAT_#CAT_TITLE#',
            'variable': joinCuts(*(bMatchingCuts + bbarMatchingCuts)).replace("CSVv2Ordered", "PtOrdered") + ' ? 1 : 0', 
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#').replace('_beforeFSR', ''),
            'binning': '(2, 0, 2)',
        },
        
        # B-tagging monitoring: 1 if b-jets is really a b-jet, 0 otherwise
        {
            'name': 'BTagging_first_CSVv2_CAT_#CAT_TITLE#',
            'variable': 'std::abs(jet_hadronFlavor[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].idxs.first ]) == 5 ? 1 : 0', 
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': '(2, 0, 2)',
        },
        {
            'name': 'BTagging_second_CSVv2_CAT_#CAT_TITLE#',
            'variable': 'std::abs(jet_hadronFlavor[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].idxs.second ]) == 5 ? 1 : 0', 
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': '(2, 0, 2)',
        },
        {
            'name': 'BTagging_both_CSVv2_CAT_#CAT_TITLE#',
            'variable': '(std::abs(jet_hadronFlavor[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].idxs.first ]) == 5 && std::abs(jet_hadronFlavor[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].idxs.second ]) == 5 ) ? 1 : 0', 
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': '(2, 0, 2)',
        },
        {
            'name': 'BTagging_first_Pt_CAT_#CAT_TITLE#',
            'variable': 'std::abs(jet_hadronFlavor[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_PtOrdered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].idxs.first ]) == 5 ? 1 : 0', 
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': '(2, 0, 2)',
        },
        {
            'name': 'BTagging_second_Pt_CAT_#CAT_TITLE#',
            'variable': 'std::abs(jet_hadronFlavor[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_PtOrdered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].idxs.second ]) == 5 ? 1 : 0', 
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': '(2, 0, 2)',
        },
        {
            'name': 'BTagging_both_Pt_CAT_#CAT_TITLE#',
            'variable': '(std::abs(jet_hadronFlavor[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_PtOrdered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].idxs.first ]) == 5 && std::abs(jet_hadronFlavor[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_PtOrdered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].idxs.second ] ) == 5 ) ? 1 : 0',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': '(2, 0, 2)',
        },
    ]



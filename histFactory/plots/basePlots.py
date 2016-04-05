import inspect
import os
import sys

# Get directory where script is stored to handle the import correctly
scriptDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(scriptDir)

from plotTools import *

# Define skeleton config for plots, with stringcards which will be replaced for each category

yields = [
        # Yields
        {
            'name': 'Yields_CAT_#CAT_TITLE#',
            'variable': '0',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (1, 0, 1)
        },
    ]

genInfo = [
        ## Gen plots
        # Inclusive
        {
            'name': 'gen_T_DRbl_vs_TT_M_CAT_All',
            'variable': 'ROOT::Math::VectorUtil::DeltaR(tt_genParticles[tt_gen_lepton_t_beforeFSR].p4, tt_genParticles[tt_gen_b_beforeFSR].p4) ::: tt_gen_ttbar_beforeFSR_p4.M()',
            'plot_cut': 'gen_isSignal',
            'binning': (100, 0, 6, 100, 250, 3000),
            'scale-factors': False,
        },
        {
            'name': 'gen_Tbar_DRbl_vs_TT_M_CAT_All',
            'variable': 'ROOT::Math::VectorUtil::DeltaR(tt_genParticles[tt_gen_lepton_tbar_beforeFSR].p4, tt_genParticles[tt_gen_bbar_beforeFSR].p4) ::: tt_gen_ttbar_beforeFSR_p4.M()',
            'plot_cut': 'gen_isSignal',
            'binning': (100, 0, 6, 100, 250, 3000),
            'scale-factors': False,
        },
        # Using the selection cuts
        {
            'name': 'gen_T_Pt_BeforeFSR_CAT_#CAT_TITLE#',
            'variable': 'tt_genParticles[tt_gen_t_beforeFSR].p4.Pt()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'gen_isSignal'),
            'binning': (100, 0, 600)
        },
        {
            'name': 'gen_T_Eta_BeforeFSR_CAT_#CAT_TITLE#',
            'variable': 'tt_genParticles[tt_gen_t_beforeFSR].p4.Eta()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'gen_isSignal'),
            'binning': (100, -5, 5)
        },
        {
            'name': 'gen_T_Rapidity_BeforeFSR_CAT_#CAT_TITLE#',
            'variable': 'tt_genParticles[tt_gen_t_beforeFSR].p4.Rapidity()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'gen_isSignal'),
            'binning': (100, -4, 4)
        },
        {
            'name': 'gen_T_DRbl_vs_TT_M_CAT_#CAT_TITLE#',
            'variable': 'ROOT::Math::VectorUtil::DeltaR(tt_genParticles[tt_gen_lepton_t_beforeFSR].p4, tt_genParticles[tt_gen_b_beforeFSR].p4) ::: tt_gen_ttbar_beforeFSR_p4.M()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'gen_isSignal'),
            'binning': (100, 0, 6, 100, 250, 3000)
        },
        {
            'name': 'gen_T_Mbl_CAT_#CAT_TITLE#',
            'variable': '(tt_genParticles[tt_gen_lepton_t_beforeFSR].p4 + tt_genParticles[tt_gen_b_beforeFSR].p4).M()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'gen_isSignal'),
            'binning': (200, 0, 180)
        },
        {
            'name': 'gen_T_MW_CAT_#CAT_TITLE#',
            'variable': '(tt_genParticles[tt_gen_lepton_t_beforeFSR].p4 + tt_genParticles[tt_gen_neutrino_t_beforeFSR].p4).M()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'gen_isSignal'),
            'binning': (200, 60, 100)
        },
        {
            'name': 'gen_Tbar_Pt_BeforeFSR_CAT_#CAT_TITLE#',
            'variable': 'tt_genParticles[tt_gen_tbar_beforeFSR].p4.Pt()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'gen_isSignal'),
            'binning': (100, 0, 600)
        },
        {
            'name': 'gen_Tbar_Eta_BeforeFSR_CAT_#CAT_TITLE#',
            'variable': 'tt_genParticles[tt_gen_tbar_beforeFSR].p4.Eta()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'gen_isSignal'),
            'binning': (100, -5, 5)
        },
        {
            'name': 'gen_Tbar_Rapidity_BeforeFSR_CAT_#CAT_TITLE#',
            'variable': 'tt_genParticles[tt_gen_tbar_beforeFSR].p4.Rapidity()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'gen_isSignal'),
            'binning': (100, -4, 4)
        },
        {
            'name': 'gen_Tbar_DRbl_vs_TT_M_CAT_#CAT_TITLE#',
            'variable': 'ROOT::Math::VectorUtil::DeltaR(tt_genParticles[tt_gen_lepton_tbar_beforeFSR].p4, tt_genParticles[tt_gen_bbar_beforeFSR].p4) ::: tt_gen_ttbar_beforeFSR_p4.M()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'gen_isSignal'),
            'binning': (100, 0, 6, 100, 250, 3000)
        },
        {
            'name': 'gen_Tbar_Mbl_CAT_#CAT_TITLE#',
            'variable': '(tt_genParticles[tt_gen_lepton_tbar_beforeFSR].p4 + tt_genParticles[tt_gen_bbar_beforeFSR].p4).M()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'gen_isSignal'),
            'binning': (200, 0, 180)
        },
        {
            'name': 'gen_Tbar_MW_CAT_#CAT_TITLE#',
            'variable': '(tt_genParticles[tt_gen_lepton_tbar_beforeFSR].p4 + tt_genParticles[tt_gen_neutrino_tbar_beforeFSR].p4).M()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'gen_isSignal'),
            'binning': (200, 60, 100)
        },
        {
            'name': 'gen_TT_M_BeforeFSR_CAT_#CAT_TITLE#',
            'variable': 'tt_gen_ttbar_beforeFSR_p4.M()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'gen_isSignal'),
            'binning': (100, 300, 3000)
        },
        {
            'name': 'gen_TT_Pt_BeforeFSR_CAT_#CAT_TITLE#',
            'variable': 'tt_gen_ttbar_beforeFSR_p4.Pt()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'gen_isSignal'),
            'binning': (100, 0, 1000)
        },
        {
            'name': 'gen_TT_Eta_BeforeFSR_CAT_#CAT_TITLE#',
            'variable': 'tt_gen_ttbar_beforeFSR_p4.Eta()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'gen_isSignal'),
            'binning': (100, -4, 4)
        },
        {
            'name': 'gen_TT_DEta_BeforeFSR_CAT_#CAT_TITLE#',
            'variable': 'std::abs(tt_gen_ttbar_beforeFSR_p4.Eta()-tt_gen_ttbar_beforeFSR_p4.Eta())',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'gen_isSignal'),
            'binning': (100, 0, 8)
        },
        {
            'name': 'gen_TT_Rapidity_BeforeFSR_CAT_#CAT_TITLE#',
            'variable': 'tt_gen_ttbar_beforeFSR_p4.Rapidity()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'gen_isSignal'),
            'binning': (100, -6, 6)
        },
        {
            'name': 'gen_TT_DeltaRapidity_BeforeFSR_CAT_#CAT_TITLE#',
            'variable': 'std::abs(tt_gen_ttbar_beforeFSR_p4.Rapidity()-tt_gen_ttbar_beforeFSR_p4.Rapidity())',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'gen_isSignal'),
            'binning': (100, 0, 4)
        },
        {
            'name': 'gen_TT_Mbl_vs_Mbl_CAT_#CAT_TITLE#',
            'variable': '(tt_genParticles[tt_gen_lepton_t_beforeFSR].p4 + tt_genParticles[tt_gen_b_beforeFSR].p4).M() ::: (tt_genParticles[tt_gen_lepton_tbar_beforeFSR].p4 + tt_genParticles[tt_gen_bbar_beforeFSR].p4).M()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'gen_isSignal'),
            'binning': (100, 0, 180, 100, 0, 180)
        },
        {
            'name': 'gen_T_Mbl_vs_TT_M_CAT_#CAT_TITLE#',
            'variable': 'tt_gen_ttbar_beforeFSR_p4.M() ::: (tt_genParticles[tt_gen_lepton_t_beforeFSR].p4 + tt_genParticles[tt_gen_b_beforeFSR].p4).M()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'gen_isSignal'),
            'binning': (100, 300, 2000, 100, 0, 180)
        },
        {
            'name': 'gen_Tbar_Mbl_vs_TT_M_CAT_#CAT_TITLE#',
            'variable': 'tt_gen_ttbar_beforeFSR_p4.M() ::: (tt_genParticles[tt_gen_lepton_tbar_beforeFSR].p4 + tt_genParticles[tt_gen_bbar_beforeFSR].p4).M()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'gen_isSignal'),
            'binning': (100, 300, 2000, 100, 0, 180)
        },
]

ll = [
        # Event/vertex infos
        {
            'name': 'nPV_CAT_#CAT_TITLE#',
            'variable': 'vertex_n',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (40, 0, 40)
        },
        #{
        #    'name': 'nPU_CAT_#CAT_TITLE#',
        #    'variable': 'event_npu',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (40, 0, 40)
        #},
        #{
        #    'name': 'HT_CAT_#CAT_TITLE#',
        #    'variable': 'event_ht',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (100, 0, 1200)
        #},

        ## nLeptons
        { 
            'name': 'nElectrons_CAT_#CAT_TITLE#',
            'variable': 'Length$(tt_electrons_IDIso[#EL_IDISO#])',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (5, 0, 5),
            'scale-factors': False
        },
        { 
            'name': 'nMuons_CAT_#CAT_TITLE#',
            'variable': 'Length$(tt_muons_IDIso[#MU_IDISO#])',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (5, 0, 5),
            'scale-factors': False
        },

        ## Lepton 1
        { 
            'name': 'lep1_pt_CAT_#CAT_TITLE#',
            'variable': 'tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.first ].p4.Pt()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, 20, 320)
        },
        { 
            'name': 'lep1_eta_CAT_#CAT_TITLE#',
            'variable': 'tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.first ].p4.Eta()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, -2.5, 2.5)
        },
        #{ 
        #    'name': 'lep1_phi_CAT_#CAT_TITLE#',
        #    'variable': 'tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.first ].p4.Phi()',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, -3.14159, 3.14159)
        #},
        { 
            'name': 'lep1_iso_CAT_#CAT_TITLE#',
            'variable': 'tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.first ].isoValue',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, 0, 0.15)
        },
        { 
            'name': 'lep1_dz_CAT_#CAT_TITLE#',
            'variable': ( 'tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.first ].isEl ? '
                            'electron_dz[ tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.first ].idx ] : '
                            'muon_dz[ tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.first ].idx ]' ),
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, -0.1, 0.1)
        },
        { 
            'name': 'lep1_dxy_CAT_#CAT_TITLE#',
            'variable': ( 'tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.first ].isEl ? '
                            'electron_dxy[ tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.first ].idx ] : '
                            'muon_dxy[ tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.first ].idx ]' ),
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, -0.1, 0.1)
        },
        { 
            'name': 'lep1_dca_CAT_#CAT_TITLE#',
            'variable': ( 'tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.first ].isEl ? '
                            'electron_dca[ tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.first ].idx ] : '
                            'muon_dca[ tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.first ].idx ]' ),
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, -10, 10)
        },
        { 
            'name': 'lep1_SF_CAT_#CAT_TITLE#',
            'variable': '#LEP1_SF#',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, 0.9, 1.1),
            'scale-factors': False
        },
        
        # Lepton 2
        { 
            'name': 'lep2_pt_CAT_#CAT_TITLE#',
            'variable': 'tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.second ].p4.Pt()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, 20, 320)
        },
        { 
            'name': 'lep2_eta_CAT_#CAT_TITLE#',
            'variable': 'tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.second ].p4.Eta()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, -2.5, 2.5)
        },
        #{ 
        #    #'name': 'lep2_phi_CAT_#CAT_TITLE#',
        #    #'variable': 'tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.second ].p4.Phi()',
        #    #'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    #'binning': (50, -3.14159, 3.14159)
        #},
        { 
            'name': 'lep2_iso_CAT_#CAT_TITLE#',
            'variable': 'tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.second ].isoValue',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, 0, 0.2)
        },
        { 
            'name': 'lep2_dz_CAT_#CAT_TITLE#',
            'variable': ( 'tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.second ].isEl ? '
                            'electron_dz[ tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.second ].idx ] : '
                            'muon_dz[ tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.second ].idx ]' ),
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, -0.1, 0.1)
        },
        { 
            'name': 'lep2_dxy_CAT_#CAT_TITLE#',
            'variable': ( 'tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.second ].isEl ? '
                            'electron_dxy[ tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.second ].idx ] : '
                            'muon_dxy[ tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.second ].idx ]' ),
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, -0.1, 0.1)
        },
        { 
            'name': 'lep2_dca_CAT_#CAT_TITLE#',
            'variable': ( 'tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.second ].isEl ? '
                            'electron_dca[ tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.second ].idx ] : '
                            'muon_dca[ tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.second ].idx ]' ),
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, -10, 10)
        },
        { 
            'name': 'lep2_SF_CAT_#CAT_TITLE#',
            'variable': '#LEP2_SF#',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, 0.9, 1.1),
            'scale-factors': False
        },
        
        # DiLepton
        { 
            'name': 'll_M_CAT_#CAT_TITLE#',
            'variable': 'tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].p4.M()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, 0, 400)
        },
        { 
            'name': 'll_M_Zpeak_CAT_#CAT_TITLE#',
            'variable': 'tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].p4.M()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, 70, 110)
        },
        { 
            'name': 'll_Pt_CAT_#CAT_TITLE#',
            'variable': 'tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].p4.Pt()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, 0, 300)
        },
        { 
            'name': 'll_Eta_CAT_#CAT_TITLE#',
            'variable': 'tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].p4.Eta()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, -5, 5)
        },
        #{ 
        #    'name': 'll_Phi_CAT_#CAT_TITLE#',
        #    'variable': 'tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].p4.Phi()',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, -3.14159, 3.14159)
        #},
        { 
            'name': 'll_DR_CAT_#CAT_TITLE#',
            'variable': 'tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].DR',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, 0, 6)
        },
        #{ 
        #    'name': 'll_DEta_CAT_#CAT_TITLE#',
        #    'variable': 'tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].DEta',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, 0, 5)
        #},
        #{ 
        #    'name': 'll_DPhi_CAT_#CAT_TITLE#',
        #    'variable': 'abs(tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].DPhi)',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, 0, 3.14159)
        #},
        
        # number of jets: also valid for categories with < 2 jets => put in here
        {
            'name': 'nJets_CAT_#CAT_TITLE#',
            'variable': 'Length$(tt_selJets_selID_DRCut[#MIN_LEP_IDISO#])',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (10, 0, 10)
        },
       
        # MissingET: same thing
        {
            'name': 'PFMET_MET_CAT_#CAT_TITLE#',
            'variable': 'met_p4.Pt()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, 0, 250)
        },
        {
            'name': 'PFFMET_Phi_CAT_#CAT_TITLE#',
            'variable': 'met_p4.Phi()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, -3.14159, 3.14159)
        },
    ]

# Jet-related plots (also dependent on lepton infos because of the minDRjl cut)
lljj = [
        # Jet 1
        { 
            'name': 'jet1_pt_CAT_#CAT_TITLE#',
            'variable': 'tt_selJets[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].diJetIdx ].jidxs.first ].p4.Pt()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (50, 30, 380)
        },
        { 
            'name': 'jet1_eta_CAT_#CAT_TITLE#',
            'variable': 'tt_selJets[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].diJetIdx ].jidxs.first ].p4.Eta()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, -2.5, 2.5)
        },
        #{ 
        #    'name': 'jet1_phi_CAT_#CAT_TITLE#',
        #    'variable': 'tt_selJets[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].diJetIdx ].jidxs.first ].p4.Phi()',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, -3.14159, 3.14159)
        #},
        { 
            'name': 'jet1_minDRjl_CAT_#CAT_TITLE#',
            'variable': 'tt_selJets[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].diJetIdx ].jidxs.first ].minDRjl_lepIDIso[#MIN_LEP_IDISO#]',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, 0, 6)
        },
        { 
            'name': 'jet1_CSVv2_CAT_#CAT_TITLE#',
            'variable': 'tt_selJets[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].diJetIdx ].jidxs.first ].CSVv2',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (50, 0, 1)
        },
        
        # Jet 2
        { 
            'name': 'jet2_pt_CAT_#CAT_TITLE#',
            'variable': 'tt_selJets[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].diJetIdx ].jidxs.second ].p4.Pt()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (50, 30, 380)
        },
        { 
            'name': 'jet2_eta_CAT_#CAT_TITLE#',
            'variable': 'tt_selJets[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].diJetIdx ].jidxs.second ].p4.Eta()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, -2.5, 2.5)
        },
        #{ 
        #    'name': 'jet2_phi_CAT_#CAT_TITLE#',
        #    'variable': 'tt_selJets[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].diJetIdx ].jidxs.second ].p4.Phi()',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, -3.14159, 3.14159)
        #},
        { 
            'name': 'jet2_minDRjl_CAT_#CAT_TITLE#',
            'variable': 'tt_selJets[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].diJetIdx ].jidxs.second ].minDRjl_lepIDIso[#MIN_LEP_IDISO#]',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, 0, 6)
        },
        { 
            'name': 'jet2_CSVv2_CAT_#CAT_TITLE#',
            'variable': 'tt_selJets[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].diJetIdx ].jidxs.second ].CSVv2',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (50, 0, 1)
        },

        # DiJet
        { 
            'name': 'jj_M_CAT_#CAT_TITLE#',
            'variable': 'tt_diJets[ tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].diJetIdx ].p4.M()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, 0, 800)
        },
        { 
            'name': 'jj_Pt_CAT_#CAT_TITLE#',
            'variable': 'tt_diJets[ tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].diJetIdx ].p4.Pt()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, 0, 500)
        },
        { 
            'name': 'jj_Eta_CAT_#CAT_TITLE#',
            'variable': 'tt_diJets[ tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].diJetIdx ].p4.Eta()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, -5, 5)
        },
        #{ 
        #    'name': 'jj_Phi_CAT_#CAT_TITLE#',
        #    'variable': 'tt_diJets[ tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].diJetIdx ].p4.Phi()',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, -3.14159, 3.14159)
        #},
        { 
            'name': 'jj_DR_CAT_#CAT_TITLE#',
            'variable': 'tt_diJets[ tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].diJetIdx ].DR',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, 0, 6)
        },
        #{ 
        #    'name': 'jj_DEta_CAT_#CAT_TITLE#',
        #    'variable': 'tt_diJets[ tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].diJetIdx ].DEta',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, 0, 10)
        #},
        #{ 
        #    'name': 'jj_DPhi_CAT_#CAT_TITLE#',
        #    'variable': 'abs(tt_diJets[ tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].diJetIdx ].DPhi)',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, 0, 3.14159)
        #},
        
        # DiLepDiJet
        { 
            'name': 'lljj_M_CAT_#CAT_TITLE#',
            'variable': 'tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].p4.M()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, 100, 2000)
        },
        { 
            'name': 'lljj_Pt_CAT_#CAT_TITLE#',
            'variable': 'tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].p4.Pt()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, 0, 500)
        },
        { 
            'name': 'lljj_Eta_CAT_#CAT_TITLE#',
            'variable': 'tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].p4.Eta()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, -5, 5)
        },
        #{ 
        #    'name': 'lljj_Phi_CAT_#CAT_TITLE#',
        #    'variable': 'tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].p4.Phi()',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, -3.14159, 3.14159)
        #},
        { 
            'name': 'lljj_DR_ll_jj_CAT_#CAT_TITLE#',
            'variable': 'tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].DR_ll_jj',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, 0, 6)
        },
        #{ 
        #    'name': 'lljj_DEta_ll_jj_CAT_#CAT_TITLE#',
        #    'variable': 'tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].DEta_ll_jj',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, 0, 10)
        #},
        #{ 
        #    'name': 'lljj_DPhi_ll_jj_CAT_#CAT_TITLE#',
        #    'variable': 'abs(tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].DPhi_ll_jj)',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, 0, 3.14159)
        #},
        { 
            'name': 'lljj_minDRjl_CAT_#CAT_TITLE#',
            'variable': 'tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].minDRjl',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, 0, 6)
        },
        { 
            'name': 'lljj_maxDRjl_CAT_#CAT_TITLE#',
            'variable': 'tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].maxDRjl',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, 0, 6)
        },
        #{ 
        #    'name': 'lljj_minDEtajl_CAT_#CAT_TITLE#',
        #    'variable': 'tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].minDEtajl',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, 0, 5)
        #},
        #{ 
        #    'name': 'lljj_maxDEtajl_CAT_#CAT_TITLE#',
        #    'variable': 'tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].maxDEtajl',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, 0, 5)
        #},
        #{ 
        #    'name': 'lljj_minDPhijl_CAT_#CAT_TITLE#',
        #    'variable': 'abs(tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].minDPhijl)',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, 0, 3.14159)
        #},
        #{ 
        #    'name': 'lljj_maxDPhijl_CAT_#CAT_TITLE#',
        #    'variable': 'abs(tt_diLepDiJets[ tt_diLepDiJets_DRCut[#LEPLEP_IDISO#][0] ].maxDPhijl)',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, 0, 3.14159)
        #},
        
        # DiLepDiJetMET
        { 
            'name': 'lljjMet_Pt_CAT_#CAT_TITLE#',
            'variable': 'tt_diLepDiJetsMet[ tt_diLepDiJetsMet_DRCut[#LEPLEP_IDISO#][0] ].p4.Pt()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, 0, 400)
        },
        #{ 
        #    'name': 'lljjMet_Phi_CAT_#CAT_TITLE#',
        #    'variable': 'tt_diLepDiJetsMet[ tt_diLepDiJetsMet_DRCut[#LEPLEP_IDISO#][0] ].p4.Phi()',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, -3.14159, 3.14159)
        #},
        { 
            'name': 'lljjMet_Mt_CAT_#CAT_TITLE#',
            'variable': 'tt_diLepDiJetsMet[ tt_diLepDiJetsMet_DRCut[#LEPLEP_IDISO#][0] ].p4.Mt()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, 100, 2000)
        },
        #{ 
        #    'name': 'lljjMet_DPhi_ll_Met_CAT_#CAT_TITLE#',
        #    'variable': 'abs(tt_diLepDiJetsMet[ tt_diLepDiJetsMet_DRCut[#LEPLEP_IDISO#][0] ].DPhi_ll_Met)',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, 0, 3.14159)
        #},
        #{ 
        #    'name': 'lljjMet_DPhi_jj_Met_CAT_#CAT_TITLE#',
        #    'variable': 'abs(tt_diLepDiJetsMet[ tt_diLepDiJetsMet_DRCut[#LEPLEP_IDISO#][0] ].DPhi_jj_Met)',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, 0, 3.14159)
        #},
        #{ 
        #    'name': 'lljjMet_DPhi_lljj_Met_CAT_#CAT_TITLE#',
        #    'variable': 'abs(tt_diLepDiJetsMet[ tt_diLepDiJetsMet_DRCut[#LEPLEP_IDISO#][0] ].DPhi_lljj_Met)',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, 0, 3.14159)
        #},
        #{ 
        #    'name': 'lljjMet_minDPhi_l_Met_CAT_#CAT_TITLE#',
        #    'variable': 'abs(tt_diLepDiJetsMet[ tt_diLepDiJetsMet_DRCut[#LEPLEP_IDISO#][0] ].minDPhi_l_Met)',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, 0, 3.14159)
        #},
        #{ 
        #    'name': 'lljjMet_maxDPhi_l_Met_CAT_#CAT_TITLE#',
        #    'variable': 'abs(tt_diLepDiJetsMet[ tt_diLepDiJetsMet_DRCut[#LEPLEP_IDISO#][0] ].maxDPhi_l_Met)',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, 0, 3.14159)
        #},
        #{ 
        #    'name': 'lljjMet_minDPhi_j_Met_CAT_#CAT_TITLE#',
        #    'variable': 'abs(tt_diLepDiJetsMet[ tt_diLepDiJetsMet_DRCut[#LEPLEP_IDISO#][0] ].minDPhi_j_Met)',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, 0, 3.14159)
        #},
        #{ 
        #    'name': 'lljjMet_maxDPhi_j_Met_CAT_#CAT_TITLE#',
        #    'variable': 'abs(tt_diLepDiJetsMet[ tt_diLepDiJetsMet_DRCut[#LEPLEP_IDISO#][0] ].maxDPhi_j_Met)',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, 0, 3.14159)
        #},
        
    ]

# BJet-related plots (also dependent on lepton infos because of the minDRjl cut)
# For now, take CSVv2-chosen di-bjets
# Only require two jets but iterate over one b-tag working point
lljj_b = [
        # number of b-jets
        { 
            'name': 'nBJets_#BWP#_CAT_#CAT_TITLE#',
            'variable': 'Length$(tt_selBJets_DRCut_BWP_CSVv2Ordered[#MIN_LEP_IDISO_BWP#])',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (6, 0, 6)
        },
    ]

# BJet-related plots (also dependent on lepton infos because of the minDRjl cut)
# For now, take CSVv2-chosen di-bjets
# Require two jets and one b-jet; iterate over one b-tag working point
llbj = [ ]

# (ll)bb(Met)-related plots
# For now, take CSVv2-chosen di-bjets
# Require two jets and loop over two b-tag working points
llbb = [
        # BJet 1
        { 
            'name': 'bjet1_pt_CAT_#CAT_TITLE#',
            'variable': 'tt_selJets[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].jidxs.first ].p4.Pt()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, 30, 450)
        },
        { 
            'name': 'bjet1_eta_CAT_#CAT_TITLE#',
            'variable': 'tt_selJets[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].jidxs.first ].p4.Eta()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, -2.5, 2.5)
        },
        #{ 
        #    'name': 'bjet1_phi_CAT_#CAT_TITLE#',
        #    'variable': 'tt_selJets[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].jidxs.first ].p4.Phi()',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (25, -3.14159, 3.14159)
        #},
        { 
            'name': 'bjet1_minDRjl_CAT_#CAT_TITLE#',
            'variable': 'tt_selJets[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].jidxs.first ].minDRjl_lepIDIso[#MIN_LEP_IDISO#]',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, 0, 6)
        },
        { 
            'name': 'bjet1_CSVv2_CAT_#CAT_TITLE#',
            'variable': 'tt_selJets[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].jidxs.first ].CSVv2',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, 0.4, 1)
        },
        { 
            'name': 'bjet1_SF_CAT_#CAT_TITLE#',
            'variable': '#BJET1_SF#',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (50, 0.9, 1.5),
            'scale-factors': False
        },
        
        # BJet 2
        { 
            'name': 'bjet2_pt_CAT_#CAT_TITLE#',
            'variable': 'tt_selJets[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].jidxs.second ].p4.Pt()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, 30, 250)
        },
        { 
            'name': 'bjet2_eta_CAT_#CAT_TITLE#',
            'variable': 'tt_selJets[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].jidxs.second ].p4.Eta()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, -2.5, 2.5)
        },
        #{ 
        #    'name': 'bjet2_phi_CAT_#CAT_TITLE#',
        #    'variable': 'tt_selJets[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].jidxs.second ].p4.Phi()',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (25, -3.14159, 3.14159)
        #},
        { 
            'name': 'bjet2_minDRjl_CAT_#CAT_TITLE#',
            'variable': 'tt_selJets[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].jidxs.second ].minDRjl_lepIDIso[#MIN_LEP_IDISO#]',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, 0, 6)
        },
        { 
            'name': 'bjet2_CSVv2_CAT_#CAT_TITLE#',
            'variable': 'tt_selJets[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].jidxs.second ].CSVv2',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, 0.4, 1)
        },
        { 
            'name': 'bjet2_SF_CAT_#CAT_TITLE#',
            'variable': '#BJET2_SF#',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (50, 0.9, 1.5),
            'scale-factors': False
        },
        
        # DiBJet
        { 
            'name': 'bb_M_CAT_#CAT_TITLE#',
            'variable': 'tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].p4.M()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (25, 0, 1000)
        },
        { 
            'name': 'bb_Pt_CAT_#CAT_TITLE#',
            'variable': 'tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].p4.Pt()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, 0, 500)
        },
        { 
            'name': 'bb_Eta_CAT_#CAT_TITLE#',
            'variable': 'tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].p4.Eta()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, -5, 5)
        },
        #{ 
        #    'name': 'bb_Phi_CAT_#CAT_TITLE#',
        #    'variable': 'tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].p4.Phi()',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (25, -3.14159, 3.14159)
        #},
        { 
            'name': 'bb_DR_CAT_#CAT_TITLE#',
            'variable': 'tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].DR',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, 0, 6)
        },
        #{ 
        #    'name': 'bb_DEta_CAT_#CAT_TITLE#',
        #    'variable': 'tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].DEta',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (25, 0, 10)
        #},
        #{ 
        #    'name': 'bb_DPhi_CAT_#CAT_TITLE#',
        #    'variable': 'abs(tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].DPhi)',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (25, 0, 3.14159)
        #},

        # DiLepDiBJet
        { 
            'name': 'llbb_M_CAT_#CAT_TITLE#',
            'variable': 'tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].p4.M()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, 100, 2000)
        },
        { 
            'name': 'llbb_Pt_CAT_#CAT_TITLE#',
            'variable': 'tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].p4.Pt()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, 0, 500)
        },
        { 
            'name': 'llbb_Eta_CAT_#CAT_TITLE#',
            'variable': 'tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].p4.Eta()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, -5, 5)
        },
        #{ 
        #    'name': 'llbb_Phi_CAT_#CAT_TITLE#',
        #    'variable': 'tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].p4.Phi()',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (25, -3.14159, 3.14159)
        #},
        { 
            'name': 'llbb_DR_ll_bb_CAT_#CAT_TITLE#',
            'variable': 'tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].DR_ll_jj',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, 0, 6)
        },
        #{ 
        #    'name': 'llbb_DEta_ll_bb_CAT_#CAT_TITLE#',
        #    'variable': 'tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].DEta_ll_jj',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (25, 0, 10)
        #},
        #{ 
        #    'name': 'llbb_DPhi_ll_bb_CAT_#CAT_TITLE#',
        #    'variable': 'abs(tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].DPhi_ll_jj)',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (25, 0, 3.14159)
        #},
        { 
            'name': 'llbb_minDRjl_CAT_#CAT_TITLE#',
            'variable': 'tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].minDRjl',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, 0, 6)
        },
        { 
            'name': 'llbb_maxDRjl_CAT_#CAT_TITLE#',
            'variable': 'tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].maxDRjl',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, 0, 6)
        },
        #{ 
        #    'name': 'llbb_minDEtajl_CAT_#CAT_TITLE#',
        #    'variable': 'tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].minDEtajl',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (25, 0, 5)
        #},
        #{ 
        #    'name': 'llbb_maxDEtajl_CAT_#CAT_TITLE#',
        #    'variable': 'tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].maxDEtajl',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (25, 0, 5)
        #},
        #{ 
        #    'name': 'llbb_minDPhijl_CAT_#CAT_TITLE#',
        #    'variable': 'abs(tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].minDPhijl)',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (25, 0, 3.14159)
        #},
        #{ 
        #    'name': 'llbb_maxDPhijl_CAT_#CAT_TITLE#',
        #    'variable': 'abs(tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].maxDPhijl)',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (25, 0, 3.14159)
        #},
        
        # DiLepDiBJetMET
        { 
            'name': 'llbbMet_Pt_CAT_#CAT_TITLE#',
            'variable': 'tt_diLepDiJetsMet[ tt_diLepDiBJetsMet_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].p4.Pt()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, 0, 800)
        },
        #{ 
        #    'name': 'llbbMet_Phi_CAT_#CAT_TITLE#',
        #    'variable': 'tt_diLepDiJetsMet[ tt_diLepDiBJetsMet_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].p4.Phi()',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, -3.14159, 3.14159)
        #},
        { 
            'name': 'llbbMet_Mt_CAT_#CAT_TITLE#',
            'variable': 'tt_diLepDiJetsMet[ tt_diLepDiBJetsMet_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].p4.Mt()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, 150, 2000)
        },
        #{ 
        #    'name': 'llbbMet_DPhi_ll_Met_CAT_#CAT_TITLE#',
        #    'variable': 'abs(tt_diLepDiJetsMet[ tt_diLepDiBJetsMet_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].DPhi_ll_Met)',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, 0, 3.14159)
        #},
        #{ 
        #    'name': 'llbbMet_DPhi_bb_Met_CAT_#CAT_TITLE#',
        #    'variable': 'abs(tt_diLepDiJetsMet[ tt_diLepDiBJetsMet_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].DPhi_jj_Met)',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, 0, 3.14159)
        #},
        #{ 
        #    'name': 'llbbMet_DPhi_llbb_Met_CAT_#CAT_TITLE#',
        #    'variable': 'abs(tt_diLepDiJetsMet[ tt_diLepDiBJetsMet_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].DPhi_lljj_Met)',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, 0, 3.14159)
        #},
        #{ 
        #    'name': 'llbbMet_minDPhi_l_Met_CAT_#CAT_TITLE#',
        #    'variable': 'abs(tt_diLepDiJetsMet[ tt_diLepDiBJetsMet_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].minDPhi_l_Met)',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, 0, 3.14159)
        #},
        #{ 
        #    'name': 'llbbMet_maxDPhi_l_Met_CAT_#CAT_TITLE#',
        #    'variable': 'abs(tt_diLepDiJetsMet[ tt_diLepDiBJetsMet_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].maxDPhi_l_Met)',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, 0, 3.14159)
        #},
        #{ 
        #    'name': 'llbbMet_minDPhi_j_Met_CAT_#CAT_TITLE#',
        #    'variable': 'abs(tt_diLepDiJetsMet[ tt_diLepDiBJetsMet_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].minDPhi_j_Met)',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, 0, 3.14159)
        #},
        #{ 
        #    'name': 'llbbMet_maxDPhi_j_Met_CAT_#CAT_TITLE#',
        #    'variable': 'abs(tt_diLepDiJetsMet[ tt_diLepDiBJetsMet_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].maxDPhi_j_Met)',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
        #    'binning': (50, 0, 3.14159)
        #},
]

llbb_recoTop = [
        ## TT reconstruction without smearing
        { 
            'name': 'llbbMet_TT_M_CAT_#CAT_TITLE#',
            'variable': 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0][0].p4.M()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0].size() > 0'),
            'binning': (20, 250, 2500)
        },
        { 
            'name': 'llbbMet_TT_Pt_CAT_#CAT_TITLE#',
            'variable': 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0][0].p4.Pt()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0].size() > 0'),
            'binning': (20, 0, 500)
        },
        { 
            'name': 'llbbMet_TT_Eta_CAT_#CAT_TITLE#',
            'variable': 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0][0].p4.Eta()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0].size() > 0'),
            'binning': (20, -5, 5)
        },
        { 
            'name': 'llbbMet_TT_Rapidity_CAT_#CAT_TITLE#',
            'variable': 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0][0].p4.Rapidity()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0].size() > 0'),
            'binning': (20, -3, 3)
        },
        # Top 1
        { 
            'name': 'llbbMet_T1_Pt_CAT_#CAT_TITLE#',
            'variable': 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0][0].top1_p4.Pt()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0].size() > 0'),
            'binning': (20, 0, 500)
        },
        { 
            'name': 'llbbMet_T1_Eta_CAT_#CAT_TITLE#',
            'variable': 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0][0].top1_p4.Eta()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0].size() > 0'),
            'binning': (20, -5, 5)
        },
        { 
            'name': 'llbbMet_T1_Rapidity_CAT_#CAT_TITLE#',
            'variable': 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0][0].top1_p4.Rapidity()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0].size() > 0'),
            'binning': (20, -3, 3)
        },
        # Top 2
        { 
            'name': 'llbbMet_T2_Pt_CAT_#CAT_TITLE#',
            'variable': 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0][0].top2_p4.Pt()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0].size() > 0'),
            'binning': (20, 0, 500)
        },
        { 
            'name': 'llbbMet_T2_Eta_CAT_#CAT_TITLE#',
            'variable': 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0][0].top2_p4.Eta()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0].size() > 0'),
            'binning': (20, -5, 5)
        },
        { 
            'name': 'llbbMet_T2_Rapidity_CAT_#CAT_TITLE#',
            'variable': 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0][0].top2_p4.Rapidity()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0].size() > 0'),
            'binning': (20, -3, 3)
        },
        #{ 
        #    'name': 'llbbMet_DPhi_top1_top2_CAT_#CAT_TITLE#',
        #    'variable': 'abs( tt_ttbar[#LEPLEP_IDISO_BBWP#][0][0].DPhi_tt )',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0].size() > 0'),
        #    'binning': (50, 0, 3.14159)
        #},
        { 
            'name': 'llbbMet_DR_top1_top2_CAT_#CAT_TITLE#',
            'variable': 'abs( tt_ttbar[#LEPLEP_IDISO_BBWP#][0][0].DR_tt )',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0].size() > 0'),
            'binning': (20, 0, 6)
        },
        #{ 
        #    'name': 'llbbMet_DEta_top1_top2_CAT_#CAT_TITLE#',
        #    'variable': 'abs( tt_ttbar[#LEPLEP_IDISO_BBWP#][0][0].DEta_tt )',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0].size() > 0'),
        #    'binning': (50, 0, 6)
        #},
        ## Resolution
        { 
            'name': 'llbbMet_TT_M_resolution_beforeFSR_CAT_#CAT_TITLE#',
            'variable': '(tt_ttbar[#LEPLEP_IDISO_BBWP#][0][0].p4.M() - tt_gen_ttbar_beforeFSR_p4.M()) / tt_gen_ttbar_beforeFSR_p4.M() ' ,
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0].size() > 0', 'tt_gen_ttbar_decay_type > 0'),
            'binning': (100, -2, 4)
        },
        { 
            'name': 'llbbMet_TT_M_minus_Mgen_beforeFSR_CAT_#CAT_TITLE#',
            'variable': 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0][0].p4.M() - tt_gen_ttbar_beforeFSR_p4.M()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0].size() > 0', 'tt_gen_ttbar_decay_type > 0'),
            'binning': (100, -1000, 1000)
        },
        { 
            'name': 'llbbMet_TT_M_minus_Mgen_vs_Mgen_beforeFSR_CAT_#CAT_TITLE#',
            'variable': 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0][0].p4.M() - tt_gen_ttbar_beforeFSR_p4.M() ::: tt_gen_ttbar_beforeFSR_p4.M()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0].size() > 0', 'tt_gen_ttbar_decay_type > 0'),
            'binning': (100, -1000, 1000, 100, 250, 2500)
        },
        { 
            'name': 'llbbMet_TT_M_Resolution_vs_Mgen_beforeFSR_CAT_#CAT_TITLE#',
            'variable': '(tt_ttbar[#LEPLEP_IDISO_BBWP#][0][0].p4.M() - tt_gen_ttbar_beforeFSR_p4.M())/tt_gen_ttbar_beforeFSR_p4.M() ::: tt_gen_ttbar_beforeFSR_p4.M()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0].size() > 0', 'tt_gen_ttbar_decay_type > 0'),
            'binning': (100, -2, 4, 100, 250, 2500)
        },
        #{ 
        #    'name': 'llbbMet_TT_M_resolution_CAT_#CAT_TITLE#',
        #    'variable': '(tt_ttbar[#LEPLEP_IDISO_BBWP#][0][0].p4.M() - tt_gen_ttbar_p4.M()) / tt_gen_ttbar_p4.M() ' ,
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0].size() > 0', 'tt_gen_ttbar_decay_type > 0'),
        #    'binning': (200, -10, 10)
        #},
        #{ 
        #    'name': 'llbbMet_TT_M_minus_Mgen_CAT_#CAT_TITLE#',
        #    'variable': 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0][0].p4.M() - tt_gen_ttbar_p4.M()',
        #    'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0].size() > 0', 'tt_gen_ttbar_decay_type > 0'),
        #    'binning': (100, -1000, 1000)
        #},

        ## TT reconstruction with smearing
        # TT
        {
            'name': 'llbbMet_RecoTop_TT_M_CAT_#CAT_TITLE#',
            'variable': 'recoTTbar[#RECOTTBAR_INDEX#].ttbar_p4.M()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, 250, 2500)
        },
        {
            'name': 'llbbMet_RecoTop_TT_Pt_CAT_#CAT_TITLE#',
            'variable': 'recoTTbar[#RECOTTBAR_INDEX#].ttbar_p4.Pt()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, 0, 500)
        },
        {
            'name': 'llbbMet_RecoTop_TT_Eta_CAT_#CAT_TITLE#',
            'variable': 'recoTTbar[#RECOTTBAR_INDEX#].ttbar_p4.Eta()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, -5, 5)
        },
        {
            'name': 'llbbMet_RecoTop_TT_DEta_CAT_#CAT_TITLE#',
            'variable': 'std::abs(recoTTbar[#RECOTTBAR_INDEX#].t_p4.Eta()-recoTTbar[#RECOTTBAR_INDEX#].tbar_p4.Eta())',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, 0, 7)
        },
        {
            'name': 'llbbMet_RecoTop_TT_Rapidity_CAT_#CAT_TITLE#',
            'variable': 'recoTTbar[#RECOTTBAR_INDEX#].ttbar_p4.Rapidity()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, -3, 3)
        },
        {
            'name': 'llbbMet_RecoTop_TT_DeltaRapidity_CAT_#CAT_TITLE#',
            'variable': 'std::abs(recoTTbar[#RECOTTBAR_INDEX#].t_p4.Rapidity()-recoTTbar[#RECOTTBAR_INDEX#].t_p4.Rapidity())',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, 0, 4)
        },
        {
            'name': 'llbbMet_RecoTop_TT_DR_CAT_#CAT_TITLE#',
            'variable': 'ROOT::Math::VectorUtil::DeltaR(recoTTbar[#RECOTTBAR_INDEX#].t_p4, recoTTbar[#RECOTTBAR_INDEX#].tbar_p4)',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, 0, 6)
        },
        # Top
        {
            'name': 'llbbMet_RecoTop_Top_Pt_CAT_#CAT_TITLE#',
            'variable': 'recoTTbar[#RECOTTBAR_INDEX#].t_p4.Pt()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, 0, 500)
        },
        {
            'name': 'llbbMet_RecoTop_Top_Eta_CAT_#CAT_TITLE#',
            'variable': 'recoTTbar[#RECOTTBAR_INDEX#].t_p4.Eta()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, -5, 5)
        },
        {
            'name': 'llbbMet_RecoTop_Top_Rapidity_CAT_#CAT_TITLE#',
            'variable': 'recoTTbar[#RECOTTBAR_INDEX#].t_p4.Rapidity()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, -3, 3)
        },
        # AntiTop
        {
            'name': 'llbbMet_RecoTop_AntiTop_Pt_CAT_#CAT_TITLE#',
            'variable': 'recoTTbar[#RECOTTBAR_INDEX#].tbar_p4.Pt()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, 0, 500)
        },
        {
            'name': 'llbbMet_RecoTop_AntiTop_Eta_CAT_#CAT_TITLE#',
            'variable': 'recoTTbar[#RECOTTBAR_INDEX#].tbar_p4.Eta()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, -5, 5)
        },
        {
            'name': 'llbbMet_RecoTop_AntiTop_Rapidity_CAT_#CAT_TITLE#',
            'variable': 'recoTTbar[#RECOTTBAR_INDEX#].tbar_p4.Rapidity()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (20, -3, 3)
        },
        # Reco nSols
        {
            'name': 'llbbMet_RecoTop_nSols_CAT_#CAT_TITLE#',
            'variable': 'recoTTbar[#RECOTTBAR_INDEX#].nSols',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (101, 0, 101)
        },
        {
            'name': 'llbbMet_RecoTop_totWeight_CAT_#CAT_TITLE#',
            'variable': 'recoTTbar[#RECOTTBAR_INDEX#].weight',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#'),
            'binning': (50, 0, 0.015)
        },
        {
            'name': 'llbbMet_minDRbl_vs_gen_TT_M_CAT_#CAT_TITLE#',
            'variable': 'tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].minDRjl ::: tt_gen_ttbar_beforeFSR_p4.M()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'gen_isSignal'),
            'binning': (50, 0, 6, 50, 250, 2500)
        },
        # Resolution
        {
            'name': 'llbbMet_RecoTop_TT_M_Resolution_CAT_#CAT_TITLE#',
            'variable': '(recoTTbar[#RECOTTBAR_INDEX#].ttbar_p4.M() - tt_gen_ttbar_beforeFSR_p4.M()) / tt_gen_ttbar_beforeFSR_p4.M()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0].size() > 0', 'tt_gen_ttbar_decay_type > 0'),
            'binning': (100, -2, 4)
        },
        {
            'name': 'llbbMet_RecoTop_TT_M_minus_Mgen_CAT_#CAT_TITLE#',
            'variable': 'recoTTbar[#RECOTTBAR_INDEX#].ttbar_p4.M() - tt_gen_ttbar_beforeFSR_p4.M()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0].size() > 0', 'tt_gen_ttbar_decay_type > 0'),
            'binning': (100, -1000, 1000)
        },
        {
            'name': 'llbbMet_RecoTop_TT_M_minus_Mgen_vs_Mgen_CAT_#CAT_TITLE#',
            'variable': 'recoTTbar[#RECOTTBAR_INDEX#].ttbar_p4.M() - tt_gen_ttbar_beforeFSR_p4.M() ::: tt_gen_ttbar_beforeFSR_p4.M()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0].size() > 0', 'tt_gen_ttbar_decay_type > 0'),
            'binning': (100, -1000, 1000, 100, 250, 2500)
        },
        {
            'name': 'llbbMet_RecoTop_TT_M_Resolution_vs_Mgen_CAT_#CAT_TITLE#',
            'variable': '(recoTTbar[#RECOTTBAR_INDEX#].ttbar_p4.M() - tt_gen_ttbar_beforeFSR_p4.M())/tt_gen_ttbar_beforeFSR_p4.M() ::: tt_gen_ttbar_beforeFSR_p4.M()',
            'plot_cut': joinCuts('#LEPLEP_CAT_CUTS#', '#JET_CAT_CUTS#', 'tt_ttbar[#LEPLEP_IDISO_BBWP#][0].size() > 0', 'tt_gen_ttbar_decay_type > 0'),
            'binning': (100, -2, 4, 100, 250, 2500)
        },
    ]

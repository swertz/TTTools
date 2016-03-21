#### This file is passed to treeFactory
#### It generates the config needed to define the skimmed tree's new branches 

import inspect
import os
import sys

#### Get directory where scripts are stored to handle the import correctly
scriptDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(scriptDir)
sys.path.append(scriptDir + "/../")

from common.TTAnalysis import pathCMS, pathTT, joinCuts, TT
import treeConfig

code_before_loop = ""
code_in_loop = ""
code_after_loop = ""
extra_branches = []

#### Chosen working points

elID = TT.LepID.M
elIso = TT.LepIso.L

muID = TT.LepID.T
muIso = TT.LepIso.T

bTag = TT.BWP.L

#### Define flavour-independent quantities to be used in the code for the branches
#### depending on which lepton pair is actually selected.

code_in_loop += """
uint16_t leplepIDIso = 0;
uint16_t leplepIDIsoBB = 0;

uint16_t diLepDiJetMetIdx = 0;
uint16_t diLepDiJetIdx = 0;
uint16_t diJetIdx = 0;
uint16_t bJet1Idx = 0;
uint16_t bJet2Idx = 0;
uint16_t diLepIdx = 0;
uint16_t lep1Idx = 0;
uint16_t lep2Idx = 0;

const TTAnalysis::DiLepDiJetMet *diLepDiBJetMet;
const TTAnalysis::DiLepDiJet *diLepDiBJet;
const TTAnalysis::DiJet *diBJet;
const TTAnalysis::Jet *bJet1, *bJet2;
const TTAnalysis::DiLepton *diLepton;
const TTAnalysis::Lepton *lepton1, *lepton2;

bool diLepton_isOS, diLepton_HLT;
bool diLepton_Mll = false;
bool diLepton_ZVeto = false;
"""

category_code = """
bool cat{3}_pre = tt_{4}_Category_{0}_cut && tt_diLepDiBJetsMet_DRCut_BWP_CSVv2Ordered[{2}].size() == 1;
bool cat{3} = false;
if(cat{3}_pre){{
    leplepIDIsoBB = {2};
    
    if(tt_diLeptons[ tt_diLepDiJetsMet[diLepDiJetMetIdx].diLepIdx ].is{3}) {{
        cat{3} = runOnMC || runOn{3};
        
        leplepIDIso = {1};
        
        diLepDiJetMetIdx = tt_diLepDiBJetsMet_DRCut_BWP_CSVv2Ordered[leplepIDIsoBB][0];
        diLepDiJetIdx = tt_diLepDiJetsMet[diLepDiJetMetIdx].diLepDiJetIdx;
        diJetIdx = tt_diLepDiJetsMet[diLepDiJetMetIdx].diJetIdx;
        bJet1Idx = tt_diJets[diJetIdx].jidxs.first;
        bJet2Idx = tt_diJets[diJetIdx].jidxs.second;        
        diLepIdx = tt_diLepDiJetsMet[diLepDiJetMetIdx].diLepIdx;
        lep1Idx = tt_diLeptons[diLepIdx].lidxs.first;
        lep2Idx = tt_diLeptons[diLepIdx].lidxs.second;

        diLepDiBJetMet = &tt_diLepDiJetsMet[diLepDiJetMetIdx];
        diLepDiBJet = &tt_diLepDiJets[diLepDiJetIdx];
        diBJet = &tt_diJets[diJetIdx];
        bJet1 = &tt_selJets[bJet1Idx];
        bJet2 = &tt_selJets[bJet2Idx];
        diLepton = &tt_diLeptons[diLepIdx];
        lepton1 = &tt_leptons[lep1Idx];
        lepton2 = &tt_leptons[lep2Idx];
        
        diLepton_isOS = tt_{4}_DiLeptonIsOS_{0}_cut;
        diLepton_HLT = tt_{4}_DiLeptonTriggerMatch_{0}_cut;
        diLepton_Mll = tt_{4}_Mll_{0}_cut;
        diLepton_ZVeto = tt_{4}_MllZVeto_{0}_cut;
    }}
}}
"""

code_in_loop += category_code.format(
        TT.LepLepIDIsoStr(elID, elIso, elID, elIso),
        TT.LepLepIDIso(elID, elIso, elID, elIso),
        TT.LepLepIDIsoJetJetBWP(elID, elIso, elID, elIso, bTag, bTag),
        "ElEl", "elel"
    )

code_in_loop += category_code.format(
        TT.LepLepIDIsoStr(elID, elIso, muID, muIso),
        TT.LepLepIDIso(elID, elIso, muID, muIso),
        TT.LepLepIDIsoJetJetBWP(elID, elIso, muID, muIso, bTag, bTag),
        "ElMu", "elmu"
    )

code_in_loop += category_code.format(
        TT.LepLepIDIsoStr(muID, muIso, elID, elIso),
        TT.LepLepIDIso(muID, muIso, elID, elIso),
        TT.LepLepIDIsoJetJetBWP(muID, muIso, elID, elIso, bTag, bTag),
        "MuEl", "muel"
    )

code_in_loop += category_code.format(
        TT.LepLepIDIsoStr(muID, muIso, muID, muIso),
        TT.LepLepIDIso(muID, muIso, muID, muIso),
        TT.LepLepIDIsoJetJetBWP(muID, muIso, muID, muIso, bTag, bTag),
        "MuMu", "mumu"
    )

code_in_loop += """
if(catElMu || catMuEl) diLepton_ZVeto = true;
if(catElEl + catElMu + catMuEl + catElEl != 1) continue;
"""

# The branches needed above will most likely not be used for the skimmer's branches => we have to add them all ourselves
extra_branches += ["tt_diLepDiBJetsMet_DRCut_BWP_CSVv2Ordered", "tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered", "tt_diLepDiJetsMet", "tt_diLepDiJets", "tt_diJets", "tt_diLeptons", "tt_selJets", "tt_leptons"]

extra_branches_categs_base = ["tt_{0}_Category_{1}_cut", "tt_{0}_DiLeptonIsOS_{1}_cut", "tt_{0}_DiLeptonTriggerMatch_{1}_cut", "tt_{0}_Mll_{1}_cut", "tt_{0}_MllZVeto_{1}_cut"]

for branch in extra_branches_categs_base:
    extra_branches.append( branch.format("elel", TT.LepLepIDIsoStr(elID, elIso, elID, elIso)) )
    extra_branches.append( branch.format("elmu", TT.LepLepIDIsoStr(elID, elIso, muID, muIso)) )
    extra_branches.append( branch.format("muel", TT.LepLepIDIsoStr(muID, muIso, elID, elIso)) )
    extra_branches.append( branch.format("mumu", TT.LepLepIDIsoStr(muID, muIso, muID, muIso)) )

#### Include source file with the HLT SFs ####

includes = ["../common/HLT_SF.h", "../common/TTbarReconstruction/SmearingFunction.h", "../common/TTbarReconstruction/TTbarReconstructor.h"]
sources = [pathTT + "/src/NeutrinosSolver.cc"]

#### TTbar system reconstruction ####

code_before_loop += """
DiracDelta topMass(172.5);
//BreitWigner wMass(80.4, 2.0, 2);
DiracDelta wMass(80.4);
//DiracDelta bJetTF;
//SimpleGaussianOnEnergy bJetTF(0, 0.1, 2);
TFile* tfFile = TFile::Open("/home/fynu/swertz/scratch/CMSSW_7_6_3_patch2/src/cp3_llbb/TTTools/histFactory/transferFunctions/tf_beforeFSR_allLoose.root");
Binned2DTransferFunction bJetTF("bJet_bParton_DeltaEvsE_Norm", tfFile);
DiracDelta leptonDelta;

TTbarReconstructor *myReconstructor = new TTbarReconstructor(
                    leptonDelta,
                    leptonDelta,
                    bJetTF,
                    wMass,
                    topMass,
                    1000);
"""

code_in_loop += """
TTbarSolution recoTTbar = myReconstructor->getSolution(
  lepton1->p4, lepton2->p4,
  bJet1->p4, bJet2->p4,
  met_p4,
  catElEl, catElMu, catMuEl, catMuMu,
  lepton1->charge);
"""

code_after_loop += "delete myReconstructor; tfFile->Close();"

#### Branches needed for TT reconstruction: just in case they're not already included

extra_branches += ["tt_leptons", "tt_diLeptons", "tt_diLeptons_IDIso", "tt_selJets", "tt_diJets", "tt_diLepDiJets", "tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered", "met_p4"]

#### Finally, configure the tree's branches
#### We don't need a global cut since we've taken care of it ourselves above

tree = treeConfig.tree

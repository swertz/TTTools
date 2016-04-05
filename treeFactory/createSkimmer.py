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
import common.ScaleFactors as SF
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

bTag1 = TT.BWP.L
bTag2 = TT.BWP.L

#### Define flavour-independent quantities to be used in the code for the branches
#### depending on which lepton pair is actually selected.

code_in_loop += """
uint16_t leplepIDIso = 0;
uint16_t leplepIDIsoBB = 0;

// This can be modified if the TT reconstruction selects
// another (ie not the first) di-jet pair!
uint16_t chosenDiLepDiBJetsMet = 0;

uint16_t diLepDiJetMetIdx = 0;
uint16_t diLepDiJetIdx = 0;
uint16_t diJetIdx = 0;
uint16_t bJet1Idx = 0;
uint16_t bJet2Idx = 0;
uint16_t fwk_jet1Idx = 0;
uint16_t fwk_jet2Idx = 0;
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

float sf_HLT = 1;
float sf_diLepton = 1;
float sf_diBJet = 1;

TTbarSolution recoTTbar;
bool recoTop_valid = false;
"""

category_code = """
bool cat{catCap}_pre = tt_{catMin}_Category_{lepLepIDIsoStr}_cut && tt_diLeptons_IDIso[{lepLepIDIso}].size() == 1 && tt_diLepDiBJetsMet_DRCut_BWP_CSVv2Ordered[{lepLepIDIsoJetJetBWP}].size() >= 1;
bool cat{catCap} = false;
if(cat{catCap}_pre){{
    leplepIDIsoBB = {lepLepIDIsoJetJetBWP};
    
    if(tt_diLeptons[ tt_diLepDiJetsMet[diLepDiJetMetIdx].diLepIdx ].is{catCap}) {{
        cat{catCap} = runOnMC || runOn{catCap};
        
        leplepIDIso = {lepLepIDIso};
        
        recoTTbar = myReconstructor->getSolution(
            tt_leptons,
            tt_diLeptons,
            tt_selJets,
            tt_diJets,
            tt_diLepDiJetsMet,
            met_p4,
            tt_diLepDiBJetsMet_DRCut_BWP_CSVv2Ordered[leplepIDIsoBB] 
            );
        recoTop_valid = recoTTbar.nSols > 0;
        
        if(recoTop_valid){{
            chosenDiLepDiBJetsMet = recoTTbar.chosenDiLepDiBJetsMet;
            diLepDiJetMetIdx = recoTTbar.diLepDiJetMetIdx;
        }}else{{
            diLepDiJetMetIdx = tt_diLepDiBJetsMet_DRCut_BWP_CSVv2Ordered[leplepIDIsoBB][0];
        }}
        
        diLepDiJetIdx = tt_diLepDiJetsMet[diLepDiJetMetIdx].diLepDiJetIdx;
        diJetIdx = tt_diLepDiJetsMet[diLepDiJetMetIdx].diJetIdx;
        bJet1Idx = tt_diJets[diJetIdx].jidxs.first;
        bJet2Idx = tt_diJets[diJetIdx].jidxs.second;        
        fwk_jet1Idx = tt_diJets[diJetIdx].idxs.first;
        fwk_jet2Idx = tt_diJets[diJetIdx].idxs.second;        
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
        
        diLepton_isOS = tt_{catMin}_DiLeptonIsOS_{lepLepIDIsoStr}_cut;
        diLepton_HLT = tt_{catMin}_DiLeptonTriggerMatch_{lepLepIDIsoStr}_cut;
        diLepton_Mll = tt_{catMin}_Mll_{lepLepIDIsoStr}_cut;
        diLepton_ZVeto = tt_{catMin}_MllZVeto_{lepLepIDIsoStr}_cut;

        sf_HLT = {sf_HLT};
        sf_diLepton = {sf_diLepton};
        sf_diBJet = {sf_diBJet};
    }}
}}
"""

category_map = [
        {
            "lepLepIDIsoStr": TT.LepLepIDIsoStr(elID, elIso, elID, elIso),
            "lepLepIDIso": TT.LepLepIDIso(elID, elIso, elID, elIso),
            "lepLepIDIsoJetJetBWP":  TT.LepLepIDIsoJetJetBWP(elID, elIso, elID, elIso, bTag1, bTag2),
            "catCap": "ElEl", "catMin": "elel",
            "sf_HLT": SF.get_HLT_SF_for_dilepton(0, elID, elID, elIso, elIso),
            "sf_diLepton": SF.get_leptons_SF_for_dilepton(0, elID, elID, elIso, elIso),
            "sf_diBJet": SF.get_at_least_two_b_SF_for_dijet("chosenDiLepDiBJetsMet", bTag1, bTag2, elID, elID, elIso, elIso),
        },
        {
            "lepLepIDIsoStr": TT.LepLepIDIsoStr(elID, elIso, muID, muIso),
            "lepLepIDIso": TT.LepLepIDIso(elID, elIso, muID, muIso),
            "lepLepIDIsoJetJetBWP":  TT.LepLepIDIsoJetJetBWP(elID, elIso, muID, muIso, bTag1, bTag2),
            "catCap": "ElMu", "catMin": "elmu",
            "sf_HLT": SF.get_HLT_SF_for_dilepton(0, elID, muID, elIso, muIso),
            "sf_diLepton": SF.get_leptons_SF_for_dilepton(0, elID, muID, elIso, muIso),
            "sf_diBJet": SF.get_at_least_two_b_SF_for_dijet("chosenDiLepDiBJetsMet", bTag1, bTag2, elID, muID, elIso, muIso),
        },
        {
            "lepLepIDIsoStr": TT.LepLepIDIsoStr(muID, muIso, elID, elIso),
            "lepLepIDIso": TT.LepLepIDIso(muID, muIso, elID, elIso),
            "lepLepIDIsoJetJetBWP": TT.LepLepIDIsoJetJetBWP(muID, muIso, elID, elIso, bTag1, bTag2),
            "catCap": "MuEl", "catMin": "muel",
            "sf_HLT": SF.get_HLT_SF_for_dilepton(0, muID, elID, muIso, elIso),
            "sf_diLepton": SF.get_leptons_SF_for_dilepton(0, muID, elID, muIso, elIso),
            "sf_diBJet": SF.get_at_least_two_b_SF_for_dijet("chosenDiLepDiBJetsMet", bTag1, bTag2, muID, elID, muIso, elIso),
        },
        {
            "lepLepIDIsoStr": TT.LepLepIDIsoStr(muID, muIso, muID, muIso),
            "lepLepIDIso": TT.LepLepIDIso(muID, muIso, muID, muIso),
            "lepLepIDIsoJetJetBWP": TT.LepLepIDIsoJetJetBWP(muID, muIso, muID, muIso, bTag1, bTag2),
            "catCap": "MuMu", "catMin": "mumu",
            "sf_HLT": SF.get_HLT_SF_for_dilepton(0, muID, muID, muIso, muIso),
            "sf_diLepton": SF.get_leptons_SF_for_dilepton(0, muID, muID, muIso, muIso),
            "sf_diBJet": SF.get_at_least_two_b_SF_for_dijet("chosenDiLepDiBJetsMet", bTag1, bTag2, muID, muID, muIso, muIso),
        },
    ]

for categ in category_map:
    code_in_loop += category_code.format(**categ)

code_in_loop += """
if(catElMu || catMuEl) diLepton_ZVeto = true;
if(catElEl + catElMu + catMuEl + catElEl != 1) continue;
"""

# The branches needed above will most likely not be used for the skimmer's branches => we have to add them all ourselves
extra_branches += ["tt_diLepDiBJetsMet_DRCut_BWP_CSVv2Ordered", "tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered", "tt_diLepDiJetsMet", "tt_diLepDiJets", "tt_diJets", "tt_diLeptons", "tt_diLeptons_IDIso", "tt_selJets", "tt_leptons"]

extra_branches += [SF.get_csvv2_sf_branch(bTag1), SF.get_csvv2_sf_branch(bTag2), SF.get_electron_id_sf_branch(elID), SF.get_muon_id_sf_branch(muID), SF.get_muon_iso_sf_branch(muIso, muID)]
# needed because of the way the el/mu SFs are called (not actually used:)
extra_branches += [SF.get_electron_id_sf_branch(muID), SF.get_muon_id_sf_branch(elID), SF.get_muon_iso_sf_branch(elIso, elID)]

extra_branches_categs_base = ["tt_{0}_Category_{1}_cut", "tt_{0}_DiLeptonIsOS_{1}_cut", "tt_{0}_DiLeptonTriggerMatch_{1}_cut", "tt_{0}_Mll_{1}_cut", "tt_{0}_MllZVeto_{1}_cut"]

for branch in extra_branches_categs_base:
    extra_branches.append( branch.format("elel", TT.LepLepIDIsoStr(elID, elIso, elID, elIso)) )
    extra_branches.append( branch.format("elmu", TT.LepLepIDIsoStr(elID, elIso, muID, muIso)) )
    extra_branches.append( branch.format("muel", TT.LepLepIDIsoStr(muID, muIso, elID, elIso)) )
    extra_branches.append( branch.format("mumu", TT.LepLepIDIsoStr(muID, muIso, muID, muIso)) )

#### Include source file with the HLT SFs ####

includes = ["../common/HLT_SF.h"]
includes += ["../common/TTbarReconstruction/recommendedSmearing/SmearingFunction.h", "../common/TTbarReconstruction/recommendedSmearing/TTbarReconstructor.h"]
sources = [pathTT + "/src/NeutrinosSolver.cc"]

#### TTbar system reconstruction ####

code_before_loop += """
TFile* fileGenBJets = TFile::Open("/home/fynu/swertz/scratch/CMSSW_7_6_3_patch2/src/cp3_llbb/TTTools/histFactory/transferFunctions/160331_withCorrelations_0/genInfo_smearingTFs_bJets.root");
TFile* fileLeptons = TFile::Open("/home/fynu/swertz/scratch/CMSSW_7_6_3_patch2/src/cp3_llbb/TTTools/histFactory/transferFunctions/160331_withCorrelations_0/smearingTFs_leptons.root");

DiracDelta topMass(172.5);
Binned1DTransferFunction wMass("gen_MW", fileGenBJets);
//DiracDelta wMass(80.4);

//DiracDelta bJetTF;

Binned1DTransferFunctionOnEnergyRatio bJetEnergyTF("EgenOverEreco_bJet", fileGenBJets);
Binned1DTransferFunctionOnAngle bJetAngleTF("Angle_bJet", fileGenBJets);

//DiracDelta leptonDelta;

Binned1DTransferFunctionOnEnergyRatio electronEnergyTF("EgenOverEreco_electron", fileLeptons);
Binned1DTransferFunctionOnAngle electronAngleTF("Angle_electron", fileLeptons);

Binned1DTransferFunctionOnEnergyRatio muonEnergyTF("EgenOverEreco_muon", fileLeptons);
Binned1DTransferFunctionOnAngle muonAngleTF("Angle_muon", fileLeptons);

Binned1DTransferFunction MblSmearing("gen_Mbl", fileGenBJets);

TTbarReconstructor *myReconstructor = new TTbarReconstructor(
                    electronEnergyTF,
                    electronAngleTF,
                    muonEnergyTF,
                    muonAngleTF,
                    bJetEnergyTF,
                    bJetAngleTF,
                    wMass,
                    topMass,
                    MblSmearing,
                    100);
"""

code_in_loop += """
"""

code_after_loop += "delete myReconstructor; fileGenBJets->Close(); fileLeptons->Close();"

#### Branches needed for TT reconstruction: just in case they're not already included

extra_branches += ["tt_leptons", "tt_diLeptons", "tt_selJets", "tt_diJets", "tt_diLepDiJetsMet", "met_p4", "tt_diLepDiBJetsMet_DRCut_BWP_CSVv2Ordered"]

#### Finally, configure the tree's branches
#### We don't need a global cut since we've taken care of it ourselves above

tree = treeConfig.tree

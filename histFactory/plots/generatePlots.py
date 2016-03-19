#### This file is passed to histFactory
#### It generates all the plot configs based on skeletons defined in basePlots
####  and on info defined in plotTools.

import inspect
import os
import sys

#### Get directory where script is stored to handle the import correctly
scriptDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(scriptDir)

from TTAnalysis import pathCMS, pathTT

#### Get dictionary definitions ####
from plotTools import *

#### Get plot skeletons from other file ####
import basePlots
import transferFunctions 

#### Define the sub-categories and the corresponding plot groups ####

categoryPlots = {
        
        ## ask for 2 leptons; vary over lepton ID & iso for two leptons
        #"llCategs": { 
        #    "plots": basePlots.ll,
        #    },
        #
        ## ask for 2 leptons & 2 jets; vary over lepton ID & iso for two leptons(take loosest ones for jet minDRjl cut)
        #"lljjCategs": { 
        #    "plots": basePlots.ll + basePlots.lljj,
        #    },
        
        ## ask for 2 leptons & 2 jets; vary over lepton ID & iso for two leptons (take loosest ones for jet minDRjl cut), and one b-tag working point
        #"lljj_b_Categs": { 
        #    "plots": basePlots.lljj_b,
        #    },
        
        ## ask for 2 leptons & 2 jets & 1 b-jet; vary over lepton ID & iso for two leptons (take loosest ones for jet minDRjl cut), and one b-tag working point
        #"llbjCategs": { 
        #    "plots": basePlots.llbj,
        #    },
        
        # ask for 2 leptons & 2 b-jets; vary over lepton ID & iso for two leptons (take loosest ones for jet minDRjl cut), and two b-tag working point
        "llbbCategs": { 
            #"plots": basePlots.ll + basePlots.lljj + basePlots.llbb + basePlots.llbb_recoTop,
            #"plots": transferFunctions.matchedBTFs,
            "plots": basePlots.genInfo + basePlots.llbb_recoTop,
            },
    
    }

# Initialize maps needed later
for categ in categoryPlots.values():
    categ["strings"] = []
    categ["weights"] = []


flavourCategPlots = { flav: copy.deepcopy(categoryPlots) for flav in myFlavours }

for flav in flavourCategPlots.items():
    generateCategoryStrings(flav[1], flav[0], doZVeto=False, useMCHLT=True)

#### Generate all the plots ####

plots = []
recoTTbarStrings = []

# Iterate over ll flavours
for flav in flavourCategPlots.values():

    # Iterate over category groups
    for categ in flav.values():

        # Iterate over each sub-category
        for subCateg_index, subCateg in enumerate(categ["strings"]):

            # Iterate over every plot skeleton defined for the current category group
            for plot in categ["plots"]:
                m_plot = copy.deepcopy(plot)
                if not 'scale-factors' in m_plot:
                    m_plot['scale-factors'] = True

                # Iterate over the string keys defined in the sub-category
                for key in subCateg.items():

                    # Update name, variable, and plot_cut field
                    for field in m_plot.keys():
                        if isinstance(m_plot[field], str):
                            m_plot[field] = m_plot[field].replace(key[0], str(key[1]))

                # Replace binning tuples by strings
                m_plot["binning"] = str(m_plot["binning"])

                # Plot weights
                m_plot["weight"] = "event_pu_weight * event_weight"
                if len(categ["weights"][subCateg_index]) > 0 and m_plot['scale-factors']:
                    m_plot["weight"] += " * " + "( {} )".format( ") * (".join(categ["weights"][subCateg_index]) )

                # If it is a plot using the TTbar reconstruction, we have to fiddle around a bit more
                if "RecoTop" in m_plot["name"]:
                    tt_index = str(len(recoTTbarStrings))
                    m_plot["variable"] = m_plot["variable"].replace("#RECOTTBAR_INDEX#", tt_index)
                    thisCutWithoutRecoTTbar = m_plot["plot_cut"]
                    m_plot["plot_cut"] = joinCuts(m_plot["plot_cut"], "recoTTbar[" + tt_index + "].nSols>0")
                    if (m_plot["plot_cut"],subCateg) not in recoTTbarStrings:
                        recoTTbarStrings.append( (thisCutWithoutRecoTTbar,subCateg) )
                
                plots.append(m_plot)

                print "Plot: {}\nVariable: {}\nCut: {}\nWeight: {}\nBinning: {}\n".format(m_plot["name"], m_plot["variable"], m_plot["plot_cut"], m_plot["weight"], m_plot["binning"])

print "Generated {} plots.\n".format(len(plots))

#### Include source file with the HLT SFs ####

includes = ["HLT_SF.h", "TTbarReconstruction/SmearingFunction.h", "TTbarReconstruction/TTbarReconstructor.h"]
#includes = ["HLT_SF.h", "TTbarReconstruction/SmearingFunction.h", "TTbarReconstruction/TTbarReconstructor.h", "<Math/VectorUtil.h>"]
sources = [pathTT + "/src/NeutrinosSolver.cc"]

#### TTbar system reconstruction ####

code_before_loop = """
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

ttbar_base_code = """
recoTTbar[#RECOTTBAR_INDEX#] = myReconstructor->getSolution(
  tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.first ].p4,
  tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.second ].p4,
  tt_selJets[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].jidxs.first ].p4,
  tt_selJets[ tt_diJets[ tt_diLepDiJets[ tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered[#LEPLEP_IDISO_BBWP#][0] ].diJetIdx ].jidxs.second ].p4,
  met_p4,
  tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].isElEl,
  tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].isElMu,
  tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].isMuEl,
  tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].isMuMu,
  tt_leptons[ tt_diLeptons[ tt_diLeptons_IDIso[#LEPLEP_IDISO#][0] ].lidxs.first ].charge
  );
"""

code_in_loop = "std::vector<TTbarSolution> recoTTbar(" + str(len(recoTTbarStrings)) + ");\n"

code_after_loop = "delete myReconstructor; tfFile->Close();"

for index, thisTTbar in enumerate(recoTTbarStrings):
    this_code = ttbar_base_code
    for key in thisTTbar[1].items():
        this_code = this_code.replace(key[0], str(key[1]))
    this_code = this_code.replace("#RECOTTBAR_INDEX#", str(index))
    this_code = "if(" + thisTTbar[0] + "){\n" + this_code + "\n}\n"
    code_in_loop += this_code

extra_branches = ["tt_leptons", "tt_diLeptons", "tt_diLeptons_IDIso", "tt_selJets", "tt_diJets", "tt_diLepDiBJets_DRCut_BWP_CSVv2Ordered"]

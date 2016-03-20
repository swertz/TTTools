import os
import ROOT as R

#### Get all the indices and functions definitions needed to retrieve the IDs/... ROOT can be awesome at times :) ####

pathCMS = os.getenv("CMSSW_BASE")
if pathCMS == "":
    raise Exception("CMS environment is not valid!")
pathTT = os.path.join(pathCMS, "src/cp3_llbb/TTAnalysis/")
pathTTdefs = os.path.join(pathTT, "plugins/Indices.cc")

R.gROOT.ProcessLine(".L " + pathTTdefs + "+")
TT =  R.TTAnalysis

#### Utility to join different cuts together (logical AND) ####

def joinCuts(*cuts):
    if len(cuts) == 0: 
        return ""
    elif len(cuts) == 1: 
        return cuts[0]
    else:
        totalCut = "("
        for cut in cuts:
            cut = cut.strip().strip("&")
            if cut == "":
                continue
            totalCut += "(" + cut + ")&&" 
        totalCut = totalCut.strip("&") + ")"
        return totalCut

#### The IDs/... we want to run on ####

# Default choice
electronID = { TT.LepID.M: "M" }
muonID = { TT.LepID.T: "T" }
electronIso = { TT.LepIso.L: "L" }
muonIso = { TT.LepIso.T: "T" }

#electronID = { TT.LepID.L: "L", TT.LepID.M: "M" }
#electronID = { TT.LepID.L: "L", TT.LepID.M: "M", TT.LepID.T: "T" }

# Loose (for TFs)
#electronID = { TT.LepID.L: "L" }
#muonID = { TT.LepID.L: "L" }
#electronIso = { TT.LepIso.L: "L" }
#muonIso = { TT.LepIso.L: "L" }

#myBWPs = { wp.first: wp.second for wp in TT.BWP.map }
#myBWPs = { TT.BWP.L: "L", TT.BWP.M: "M" } 
myBWPs = { TT.BWP.L: "L" } 

myFlavours = [ "ElEl", "MuEl", "ElMu", "MuMu" ]
#myFlavours = [ "ElEl" ]
#myFlavours = [ "MuMu" ]
#myFlavours = [ "ElMu", "MuEl" ]

keepOnlySymmetricWP = False

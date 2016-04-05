#!/nfs/soft/python/python-2.7.5-sl6_amd64_gcc44/bin/python

# usage in TTTools/histFactory : python launchJobs.py -o condorOutDir -t -p pathToPlotterExe [-s]

import sys, os, json
import copy
import datetime

import argparse

# Add default ingrid storm package
sys.path.append('/nfs/soft/python/python-2.7.5-sl6_amd64_gcc44/lib/python2.7/site-packages/storm-0.20-py2.7-linux-x86_64.egg')
sys.path.append('/nfs/soft/python/python-2.7.5-sl6_amd64_gcc44/lib/python2.7/site-packages/MySQL_python-1.2.3-py2.7-linux-x86_64.egg')

CMSSW_BASE = os.environ['CMSSW_BASE']
SCRAM_ARCH = os.environ['SCRAM_ARCH']
sys.path.append(os.path.join(CMSSW_BASE,'bin', SCRAM_ARCH))
sys.path.append(os.path.join(CMSSW_BASE, "src/cp3_llbb/CommonTools/histFactory/"))
sys.path.append(os.path.join(CMSSW_BASE, "src/cp3_llbb/CommonTools/treeFactory/"))

from condorTools import condorSubmitter

# Prod 16/03/07
#IDs = range(1462, 1483)
IDs = range(1462, 1471)
IDs.remove(1467)
#IDs.remove(1471)
IDs.append(1506)
#IDs = [1506]

parser = argparse.ArgumentParser(description='Facility to submit treeFactory/histFactory jobs on condor.', usage='Usage in TTTools/common: python launchHistFactory.py -o condorOutDir -f -p pathToPlotterExe [-s]')
parser.add_argument('-o', '--output', dest='output', default=str(datetime.date.today()), help='Name of output directory.')
parser.add_argument('-s', '--submit', help='Choice to actually submit the jobs or not.', action="store_true")
parser.add_argument('-f', '--filter', dest='filter', default=False, help='Apply filter on DY ht and TT lepton flavour.', action="store_true")
parser.add_argument('-p', '--plotter', dest='plotter', help='Path to plotter.')
parser.add_argument('-r', '--remove', help='Overwrite output directory if it already exists.', action="store_true")

args = parser.parse_args()

samples = []
for ID in IDs:
    filesperJob = 5
    samples.append(
        {
            "ID": ID,
            "files_per_job": filesperJob,
        }
    )

if args.remove :
    if os.path.isdir(args.output) :
        print "Are you sure you want to execute the following command ?"
        print "rm -r " + args.output
        print "Type enter if yes, ctrl-c if not."
        raw_input()
        os.system("rm -r " + args.output)
        print "Deleted ", args.output, " folder."

mySub = condorSubmitter(samples, args.plotter, "DUMMY", args.output + "/", rescale = True)

## Create test_condor directory and subdirs
mySub.setupCondorDirs()

## Write command and data files in the condor directory
mySub.createCondorFiles()

## Modifies the input sample jsons to add sample cuts for TT decays
if args.filter : 
    jsonSampleFileList = [os.path.join(mySub.inDir,jsonSampleFile) for jsonSampleFile in os.listdir(mySub.inDir) if "sample" in jsonSampleFile]
    for jsonSampleFilePath in jsonSampleFileList : 
        with open(jsonSampleFilePath, 'r') as jsonSampleFile :
            jsonSample = json.load(jsonSampleFile)
            for sampleName in jsonSample.keys():
                if 'TT_TuneCUETP8M1_13TeV-powheg-pythia8' in sampleName : 
                    
                    ## New division: dilep (excluding taus), dilep(with one or two taus) and all the rest
                    ttflname = sampleName + "_signal"
                    jsonSample[ttflname] = copy.deepcopy(jsonSample[sampleName])
                    jsonSample[ttflname]["sample_cut"] = "(tt_gen_ttbar_decay_type >= 4 && tt_gen_ttbar_decay_type <= 6 )"
                    jsonSample[ttflname]["output_name"] += "_signal"

                    ttflname = sampleName + "_tau"
                    jsonSample[ttflname] = copy.deepcopy(jsonSample[sampleName])
                    jsonSample[ttflname]["sample_cut"] = "tt_gen_ttbar_decay_type >= 8"
                    jsonSample[ttflname]["output_name"] += "_tau"

                    ttflname = sampleName + "_other"
                    jsonSample[ttflname] = copy.deepcopy(jsonSample[sampleName])
                    jsonSample[ttflname]["sample_cut"] = "!(tt_gen_ttbar_decay_type >= 4 && tt_gen_ttbar_decay_type <= 6 ) && tt_gen_ttbar_decay_type < 8"
                    jsonSample[ttflname]["output_name"] += "_other"

                    ## Old division (dilep - semilep - hadr) with taus included in "lepton"
                    #ttflname = sampleName + "_diLep"
                    #jsonSample[ttflname] = copy.deepcopy(jsonSample[sampleName])
                    #jsonSample[ttflname]["sample_cut"] = "(tt_gen_ttbar_decay_type >= 4 && tt_gen_ttbar_decay_type <= 6 ) || tt_gen_ttbar_decay_type >= 8"
                    #jsonSample[ttflname]["output_name"] += "_diLep"

                    #ttslname = sampleName + "_semiLep"
                    #jsonSample[ttslname] = copy.deepcopy(jsonSample[sampleName])
                    #jsonSample[ttslname]["sample_cut"] = "tt_gen_ttbar_decay_type == 2 || tt_gen_ttbar_decay_type == 3 || tt_gen_ttbar_decay_type == 7"
                    #jsonSample[ttslname]["output_name"] += "_semiLep"

                    #ttfhname = sampleName + "_hadr"
                    #jsonSample[ttfhname] = copy.deepcopy(jsonSample[sampleName])
                    #jsonSample[ttfhname]["sample_cut"] = "tt_gen_ttbar_decay_type <= 1"
                    #jsonSample[ttfhname]["output_name"] += "_hadr"
                    
                    jsonSample.pop(sampleName)

        with open(jsonSampleFilePath, 'w+') as jsonSampleFile :
            json.dump(jsonSample, jsonSampleFile)
                

## Actually submit the jobs
## It is recommended to do a dry-run first without submitting to condor
if args.submit : 
    mySub.submitOnCondor()

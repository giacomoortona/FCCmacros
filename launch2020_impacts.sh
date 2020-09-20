#!/bin/bash
#stuff to run on condor

cd /afs/cern.ch/user/g/gortona/work/FCCmacros/CMSSW_10_2_13/src
eval $(scram ru -sh)
cmsenv
cd /afs/cern.ch/user/g/gortona/work/FCCmacros/

export scen=$1
export syst=$2

export chan=$3
### impacts
# echo "combineTool.py -M Impacts -d combCard_1.00_syst2.txt --doInitialFit --redefineSignalPOIs kl --setParameterRanges kl=0.7,1.3 -t -1 --setParameters $defParams --freezeParameters ${paramFreezer},r -n kl_impact2 --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-8"
#combineTool.py -M Impacts -d cardComb_syst${2}_${1}${6}${4}${5}${3}${7}.root --doInitialFit --redefineSignalPOIs kl --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1,BkgScaler=1.0,fakeScaler=0.7,smearPhoton=1.3,fakeRater=1.0,btagger=1.0,ttbarScaler=1.0,lumiScaler=1 --freezeParameters klConst,meanG,sigmaG,lumi,lumiSig,lumiTwoAll,BkgScaler,fakeScaler,effScaler,btagger,smearPhoton,lumiScaler,fakeRater,ttbarScaler,param0,param1,param2,param3,param4,paramL,paramH,r -n kl_impact2_bbaa --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-8
#combineTool.py -M Impacts -d cardComb_syst${2}_${1}${6}${4}${5}${3}${7}.root --doFits --redefineSignalPOIs kl --setParameterRanges kl=0.7,1.3 -t -1  -n kl_impact2_bbaa --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-8 -v 10 --setParameters kl=1,BkgScaler=1.0,ttbarScaler=1.0,lumiScaler=1 --freezeParameters klConst,meanG,sigmaG,lumi,lumiSig,lumiTwoAll,BkgScaler,fakeScaler,effScaler,btagger,smearPhoton,lumiScaler,fakeRater,ttbarScaler,param0,param1,param2,param3,param4,paramL,paramH,r
#combineTool.py -M Impacts -m 120 -d cardComb_syst2_IIMMMMM.root --doInitialFit --redefineSignalPOIs kl --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,jets_ID,param0,param1,param2,param3,lumiScaler,r,btag,btagbb,btagaa,xsec_QCD -n kl_impacts_comb_${2}_${1} --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7

if [ "${3}" == "comb" ]
then
combineTool.py -M Impacts -m 120 -d cardComb_syst${2}_${1}MMMMM.root --doInitialFit --redefineSignalPOIs kl --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,param0,param1,param2,param3,lumiScaler,r,beffQCD -n kl_impacts_comb_${2}_${1} --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7
combineTool.py -M Impacts -m 120 -d cardComb_syst${2}_${1}MMMMM.root --doFits --redefineSignalPOIs kl --setParameterRanges kl=0.7,1.3 -t -1 -n kl_impacts_comb_${2}_${1} --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7
else
	if [ "${3}" == "bbaa" ]
	then
		echo "bbaaa"
		text2workspace.py card1.00_syst${1}_sel0_${2}_MM.txt
		combineTool.py -M Impacts -m 120 -d card1.00_syst${2}_sel0_${1}_MM.root --doInitialFit --redefineSignalPOIs kl --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,lumiScaler,r -n kl_impacts_bbaa_${2}_${1} --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7
		combineTool.py -M Impacts -m 120 -d card1.00_syst${2}_sel0_${1}_MM.root --doFits --redefineSignalPOIs kl --setParameterRanges kl=0.7,1.3 -t -1 -n kl_impacts_bbaa_${2}_${1} --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7
	else 
		if [ "${3}" == "bbbb" ]
		then
			echo "bbbb"
			text2workspace.py card1.00_boosted_syst1_sel0_I_M.txt.txt
			combineTool.py -M Impacts -m 120 -d card1.00_boosted_syst${2}_sel0_${1}_M.root --doInitialFit --redefineSignalPOIs kl --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,lumiScaler,r,beffQCD -n kl_impacts_bbbb_${2}_${1} --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7
			combineTool.py -M Impacts -m 120 -d card1.00_boosted_syst${2}_sel0_${1}_M.root --doFits --redefineSignalPOIs kl --setParameterRanges kl=0.7,1.3 -t -1 -n kl_impacts_bbbb_${2}_${1} --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7
		else
			if [ "${3}" == "bbtt" ]
			then
				echo "bbtt"
				text2workspace.py cardbbttComb_syst${2}_${1}MM.txt
				combineTool.py -M Impacts -m 120 -d cardbbttComb_syst${2}_${1}MM.root --doInitialFit --redefineSignalPOIs kl --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,lumiScaler,r -n kl_impacts_bbtt_${2}_${1} --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7
				combineTool.py -M Impacts -m 120 -d cardbbttComb_syst${2}_${1}MM.root --doFits --redefineSignalPOIs kl --setParameterRanges kl=0.7,1.3 -t -1 -n kl_impacts_bbtt_${2}_${1} --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7
			fi
		fi
	fi
fi


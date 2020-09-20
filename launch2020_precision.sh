#!/bin/bash

##FitDiagnostics for lumi scaling
### forse dovrei modificare in modo da avere i punti in klambda direttamente invece delle cards scalate
### da fare dopo che ho i best WP cosi controlliamo che lambda mancano li

echo "lumiScaler rateParam * * 1.0 " >> cardComb_syst1_IMLMLL.txt
echo "lumiScaler rateParam * * 1.0 " >> cardComb_syst2_IIMLMLM.txt
echo "lumiScaler rateParam * * 1.0 " >> cardComb_syst3_IIIMLLLT.txt
text2workspace.py cardComb_syst1_IMLMLL.txt
text2workspace.py cardComb_syst2_IIMLMLM.txt
text2workspace.py cardComb_syst3_IIIMLLLT.txt
for ilumi in 0.01 0.02 0.03 0.04 0.05 0.06 0.07 0.08 0.09 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0 ; do combine -M MultiDimFit --algo=singles cardComb_syst1_IMLMLL.root --redefineSignalPOIs kl --setParameterRanges kl=0.7,1.3 -t -1 --setParameters lumiScaler=${ilumi},kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,jets_ID,param0,param1,param2,param3,paramL,paramH,paramL2,paramH2,lumiScaler,r,btag -n lumiScan_I_lumi${ilumi}_forPrec --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-8 ; combine -M MultiDimFit --algo=singles cardComb_syst2_IIMLMLM.root --redefineSignalPOIs kl --setParameterRanges kl=0.7,1.3 -t -1 --setParameters lumiScaler=${ilumi},kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,jets_ID,param0,param1,param2,param3,paramL,paramH,paramL2,paramH2,lumiScaler,r,btag -n lumiScan_II_lumi${ilumi}_forPrec --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-8 ; combine -M MultiDimFit --algo=singles cardComb_syst3_IIIMLLLT.root --redefineSignalPOIs kl --setParameterRanges kl=0.2,1.8 -t -1 --setParameters lumiScaler=${ilumi},kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,jets_ID,param0,param1,param2,param3,paramL,paramH,paramL2,paramH2,lumiScaler,r,btag -n lumiScan_III_lumi${ilumi}_forPrec --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-8 ; combine -M MultiDimFit --algo=singles cardComb_syst1_IMLMLL.root --redefineSignalPOIs kl --setParameterRanges kl=0.7,1.3 -t -1 --setParameters lumiScaler=${ilumi},kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters beffHH,beffSH,beffZ,beffTop,xsec_tt,xsec_ttH,xsec_HH,tauEff,lumi,jets_ID,lepton_ID,btag,xsec_HH,paramL,paramL2,paramH,paramH2,beffGJ,xsec_Zbb,gamma_ID,btagaa,BkgScaler_bbaa,beffQCD,btagbb,lumiScaler,r,btag -n lumiScan_I_lumi${ilumi}_noSyst_forPrec --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-8 --fastScan; done

for ilumi in 0.01 0.02 0.03 0.04 0.05 0.06 0.07 0.08 0.09 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0 ; do combine -M FitDiagnostics cardComb_syst1_IMLMLL.root --redefineSignalPOIs kl --setParameterRanges kl=0.7,1.3 -t -1 --setParameters lumiScaler=${ilumi},kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,jets_ID,param0,param1,param2,param3,paramL,paramH,paramL2,paramH2,lumiScaler,r,btag -n lumiScan_I_lumi${ilumi}_forPrec --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-8 ; combine -M FitDiagnostics cardComb_syst2_IIMLMLM.root --redefineSignalPOIs kl --setParameterRanges kl=0.7,1.3 -t -1 --setParameters lumiScaler=${ilumi},kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,jets_ID,param0,param1,param2,param3,paramL,paramH,paramL2,paramH2,lumiScaler,r,btag -n lumiScan_II_lumi${ilumi}_forPrec --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-8 ; combine -M FitDiagnostics cardComb_syst3_IIIMLLLT.root --redefineSignalPOIs kl --setParameterRanges kl=0.2,1.8 -t -1 --setParameters lumiScaler=${ilumi},kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,jets_ID,param0,param1,param2,param3,paramL,paramH,paramL2,paramH2,lumiScaler,r,btag -n lumiScan_III_lumi${ilumi}_forPrec --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-8 ; combine -M FitDiagnostics cardComb_syst1_IMLMLL.root --redefineSignalPOIs kl --setParameterRanges kl=0.7,1.3 -t -1 --setParameters lumiScaler=${ilumi},kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters beffHH,beffSH,beffZ,beffTop,xsec_tt,xsec_ttH,xsec_HH,tauEff,lumi,jets_ID,lepton_ID,btag,xsec_HH,paramL,paramL2,paramH,paramH2,beffGJ,xsec_Zbb,gamma_ID,btagaa,BkgScaler_bbaa,beffQCD,btagbb,lumiScaler,r,btag -n lumiScan_I_lumi${ilumi}_noSyst_forPrec --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-8 ; done




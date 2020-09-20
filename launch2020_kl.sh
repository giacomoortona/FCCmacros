#!/bin/bash

####No systs
#bbtahtal
for syst in 1 2 3 ; do for scen in I II III ; do for lwp in L M T ; do for bwp in L M T ; do combine -M MultiDimFit card1.00_bbtt_sel0_semilep_forComb_syst${syst}_${scen}_${bwp}${lwp}.txt --redefineSignalPOIs kl --algo grid --points 100 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters r,beffHH,beffSH,beffZ,beffTop,xsec_tt,xsec_ttH,xsec_HH,tauEff,lumi,jets_ID,lepton_ID,btag,xsec_HH,paramL,paramL2 -n 1.00_bbtl_btag_${syst}_${scen}${lwp}${bwp}_noSyst --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 --fastScan; done ; done ; done ; done 

#bbtautau comb
for syst in 1 2 3 ; do for scen in I II III ; do for lwp in L M T ; do for bwp in L M T ; do combine -M MultiDimFit cardbbttComb_syst${syst}_${scen}${bwp}${lwp}.txt --redefineSignalPOIs kl --algo grid --points 100 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters r,beffHH,beffSH,beffZ,beffTop,xsec_tt,xsec_ttH,xsec_HH,tauEff,lumi,jets_ID,lepton_ID,btag,xsec_HH,paramL,paramL2,paramH,paramH2 -n 1.00_bbttcomb_btag_${syst}_${scen}${lwp}${bwp}_noSyst --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 --fastScan; done ; done ; done ; done 

#bbaa
for syst in 1 2 3 ; do for scen in I II III ; do for pwp in M T ; do for bwp in L M T ; do combine -M MultiDimFit card1.00_syst${syst}_sel0_${scen}_${bwp}${pwp}.txt --redefineSignalPOIs kl --algo grid --points 100 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters r,beffGJ,beffHH,beffSH,xsec_tt,xsec_ttH,xsec_QCD,xsec_Zbb,gamma_ID,lumi,jets_ID,btagaa,xsec_HH,BkgScaler_bbaa -n 1.00_bbaa_btag_${syst}_${scen}${pwp}${bwp}_noSyst --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 --fastScan; done ; done ; done ; done 

#bbtahtah
for syst in 1 2 3 ; do for scen in I II III ; do for lwp in L M T ; do for bwp in L M T ; do combine -M MultiDimFit card1.00_bbtt_sel0_forComb_syst${syst}_${scen}_${bwp}${lwp}.txt --redefineSignalPOIs kl --algo grid --points 100 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters r,beffHH,beffSH,beffZ,beffTop,xsec_tt,xsec_ttH,xsec_HH,tauEff,lumi,jets_ID,btag,xsec_HH,paramH,paramH2 -n 1.00_bbtt_btag_${syst}_${scen}${lwp}${bwp}_noSyst --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 --fastScan; done ; done ; done ; done 

#4b
for syst in 1 2 3 ; do for scen in I II III ; do for bwp in L M T ; do combine -M MultiDimFit card1.00_boosted_syst${syst}_sel0_${scen}_${bwp}.txt --redefineSignalPOIs kl --algo grid --points 100 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters r,beffZ,beffTop,beffQCD,beffHH,beffSH,xsec_tt,xsec_ttH,xsec_QCD,xsec_Zbb,lumi,btagbb,xsec_HH -n 1.00_bbbb_btag_${syst}_${scen}${bwp}_noSyst --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 --fastScan; done ; done ; done  

#comb
for syst in 1 2 3 ; do for scen in I II III ; do for pwp in M T ; do for bwp in L M T ; do for lwp in L M T ; do combine -M MultiDimFit cardComb_syst${syst}_${scen}${pwp}${bwp}${lwp}.root --redefineSignalPOIs kl --algo grid --points 100 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters r,beffHH,beffSH,beffZ,beffTop,xsec_tt,xsec_ttH,xsec_HH,tauEff,lumi,jets_ID,lepton_ID,btag,xsec_HH,paramL,paramL2,paramH,paramH2,beffGJ,xsec_Zbb,gamma_ID,btagaa,BkgScaler_bbaa,beffQCD,btagbb -n 1.00_comb_${syst}_${scen}${pwp}${bwp}${lwp}_noSyst --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7  --fastScan; done ; done ; done ; done ; done

#combAll
for syst in 1 2 3 ; do for scen in I II III ; do for pwp in M T ; do for bwpgamma in L M T ; do for bwptau in L M T ; do for bwpb in L M T ; do for lwp in L M T ; do combine -M MultiDimFit cardComb_syst${syst}_${scen}${pwp}${bwpgamma}${bwptau}${bwpb}${lwp}.root --redefineSignalPOIs kl --algo grid --points 100 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters r,beffHH,beffSH,beffZ,beffTop,xsec_tt,xsec_ttH,xsec_HH,tauEff,lumi,jets_ID,lepton_ID,btag,xsec_HH,paramL,paramL2,paramH,paramH2,beffGJ,xsec_Zbb,gamma_ID,btagaa,BkgScaler_bbaa,beffQCD,btagbb -n 1.00_comb_${syst}_${scen}${pwp}${bwpgamma}${bwptau}${bwpb}${lwp}_noSyst --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 --fastScan ; done ; done ; done ; done ; done ; done ; done



####Systs
#comb
for syst in 1 2 3 ; do for scen in I II III ; do for pwp in M T ; do for bwp in L M T ; do for lwp in L M T ; do combine -M MultiDimFit cardComb_syst${syst}_${scen}${pwp}${bwp}${lwp}.root --redefineSignalPOIs kl --algo grid --points 100 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,jets_ID,param0,param1,param2,param3,paramL,paramH,paramL2,paramH2,lumiScaler,r,btag -n 1.00_comb_${syst}_${scen}${pwp}${bwp}${lwp} --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7  ; done ; done ; done ; done ; done

#bbaa
for syst in 1 2 3 ; do for scen in I II III ; do for pwp in M T ; do for bwp in L M T ; do combine -M MultiDimFit card1.00_syst${syst}_sel0_${scen}_${bwp}${pwp}.txt --redefineSignalPOIs kl --algo grid --points 100 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,jets_ID,param0,param1,param2,param3,paramL,paramH,paramL2,paramH2,lumiScaler,r,btag -n 1.00_bbaa_btag_${syst}_${scen}${pwp}${bwp} --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 ; done ; done ; done ; done 

#4b
for syst in 1 2 3 ; do for scen in I II III ; do for bwp in L M T ; do combine -M MultiDimFit card1.00_boosted_syst${syst}_sel0_${scen}_${bwp}.txt --redefineSignalPOIs kl --algo grid --points 100 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,jets_ID,param0,param1,param2,param3,paramL,paramH,paramL2,paramH2,lumiScaler,r,btag -n 1.00_bbbb_btag_${syst}_${scen}${bwp} --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 ; done ; done ; done  

#bbtahtah
for syst in 1 2 3 ; do for scen in I II III ; do for lwp in L M T ; do for bwp in L M T ; do combine -M MultiDimFit card1.00_bbtt_sel0_forComb_syst${syst}_${scen}_${bwp}${lwp}.txt --redefineSignalPOIs kl --algo grid --points 100 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,jets_ID,param0,param1,param2,param3,paramL,paramH,paramL2,paramH2,lumiScaler,r,btag -n 1.00_bbtt_btag_${syst}_${scen}${lwp}${bwp} --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 ; done ; done ; done ; done 

#bbtahtal
for syst in 1 2 3 ; do for scen in I II III ; do for lwp in L M T ; do for bwp in L M T ; do combine -M MultiDimFit card1.00_bbtt_sel0_semilep_forComb_syst${syst}_${scen}_${bwp}${lwp}.txt --redefineSignalPOIs kl --algo grid --points 100 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,jets_ID,param0,param1,param2,param3,paramL,paramH,paramL2,paramH2,lumiScaler,r,btag -n 1.00_bbtl_btag_${syst}_${scen}${lwp}${bwp} --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 ; done ; done ; done ; done 

#bbtautau comb
for syst in 1 2 3 ; do for scen in I II III ; do for lwp in L M T ; do for bwp in L M T ; do combine -M MultiDimFit cardbbttComb_syst${syst}_${scen}${bwp}${lwp}.txt --redefineSignalPOIs kl --algo grid --points 100 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,jets_ID,param0,param1,param2,param3,paramL,paramH,paramL2,paramH2,lumiScaler,r,btag -n 1.00_bbttcomb_btag_${syst}_${scen}${lwp}${bwp} --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 ; done ; done ; done ; done 

#combAll
for syst in 1 2 3 ; do for scen in I II III ; do for pwp in M T ; do for bwpgamma in L M T ; do for bwptau in L M T ; do for bwpb in L M T ; do for lwp in L M T ; do combine -M MultiDimFit cardComb_syst${syst}_${scen}${pwp}${bwpgamma}${bwptau}${bwpb}${lwp}.root --redefineSignalPOIs kl --algo grid --points 100 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,jets_ID,param0,param1,param2,param3,paramL,paramH,paramL2,paramH2,lumiScaler,r,btag -n 1.00_comb_${syst}_${scen}${pwp}${bwpgamma}${bwptau}${bwpb}${lwp} --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7  ; done ; done ; done ; done ; done ; done ; done



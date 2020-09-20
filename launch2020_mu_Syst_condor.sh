#!/bin/bash
#stuff to run on condor
cd /afs/cern.ch/user/g/gortona/work/FCCmacros/CMSSW_10_2_13/src
eval $(scram ru -sh)
cmsenv
cd /afs/cern.ch/user/g/gortona/work/FCCmacros/

export scen=$1
export syst=$2

####Systs
#bbaa
for pwp in M T ; do for bwp in M T ; do combine -M MultiDimFit card1.00_syst${syst}_sel0_${scen}_${bwp}${pwp}.txt --algo grid --points 500 --rMax 4 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,lumiScaler,kl,beffGJ -n 1.00_bbaa_btag_${syst}_${scen}${pwp}${bwp}_mu --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 ; done ; done ; 

#4b
for bwp in M T ; do combine -M MultiDimFit card1.00_boosted_syst${syst}_sel0_${scen}_${bwp}.txt --algo grid --points 500 --rMax 4 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,lumiScaler,kl,beffQCD -n 1.00_bbbb_btag_${syst}_${scen}${bwp}_mu --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 ; done ;  

#bbtahtah
for lwp in M T ; do for bwp in M T ; do combine -M MultiDimFit card1.00_bbtt_sel0_forComb_syst${syst}_${scen}_${bwp}${lwp}.txt --algo grid --points 500 --rMax 4 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,lumiScaler,kl -n 1.00_bbtt_btag_${syst}_${scen}${lwp}${bwp}_mu --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 ; done ; done ; 

#bbtahtal
for lwp in M T ; do for bwp in M T ; do combine -M MultiDimFit card1.00_bbtt_sel0_semilep_forComb_syst${syst}_${scen}_${bwp}${lwp}.txt --algo grid --points 500 --rMax 4 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,lumiScaler,kl -n 1.00_bbtl_btag_${syst}_${scen}${lwp}${bwp}_mu --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 ; done ; done ; 

#bbtautau comb
for lwp in M T ; do for bwp in M T ; do combine -M MultiDimFit cardbbttComb_syst${syst}_${scen}${bwp}${lwp}.txt --algo grid --points 500 --rMax 4 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,lumiScaler,kl -n 1.00_bbttcomb_btag_${syst}_${scen}${lwp}${bwp}_mu --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 ; done ; done ; 

#combAll
for pwp in M T ; do for bwpgamma in M T ; do for bwptau in M T ; do for bwpb in M T ; do for lwp in M T ; do combine -M MultiDimFit cardComb_syst${syst}_${scen}${pwp}${bwpgamma}${bwptau}${bwpb}${lwp}.root --algo grid --points 500 --rMax 4 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,param0,param1,param2,param3,lumiScaler,kl,beffQCD,beffGJ -n 1.00_comb_${syst}_${scen}${pwp}${bwpgamma}${bwptau}${bwpb}${lwp}_mu --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7  ; done ; done ; done ; done ; done ;



# #da tenere
# beffHH 
# beffQCD
# beffSH 
# beffTop
# beffZ
# gamma_ID
# jets_ID
# lepton_ID
# lumi
# tauEff 
# xsec_HH
# xsec_Zbb
# xsec_tt
# xsec_ttH
# beffGJ        param  0 1 [-3,3]
# 
# #da togliere
# btag
# btagaa
# btagbb
# xsec_QCD
# BkgScaler_bbaa  rateParam bbgg jgjj 1.0  
# param0 extArg 945.911
# param3 extArg 0.002063749213
# param2 extArg 109.963
# param1 extArg 571.319
# 


#
#for pwp in M T ; do for bwp in L M T ; do combine -M MultiDimFit card1.00_syst${syst}_sel0_${scen}_${bwp}${pwp}.txt --algo grid --points 500 --rMax 4 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,jets_ID,param0,param1,param2,param3,lumiScaler,kl,btag -n 1.00_bbaa_btag_${syst}_${scen}${pwp}${bwp}_mu --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 ; done ; done ; 
#
##4b
#for bwp in L M T ; do combine -M MultiDimFit card1.00_boosted_syst${syst}_sel0_${scen}_${bwp}.txt --algo grid --points 500 --rMax 4 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,jets_ID,param0,param1,param2,param3,lumiScaler,kl,btag -n 1.00_bbbb_btag_${syst}_${scen}${bwp}_mu --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 ; done ;  
#
##bbtahtah
#for lwp in L M T ; do for bwp in L M T ; do combine -M MultiDimFit card1.00_bbtt_sel0_forComb_syst${syst}_${scen}_${bwp}${lwp}.txt --algo grid --points 500 --rMax 4 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,jets_ID,param0,param1,param2,param3,lumiScaler,kl,btag -n 1.00_bbtt_btag_${syst}_${scen}${lwp}${bwp}_mu --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 ; done ; done ; 
#
##bbtahtal
#for lwp in L M T ; do for bwp in L M T ; do combine -M MultiDimFit card1.00_bbtt_sel0_semilep_forComb_syst${syst}_${scen}_${bwp}${lwp}.txt --algo grid --points 500 --rMax 4 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,jets_ID,param0,param1,param2,param3,lumiScaler,kl,btag -n 1.00_bbtl_btag_${syst}_${scen}${lwp}${bwp}_mu --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 ; done ; done ; 
#
##bbtautau comb
#for lwp in L M T ; do for bwp in L M T ; do combine -M MultiDimFit cardbbttComb_syst${syst}_${scen}${bwp}${lwp}.txt --algo grid --points 500 --rMax 4 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,jets_ID,param0,param1,param2,param3,lumiScaler,kl,btag -n 1.00_bbttcomb_btag_${syst}_${scen}${lwp}${bwp}_mu --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 ; done ; done ; 
#
##combAll
#for pwp in M T ; do for bwpgamma in L M T ; do for bwptau in L M T ; do for bwpb in L M T ; do for lwp in L M T ; do combine -M MultiDimFit cardComb_syst${syst}_${scen}${pwp}${bwpgamma}${bwptau}${bwpb}${lwp}.root --algo grid --points 500 --rMax 4 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters BkgScaler,BkgScaler_bbaa,jets_ID,param0,param1,param2,param3,lumiScaler,kl,btag -n 1.00_comb_${syst}_${scen}${pwp}${bwpgamma}${bwptau}${bwpb}${lwp}_mu --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7  ; done ; done ; done ; done ; done ;
#

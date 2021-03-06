#!/bin/bash

#stuff to run on condor
cd /afs/cern.ch/user/g/gortona/work/FCCmacros/CMSSW_10_2_13/src
eval $(scram ru -sh)
cmsenv
cd /afs/cern.ch/user/g/gortona/work/FCCmacros/

export scen=$1
export syst=$2


###
#signal strengths
####No systs
#bbtahtal
for lwp in M T ; do for bwp in M T ; do combine -M MultiDimFit card1.00_bbtt_sel0_semilep_forComb_syst${syst}_${scen}_${bwp}${lwp}.txt --algo grid --points 1000 --rMax 4 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters kl,beffHH,beffSH,beffZ,beffTop,xsec_tt,xsec_ttH,tauEff,lumi,lepton_ID,xsec_HH -n 1.00_bbtl_btag_${syst}_${scen}${lwp}${bwp}_noSyst_mu --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 --fastScan; done ; done ;

#bbtahtah
for lwp in M T ; do for bwp in M T ; do combine -M MultiDimFit card1.00_bbtt_sel0_forComb_syst${syst}_${scen}_${bwp}${lwp}.txt --algo grid --points 1000 --rMax 4 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters kl,beffHH,beffSH,beffZ,beffTop,xsec_tt,xsec_ttH,tauEff,lumi,xsec_HH -n 1.00_bbtt_btag_${syst}_${scen}${lwp}${bwp}_noSyst_mu --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 --fastScan; done ; done ;

#bbtautau comb
for lwp in M T ; do for bwp in M T ; do combine -M MultiDimFit cardbbttComb_syst${syst}_${scen}${bwp}${lwp}.txt --algo grid --points 1000 --rMax 4 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters kl,beffHH,beffSH,beffZ,beffTop,xsec_tt,xsec_ttH,tauEff,lumi,lepton_ID,xsec_HH -n 1.00_bbttcomb_btag_${syst}_${scen}${lwp}${bwp}_noSyst_mu --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 --fastScan; done ; done ;

#bbaa
for pwp in M T ; do for bwp in M T ; do combine -M MultiDimFit card1.00_syst${syst}_sel0_${scen}_${bwp}${pwp}.txt --algo grid --points 1000 --rMax 4 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters kl,beffGJ,beffHH,beffSH,xsec_tt,xsec_ttH,xsec_Zbb,gamma_ID,lumi,xsec_HH,BkgScaler_bbaa -n 1.00_bbaa_btag_${syst}_${scen}${pwp}${bwp}_noSyst_mu --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 --fastScan; done ; done ;

#4b
for bwp in M T ; do combine -M MultiDimFit card1.00_boosted_syst${syst}_sel0_${scen}_${bwp}.txt --algo grid --points 1000 --rMax 4 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters kl,beffZ,beffTop,beffQCD,beffHH,beffSH,xsec_tt,xsec_ttH,xsec_Zbb,lumi,xsec_HH -n 1.00_bbbb_btag_${syst}_${scen}${bwp}_noSyst_mu --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 --fastScan; done ; 

#combAll
for pwp in M T ; do for bwpgamma in M T ; do for bwptau in M T ; do for bwpb in M T ; do for lwp in M T ; do combine -M MultiDimFit cardComb_syst${syst}_${scen}${pwp}${bwpgamma}${bwptau}${bwpb}${lwp}.root --algo grid --points 1000 --rMax 4 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters kl,beffHH,beffSH,beffZ,beffTop,xsec_tt,xsec_ttH,tauEff,lumi,lepton_ID,xsec_HH,beffGJ,xsec_Zbb,gamma_ID,BkgScaler_bbaa,beffQCD,param0,param1,param2,param3 -n 1.00_comb_${syst}_${scen}${pwp}${bwpgamma}${bwptau}${bwpb}${lwp}_noSyst_mu --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 --fastScan ; done ; done ; done ; done ; done 


# 
# #bbtahtal
# for lwp in L M T ; do for bwp in L M T ; do combine -M MultiDimFit card1.00_bbtt_sel0_semilep_forComb_syst${syst}_${scen}_${bwp}${lwp}.txt --algo grid --points 1000 --rMax 4 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters kl,beffHH,beffSH,beffZ,beffTop,xsec_tt,xsec_ttH,xsec_HH,tauEff,lumi,jets_ID,lepton_ID,btag,xsec_HH,paramL2 -n 1.00_bbtl_btag_${syst}_${scen}${lwp}${bwp}_noSyst_mu --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 --fastScan; done ; done ;
# 
# #bbtautau comb
# for lwp in L M T ; do for bwp in L M T ; do combine -M MultiDimFit cardbbttComb_syst${syst}_${scen}${bwp}${lwp}.txt --algo grid --points 1000 --rMax 4 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters kl,beffHH,beffSH,beffZ,beffTop,xsec_tt,xsec_ttH,xsec_HH,tauEff,lumi,jets_ID,lepton_ID,btag,xsec_HH,paramH2 -n 1.00_bbttcomb_btag_${syst}_${scen}${lwp}${bwp}_noSyst_mu --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 --fastScan; done ; done ;
# 
# #bbaa
# for pwp in M T ; do for bwp in L M T ; do combine -M MultiDimFit card1.00_syst${syst}_sel0_${scen}_${bwp}${pwp}.txt --algo grid --points 1000 --rMax 4 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters kl,beffGJ,beffHH,beffSH,xsec_tt,xsec_ttH,xsec_QCD,xsec_Zbb,gamma_ID,lumi,jets_ID,btagaa,xsec_HH,BkgScaler_bbaa -n 1.00_bbaa_btag_${syst}_${scen}${pwp}${bwp}_noSyst_mu --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 --fastScan; done ; done ;
# 
# #bbtahtah
# for lwp in L M T ; do for bwp in L M T ; do combine -M MultiDimFit card1.00_bbtt_sel0_forComb_syst${syst}_${scen}_${bwp}${lwp}.txt --algo grid --points 1000 --rMax 4 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters kl,beffHH,beffSH,beffZ,beffTop,xsec_tt,xsec_ttH,xsec_HH,tauEff,lumi,jets_ID,btag,xsec_HH,paramH2 -n 1.00_bbtt_btag_${syst}_${scen}${lwp}${bwp}_noSyst_mu --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 --fastScan; done ; done ;
# 
# #4b
# for bwp in L M T ; do combine -M MultiDimFit card1.00_boosted_syst${syst}_sel0_${scen}_${bwp}.txt --algo grid --points 1000 --rMax 4 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters kl,beffZ,beffTop,beffQCD,beffHH,beffSH,xsec_tt,xsec_ttH,xsec_QCD,xsec_Zbb,lumi,btagbb,xsec_HH -n 1.00_bbbb_btag_${syst}_${scen}${bwp}_noSyst_mu --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 --fastScan; done ; 
# 
# #combAll
# for pwp in M T ; do for bwpgamma in L M T ; do for bwptau in L M T ; do for bwpb in L M T ; do for lwp in L M T ; do combine -M MultiDimFit cardComb_syst${syst}_${scen}${pwp}${bwpgamma}${bwptau}${bwpb}${lwp}.root --algo grid --points 1000 --rMax 4 --setParameterRanges kl=0.7,1.3 -t -1 --setParameters kl=1.0,BkgScaler_bbaa=1.0,r=1.0,BkgScaler=1.0 --freezeParameters kl,beffHH,beffSH,beffZ,beffTop,xsec_tt,xsec_ttH,xsec_HH,tauEff,lumi,jets_ID,lepton_ID,btag,xsec_HH,beffGJ,xsec_Zbb,gamma_ID,btagaa,BkgScaler_bbaa,beffQCD,btagbb -n 1.00_comb_${syst}_${scen}${pwp}${bwpgamma}${bwptau}${bwpb}${lwp}_noSyst_mu --robustFit=1 --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:1.0 --cminFallbackAlgo Minuit2,Migrad,1:1.0 --cminFallbackAlgo Minuit2,Migrad,0:5.0 --cminApproxPreFitTolerance=100 --X-rtd MINIMIZER_MaxCalls=9999999 --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --cminDefaultMinimizerPrecision 1E-7 --fastScan ; done ; done ; done ; done ; done 
# 


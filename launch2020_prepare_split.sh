#!/bin/bash

#1 -> scen #I II III
#2 -> syst # 1 2 3
#3 -> bwpb # LMT
#4 -> bwpg # LMT
#5 -> bwpt # LMT
#6 -> pwp #MT
#7 -> lwp #LMT

# assume bwpb == bwp generic

#stuff to run on condor
cd /afs/cern.ch/user/g/gortona/work/FCCmacros/CMSSW_10_2_13/src
eval $(scram ru -sh)
cmsenv
cd /afs/cern.ch/user/g/gortona/work/FCCmacros/
## 
# prepare cards
python cardMaker.py -s ${2} -F "_${1}_${4}${6}" -w 1.0
python cardMaker.py -s ${2} -F "_${1}_${3}" -w 1.0 -t boosted 
python cardMaker_bbtautau.py -x ${2} -F "_${1}_${5}${7}" -c
python cardMaker_bbtautau.py -x ${2} -F "_${1}_${5}${7}" -c -l

# #comb all same bwp (bwpb)
# combineCards.py -S bbtahtah=card1.00_bbtt_sel0_forComb_syst${2}_${1}_${3}${7}.txt bbtahtal=card1.00_bbtt_sel0_semilep_forComb_syst${2}_${1}_${3}${7}.txt bb4l=card1.00_bb4l_syst${2}.txt bbgg=card1.00_syst${2}_sel0_${1}_${3}${6}.txt bbbb=card1.00_boosted_syst${2}_sel0_${1}_${3}.txt > cardComb_syst${2}_${1}${6}${3}${7}.txt
# text2workspace.py cardComb_syst${2}_${1}${6}${3}${7}.txt

# comb bbtautau
combineCards.py -S bbtahtah=card1.00_bbtt_sel0_forComb_syst${2}_${1}_${5}${7}.txt bbtahtal=card1.00_bbtt_sel0_semilep_forComb_syst${2}_${1}_${5}${7}.txt  > cardbbttComb_syst${2}_${1}${5}${7}.txt 
text2workspace.py cardbbttComb_syst${2}_${1}${5}${7}.txt 

#comb all options
combineCards.py -S bbtahtah=card1.00_bbtt_sel0_forComb_syst${2}_${1}_${5}${7}.txt bbtahtal=card1.00_bbtt_sel0_semilep_forComb_syst${2}_${1}_${5}${7}.txt bb4l=card1.00_bb4l_syst${2}.txt bbgg=card1.00_syst${2}_sel0_${1}_${4}${6}.txt bbbb=card1.00_boosted_syst${2}_sel0_${1}_${3}.txt > cardComb_syst${2}_${1}${6}${4}${5}${3}${7}.txt
text2workspace.py cardComb_syst${2}_${1}${6}${4}${5}${3}${7}.txt 



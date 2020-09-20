#!/bin/bash

#stuff to run on condor
cd /afs/cern.ch/user/g/gortona/work/FCCmacros/CMSSW_10_2_13/src
eval $(scram ru -sh)
cmsenv
cd /afs/cern.ch/user/g/gortona/work/FCCmacros/

#prepare cards
for syst in 1 2 3 ; do for sc in I II III ; do for bwp in M T ; do python cardMaker.py -s $syst -F "_${sc}_${bwp}" -w 1.0 -t boosted ; done ; for bwp in M T ; do for pwp in M T ; do python cardMaker_bbtautau.py -x $syst -F "_${sc}_${bwp}${pwp}" -c ; done ; done ; for bwp in M T ; do for pwp in M T ; do python cardMaker_bbtautau.py -x $syst -F "_${sc}_${bwp}${pwp}" -c -l ; done ; done ; for bwp in M T ; do for pwp in M T ; do python cardMaker.py -s $syst -F "_${sc}_${bwp}${pwp}" -w 1.0 ; done ; done ; done ; done ;


for syst in 1 2 3 ; do for scen in I II III ; do for pwp in M T ; do for bwp in M T ; do for lwp in M T ; do combineCards.py -S bbtahtah=card1.00_bbtt_sel0_forComb_syst${syst}_${scen}_${bwp}${lwp}.txt bbtahtal=card1.00_bbtt_sel0_semilep_forComb_syst${syst}_${scen}_${bwp}${lwp}.txt bb4l=card1.00_bb4l_syst${syst}.txt bbgg=card1.00_syst${syst}_sel0_${scen}_${bwp}${pwp}.txt bbbb=card1.00_boosted_syst${syst}_sel0_${scen}_${bwp}.txt > cardComb_syst${syst}_${scen}${pwp}${bwp}${lwp}.txt ; done ; done ; done ; done ; done

for syst in 1 2 3 ; do for scen in I II III ; do for pwp in M T ; do for bwp in M T ; do for lwp in M T ; do text2workspace.py cardComb_syst${syst}_${scen}${pwp}${bwp}${lwp}.txt ; done ; done ; done ; done ; done

for syst in 1 2 3 ; do for scen in I II III ; do for bwp in M T ; do for lwp in M T ; do combineCards.py -S bbtahtah=card1.00_bbtt_sel0_forComb_syst${syst}_${scen}_${bwp}${lwp}.txt bbtahtal=card1.00_bbtt_sel0_semilep_forComb_syst${syst}_${scen}_${bwp}${lwp}.txt  > cardbbttComb_syst${syst}_${scen}${bwp}${lwp}.txt ; done ; done ; done ; done 

for syst in 1 2 3 ; do for scen in I II III ; do for bwp in M T ; do for lwp in M T ; do text2workspace.py cardbbttComb_syst${syst}_${scen}${bwp}${lwp}.txt ; done ; done ; done ; done

#prepare combAll
#for syst in 1 2 3 ; do for sc in I II III ; do for bwp in M T ; do python cardMaker.py -s $syst -F "_${sc}_${bwp}" -w 1.0 -t boosted ; done ; for bwp in M T ; do for pwp in M T ; do python cardMaker_bbtautau.py -x $syst -F "_${sc}_${bwp}${pwp}" -c ; done ; done ; for bwp in M T ; do for pwp in M T ; do python cardMaker_bbtautau.py -x $syst -F "_${sc}_${bwp}${pwp}" -c -l ; done ; done ; for bwp in M T ; do for pwp in M T ; do python cardMaker.py -s $syst -F "_${sc}_${bwp}${pwp}" -w 1.0 ; done ; done ; done ; done ;


for syst in 1 2 3 ; do for scen in I II III ; do for pwp in M T ; do for bwpgamma in M T ; do for bwptau in M T ; do for bwpb in M T ; do for lwp in M T ; do combineCards.py -S bbtahtah=card1.00_bbtt_sel0_forComb_syst${syst}_${scen}_${bwptau}${lwp}.txt bbtahtal=card1.00_bbtt_sel0_semilep_forComb_syst${syst}_${scen}_${bwptau}${lwp}.txt bb4l=card1.00_bb4l_syst${syst}.txt bbgg=card1.00_syst${syst}_sel0_${scen}_${bwpgamma}${pwp}.txt bbbb=card1.00_boosted_syst${syst}_sel0_${scen}_${bwpb}.txt > cardComb_syst${syst}_${scen}${pwp}${bwpgamma}${bwptau}${bwpb}${lwp}.txt ; done ; done ; done ; done ; done ; done ; done

for syst in 1 2 3 ; do for scen in I II III ; do for pwp in M T ; do for bwpgamma in M T ; do for bwptau in M T ; do for bwpb in M T ; do for lwp in M T ; do text2workspace.py cardComb_syst${syst}_${scen}${pwp}${bwpgamma}${bwptau}${bwpb}${lwp}.txt ; done ; done ; done ; done ; done ;done ; done


# 
# 
# for syst in 1 2 3 ; do for sc in I II III ; do for bwp in L M T ; do python cardMaker.py -s $syst -F "_${sc}_${bwp}" -w 1.0 -t boosted ; done ; for bwp in L M T ; do for pwp in L M T ; do python cardMaker_bbtautau.py -x $syst -F "_${sc}_${bwp}${pwp}" -c ; done ; done ; for bwp in L M T ; do for pwp in L M T ; do python cardMaker_bbtautau.py -x $syst -F "_${sc}_${bwp}${pwp}" -c -l ; done ; done ; for bwp in L M T ; do for pwp in M T ; do python cardMaker.py -s $syst -F "_${sc}_${bwp}${pwp}" -w 1.0 ; done ; done ; done ; done ;
# 
# 
# for syst in 1 2 3 ; do for scen in I II III ; do for pwp in M T ; do for bwp in L M T ; do for lwp in L M T ; do combineCards.py -S bbtahtah=card1.00_bbtt_sel0_forComb_syst${syst}_${scen}_${bwp}${lwp}.txt bbtahtal=card1.00_bbtt_sel0_semilep_forComb_syst${syst}_${scen}_${bwp}${lwp}.txt bb4l=card1.00_bb4l_syst${syst}.txt bbgg=card1.00_syst${syst}_sel0_${scen}_${bwp}${pwp}.txt bbbb=card1.00_boosted_syst${syst}_sel0_${scen}_${bwp}.txt > cardComb_syst${syst}_${scen}${pwp}${bwp}${lwp}.txt ; done ; done ; done ; done ; done
# 
# for syst in 1 2 3 ; do for scen in I II III ; do for pwp in M T ; do for bwp in L M T ; do for lwp in L M T ; do text2workspace.py cardComb_syst${syst}_${scen}${pwp}${bwp}${lwp}.txt ; done ; done ; done ; done ; done
# 
# for syst in 1 2 3 ; do for scen in I II III ; do for bwp in L M T ; do for lwp in L M T ; do combineCards.py -S bbtahtah=card1.00_bbtt_sel0_forComb_syst${syst}_${scen}_${bwp}${lwp}.txt bbtahtal=card1.00_bbtt_sel0_semilep_forComb_syst${syst}_${scen}_${bwp}${lwp}.txt  > cardbbttComb_syst${syst}_${scen}${bwp}${lwp}.txt ; done ; done ; done ; done 
# 
# for syst in 1 2 3 ; do for scen in I II III ; do for bwp in L M T ; do for lwp in L M T ; do text2workspace.py cardbbttComb_syst${syst}_${scen}${bwp}${lwp}.txt ; done ; done ; done ; done
# 
# #prepare combAll
# #for syst in 1 2 3 ; do for sc in I II III ; do for bwp in L M T ; do python cardMaker.py -s $syst -F "_${sc}_${bwp}" -w 1.0 -t boosted ; done ; for bwp in L M T ; do for pwp in L M T ; do python cardMaker_bbtautau.py -x $syst -F "_${sc}_${bwp}${pwp}" -c ; done ; done ; for bwp in L M T ; do for pwp in L M T ; do python cardMaker_bbtautau.py -x $syst -F "_${sc}_${bwp}${pwp}" -c -l ; done ; done ; for bwp in L M T ; do for pwp in M T ; do python cardMaker.py -s $syst -F "_${sc}_${bwp}${pwp}" -w 1.0 ; done ; done ; done ; done ;
# 
# 
# for syst in 1 2 3 ; do for scen in I II III ; do for pwp in M T ; do for bwpgamma in L M T ; do for bwptau in L M T ; do for bwpb in L M T ; do for lwp in L M T ; do combineCards.py -S bbtahtah=card1.00_bbtt_sel0_forComb_syst${syst}_${scen}_${bwptau}${lwp}.txt bbtahtal=card1.00_bbtt_sel0_semilep_forComb_syst${syst}_${scen}_${bwptau}${lwp}.txt bb4l=card1.00_bb4l_syst${syst}.txt bbgg=card1.00_syst${syst}_sel0_${scen}_${bwpgamma}${pwp}.txt bbbb=card1.00_boosted_syst${syst}_sel0_${scen}_${bwpb}.txt > cardComb_syst${syst}_${scen}${pwp}${bwpgamma}${bwptau}${bwpb}${lwp}.txt ; done ; done ; done ; done ; done ; done ; done
# 
# for syst in 1 2 3 ; do for scen in I II III ; do for pwp in M T ; do for bwpgamma in L M T ; do for bwptau in L M T ; do for bwpb in L M T ; do for lwp in L M T ; do text2workspace.py cardComb_syst${syst}_${scen}${pwp}${bwpgamma}${bwptau}${bwpb}${lwp}.txt ; done ; done ; done ; done ; done ;done ; done
# 
# 

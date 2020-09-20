from ROOT import *
import os,re, optparse
from outRatesbbtahtah import getRatebbtahtah
from outRatesbbtahtal import getRatebbtahtal
# dovrei aggiustare hobs

def getScenario(folderName):
	if "III" in folderName: return "III"
	elif "II" in folderName: return "II"
	else : return "I"

def getLwP(folderName):
	if "LL" in folderName: return "L"
	if "LM" in folderName: return "M"
	elif "LT" in folderName: return "T"
	elif "ML" in folderName: return "L"
	elif "MM" in folderName: return "M"
	elif "MT" in folderName: return "T"
	elif "TL" in folderName: return "L"
	elif "TM" in folderName: return "M"
	elif "TT" in folderName: return "T"
	else : return "CIAO"

def getBwP(folderName):
	if "_L" in folderName: return "L"
	elif "_M" in folderName: return "M"
	elif "_T" in folderName: return "T"
	else : return "CIAO"


def getLinearCoeff(sel,tipo,version):
	coeff_sl_v1 = [
	-0.6551,
	-0.7793,
	-0.7793,
	-0.7903,
	-0.7857,
	-0.7029,
	-0.5955,
	-0.5752,
	-0.5716
	]
	coeff_fh_v0 =[
	-0.6833,
	-0.6424
	]
	coeff_fh_v1 = [
	-0.7158,
	-0.6618,
	-0.6618,
	-0.6168,
	-0.6757,
	-0.6126,
	-0.6154,
	-0.6079,
	-0.5961
	]
	coeff_sl_v2 = [
-0.6651,
-0.7793,
-0.7793,
-0.7903,
-0.7857,
-0.7029,
-0.5955,
-0.5762,
-0.5716
	]
	coeff_fh_v2 = [
-0.6874,
-0.6355,
-0.6355,
-0.5924,
-0.649,
-0.5884,
-0.5912,
-0.5841,
-0.5731	]
	coeff_fh_v3 = [
-0.4894, #v5 updated
-0.5893, #v1 updated 
-0.6286, #v1 updated
-0.5924,
-0.649,
-0.5884,
-0.5912,
-0.5841,
-0.5731	]
	coeff_sl_v3 = [
-0.37 #v5 updated
	]

	if (version == 0) : 
		return coeff_fh_v0[sel]
	elif version == 1: 
		if tipo == 0 :
			if sel>8 : return coeff_fh_v1[8]
			else : return coeff_fh_v1[sel]
		else :
			if sel>8 : return coeff_sl_v1[8]
			else : return coeff_sl_v1[sel]
	elif version == 2 :
		if tipo == 0 :
			if sel>8 : return coeff_fh_v2[8]
			else : return coeff_fh_v2[sel]
		else :
			if sel>8 : return coeff_sl_v2[8]
			else : return coeff_sl_v2[sel]
	else :
		if tipo == 0 :
			if sel>8 : return coeff_fh_v3[8]
			else : return coeff_fh_v3[sel] #sto usando lo stesso per semilep e fh perche semilep fa schifo
		else :
			return coeff_sl_v3[0]

def createDict():
	dd ={}
	channel            =[    "ch1"       ,    "ch1"       ,    "ch1"       ,    "ch1"       ,    "ch1"       ,   "ch1"       ,   "ch1"       ,   "ch2"       ,   "ch2"       ,  "ch2"       ,    "ch2"       ,    "ch2"       ,    "ch2"       ,    "ch2"       ,    "ch3"       ,    "ch3"       ,    "ch3"       ,    "ch3"       ,    "ch3"       ,    "ch4"       ,    "ch4"       ,    "ch4"       ,    "ch4"       ,    "ch4"      ,    "ch4"       ,    "ch5"         ,    "ch5"      ,    "ch5"       ,    "ch5"     , "ch5"     , "ch5"  ]
	process            =[    "HH"        ,  "zjets"       , "singleH"      ,  "ttbar"       ,   "ZZ"         ,   "ttV"       ,  "ttVV"       ,   "ttV"       ,  "ttVV"       ,  "HH"        ,   "zjets"      ,  "singleH"     ,   "ttbar"      ,  "ZZ"          , "HH"           ,   "ttZ"        ,  "ttH"         ,    "ZH"         , "bbH"         ,  "HH"          ,  "VH"          ,  "jgjj"        ,  "ttH"         ,  "ggjj"       ,  "singleH"     ,    "HH"          ,    "ZZ"       ,     "Zbb"      ,    "QCD"     , "singleH" , "ttbar"]
	xsec_tt_opt        =[    "-"         ,    "-"         ,    "-"         ,    "1.005"     ,    "-"         ,   "1.005"     ,   "1.005"     ,   "1.005"     ,   "1.005"     ,  "-"         ,    "-"         ,   "-"          ,  "1.005"       ,    "-"         ,    "-"         ,   "1.005"      ,   "-"          ,   "-"          ,   "-"          ,   "-"          ,   "-"          ,   "-"          ,   "-"          ,    "-"        ,    "-"         ,    "-"           ,    "-"        ,    "-"         ,     "-"       , "-"       , "1.005"]
	xsec_tt_int        =[     "-"        ,     "-"        ,    "-"         ,    "1.010"     ,     "-"        ,   "1.010"     ,   "1.010"     ,   "1.010"     ,   "1.010"     ,  "-"         ,     "-"        ,   "-"          ,    "1.010"     ,     "-"        ,     "-"        ,   "1.010"      ,  "-"           ,   "-"          ,     "-"        ,    "-"         ,     "-"        ,    "-"         ,    "-"         ,    "-"        ,     "-"        ,      "-"         ,      "-"      ,    "-"         ,     "-"      , "-"       , "1.010"]
	xsec_tt_pes        =[     "-"        ,     "-"        ,    "-"         ,    "1.015"     ,     "-"        ,   "1.015"     ,   "1.015"     ,   "1.015"     ,   "1.015"     ,  "-"         ,     "-"        ,   "-"          ,    "1.015"     ,     "-"        ,     "-"        ,   "1.015"      ,  "-"           ,   "-"          ,     "-"        ,    "-"         ,     "-"        ,    "-"         ,    "-"         ,    "-"        ,     "-"        ,      "-"         ,      "-"      ,    "-"         ,     "-"      , "-"       , "1.015"]

	xsec_ttH_opt       =[     "-"        ,    "-"         ,    "1.005"     ,    "-"         ,    "-"         ,   "-"         ,   "-"         ,   "-"         ,   "-"         ,  "-"         ,    "-"         ,   "1.005"      ,  "-"           ,    "-"         ,    "-"         ,   "-"          ,  "1.005"       ,   "1.005"       ,   "1.005"      ,   "-"          ,   "1.005"     ,   "-"	  	    ,   "1.005"      ,    "-"        ,    "1.005"     ,    "-"           ,    "-"        ,    "-"         ,    "-"       , "1.005"   , "-"    ]
	xsec_ttH_int       =[     "-"        ,     "-"        ,    "1.010"     ,     "-"        ,     "-"        ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "-"         ,     "-"        ,   "1.010"      ,    "-"         ,     "-"        ,     "-"        ,      "-"       ,  "1.010"       ,   "1.010"       ,   "1.010"      ,    "-"         ,   "1.010"     ,    "-"	        ,   "1.010"      ,    "-"        ,    "1.010"     ,      "-"         ,      "-"      ,    "-"         ,     "-"      , "1.010"   , "-"    ]
	xsec_ttH_pes       =[     "-"        ,     "-"        ,    "1.015"     ,     "-"        ,     "-"        ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "-"         ,     "-"        ,   "1.015"      ,    "-"         ,     "-"        ,     "-"        ,      "-"       ,  "1.015"       ,   "1.015"       ,   "1.015"      ,    "-"         ,   "1.015"     ,    "-"	        ,   "1.015"      ,    "-"        ,    "1.015"     ,      "-"         ,      "-"      ,    "-"         ,     "-"      , "1.015"   , "-"    ]

	xsec_QCD_opt       =[     "-"        ,    "-"         ,    "-"         ,     "-"        ,    "-"         ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "-"         ,    "-"         ,   "-"          ,  "-"           ,    "-"         ,    "-"         ,   "-"          ,  "-"           ,   "-"          ,    "-"         ,   "-"          ,   "-"          ,    "-"         ,   "-"          ,    "-"        ,    "-"         ,    "-"           ,    "-"        ,    "-"          ,    "-"      , "-"       , "-"    ]
	xsec_QCD_int       =[     "-"        ,     "-"        ,    "-"         ,     "-"        ,     "-"        ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "-"         ,     "-"        ,   "-"          ,    "-"         ,     "-"        ,     "-"        ,      "-"       ,  "-"           ,   "-"          ,     "-"        ,    "-"         ,     "-"        ,    "-"         ,    "-"         ,    "-"        ,     "-"        ,      "-"         ,      "-"      ,    "-"          ,    "-"      , "-"       , "-"    ]
	xsec_QCD_pes       =[     "-"        ,     "-"        ,    "-"         ,     "-"        ,     "-"        ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "-"         ,     "-"        ,   "-"          ,    "-"         ,     "-"        ,     "-"        ,      "-"       ,  "-"           ,   "-"          ,     "-"        ,    "-"         ,     "-"        ,    "-"         ,    "-"         ,    "-"        ,     "-"        ,      "-"         ,      "-"      ,    "-"          ,    "-"      , "-"       , "-"    ]

	xsec_Zbb_opt       =[     "-"        ,    "-"         ,    "-"         ,     "-"        ,    "-"         ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "-"         ,    "-"         ,   "-"          ,  "-"           ,    "-"         ,    "-"         ,   "-"          ,  "-"           ,   "-"          ,    "-"         ,   "-"          ,   "-"          ,    "-"         ,   "-"          ,    "-"        ,    "-"         ,    "-"           ,    "-"        ,    "1.01 "     ,    "-"        , "-"       , "-"    ]
	xsec_Zbb_int       =[     "-"        ,     "-"        ,    "-"         ,     "-"        ,     "-"        ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "-"         ,     "-"        ,   "-"          ,    "-"         ,     "-"        ,     "-"        ,      "-"       ,  "-"           ,   "-"          ,     "-"        ,    "-"         ,     "-"        ,    "-"         ,    "-"         ,    "-"        ,     "-"        ,      "-"         ,      "-"      ,    "1.02 "     ,     "-"       , "-"       , "-"    ]
	xsec_Zbb_pes       =[     "-"        ,     "-"        ,    "-"         ,     "-"        ,     "-"        ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "-"         ,     "-"        ,   "-"          ,    "-"         ,     "-"        ,     "-"        ,      "-"       ,  "-"           ,   "-"          ,     "-"        ,    "-"         ,     "-"        ,    "-"         ,    "-"         ,    "-"        ,     "-"        ,      "-"         ,      "-"      ,    "1.03 "     ,     "-"       , "-"       , "-"    ]

	xsec_ZZ_opt       =[     "-"        ,    "-"         ,    "-"         ,     "-"        ,     "1.005"        ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "-"         ,    "-"         ,   "-"          ,  "-"           ,    "1.005"         ,    "-"         ,   "-"          ,  "-"           ,   "-"          ,    "-"         ,   "-"          ,   "-"          ,    "-"         ,   "-"          ,    "-"        ,    "-"         ,    "-"           ,      "1.005"      ,    "-"     ,    "-"        , "-"       , "-"    ]
	xsec_ZZ_int       =[     "-"        ,     "-"        ,    "-"         ,     "-"        ,     "1.010"        ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "-"         ,     "-"        ,   "-"          ,    "-"         ,     "1.010"        ,     "-"        ,      "-"       ,  "-"           ,   "-"          ,     "-"        ,    "-"         ,     "-"        ,    "-"         ,    "-"         ,    "-"        ,     "-"        ,      "-"         ,      "1.010"      ,    "-"     ,     "-"       , "-"       , "-"    ]
	xsec_ZZ_pes       =[     "-"        ,     "-"        ,    "-"         ,     "-"        ,     "1.020"        ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "-"         ,     "-"        ,   "-"          ,    "-"         ,     "1.020"        ,     "-"        ,      "-"       ,  "-"           ,   "-"          ,     "-"        ,    "-"         ,     "-"        ,    "-"         ,    "-"         ,    "-"        ,     "-"        ,      "-"         ,      "1.020"      ,    "-"     ,     "-"       , "-"       , "-"    ]

	xsec_Zjets_opt    =[     "-"        ,     "1.01"      ,    "-"         ,     "-"        ,    "-"         ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "-"         ,     "1.01"    ,   "-"          ,  "-"           ,    "-"         ,    "-"         ,   "-"          ,  "-"           ,   "-"          ,    "-"         ,   "-"          ,   "-"          ,    "-"         ,   "-"          ,    "-"        ,    "-"         ,    "-"           ,      "1.005"      ,    "-"     ,    "-"        , "-"       , "-"    ]
	xsec_Zjets_int    =[     "-"        ,     "1.02"      ,    "-"         ,     "-"        ,     "-"        ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "-"         ,     "1.02"    ,   "-"          ,    "-"         ,     "-"        ,     "-"        ,      "-"       ,  "-"           ,   "-"          ,     "-"        ,    "-"         ,     "-"        ,    "-"         ,    "-"         ,    "-"        ,     "-"        ,      "-"         ,      "1.010"      ,    "-"     ,     "-"       , "-"       , "-"    ]
	xsec_Zjets_pes    =[     "-"        ,     "1.03"      ,    "-"         ,     "-"        ,     "-"        ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "-"         ,     "1.03"    ,   "-"          ,    "-"         ,     "-"        ,     "-"        ,      "-"       ,  "-"           ,   "-"          ,     "-"        ,    "-"         ,     "-"        ,    "-"         ,    "-"         ,    "-"        ,     "-"        ,      "-"         ,      "1.020"      ,    "-"     ,     "-"       , "-"       , "-"    ]
#0.5/1/2 x gamma
	gamma_ID_opt       =[     "-"        ,    "-"         ,    "-"         ,     "-"        ,    "-"         ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "-"         ,    "-"         ,   "-"          ,  "-"           ,    "-"         ,    "-"         ,   "-"          ,  "-"           ,   "-"          ,    "-"         ,   "1.010"      ,   "-"          ,    "-"         ,    "-"         ,    "-"        ,	  "1.010"     ,    "-"           ,    "-"        ,    "-"         ,     "-" 	 , "-"       , "-"    ]
	gamma_ID_int       =[     "-"        ,     "-"        ,    "-"         ,     "-"        ,     "-"        ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "-"         ,     "-"        ,   "-"          ,    "-"         ,     "-"        ,     "-"        ,      "-"       ,  "-"           ,   "-"          ,     "-"        ,   "1.020"      ,   "-"          ,    "-"         ,    "-"         ,    "-" 	     ,	  "1.020"     ,      "-"         ,      "-"      ,    "-"         ,     "-"      , "-"       , "-"    ]
	gamma_ID_pes       =[     "-"        ,     "-"        ,    "-"         ,     "-"        ,     "-"        ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "-"         ,     "-"        ,   "-"          ,    "-"         ,     "-"        ,     "-"        ,      "-"       ,  "-"           ,   "-"          ,     "-"        ,   "1.040"      ,   "-"          ,    "-"         ,    "-"         ,    "-" 	     ,	  "1.040"     ,      "-"         ,      "-"      ,    "-"         ,     "-"      , "-"       , "-"    ]
#0.5/1/2 x gamma
	gamma_ID_bkg_opt   =[     "-"        ,    "-"         ,    "-"         ,     "-"        ,    "-"         ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "-"         ,    "-"         ,   "-"          ,  "-"           ,    "-"         ,    "-"         ,   "-"          ,  "-"           ,   "-"          ,    "-"         ,   "-"          ,   "-"          ,     "-"        ,     "-"        ,     "-"       ,	  "-"         ,    "-"           ,    "-"        ,    "-"         ,     "-" 	 , "-"       , "-"    ]
	gamma_ID_bkg_int   =[     "-"        ,     "-"        ,    "-"         ,     "-"        ,     "-"        ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "-"         ,     "-"        ,   "-"          ,    "-"         ,     "-"        ,     "-"        ,      "-"       ,  "-"           ,   "-"          ,     "-"        ,   "-"          ,   "-"          ,     "-"        ,     "-"        ,     "-" 	     ,	  "-"         ,      "-"         ,      "-"      ,    "-"         ,     "-"      , "-"       , "-"    ]
	gamma_ID_bkg_pes   =[     "-"        ,     "-"        ,    "-"         ,     "-"        ,     "-"        ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "-"         ,     "-"        ,   "-"          ,    "-"         ,     "-"        ,     "-"        ,      "-"       ,  "-"           ,   "-"          ,     "-"        ,   "-"          ,   "-"          ,     "-"        ,     "-"        ,     "-" 	     ,	  "-"         ,      "-"         ,      "-"      ,    "-"         ,     "-"      , "-"       , "-"    ]
#1/2/3.5 x tau
	tauEff_opt         =[     "1.01"     ,    "1.01 "     ,    "1.01 "     ,     "1.01"     ,    "1.01 "     ,    "1.01"     ,    "1.01"     ,    "1.020"    ,    "1.020"    ,  "1.020"     ,    "1.020"     ,   "1.020"      ,    "1.020"     ,    "1.020"     ,    "-"         ,   "-"          ,  "-"           ,   "-"          ,    "-"         ,   "-"          ,   "-"          ,    "-"         ,   "-"          ,    "-"        ,      "-"       ,    "-"           ,    "-"        ,    "-"         ,     "-"      , "-"       , "-"    ]
	tauEff_int         =[     "1.02 "    ,     "1.02 "    ,  "1.02 "       ,     "1.02"     ,     "1.02 "    ,    "1.02"     ,    "1.02"     ,    "1.040"    ,    "1.040"    ,  "1.040"     ,    "1.040"     ,   "1.040"      ,    "1.040"     ,    "1.040"     ,     "-"        ,      "-"       ,  "-"           ,   "-"          ,     "-"        ,    "-"         ,     "-"        ,    "-"         ,    "-"         ,    "-"        ,     "-"        ,      "-"         ,     "-"       ,    "-"         ,     "-"      , "-"       , "-"    ]
	tauEff_pes         =[     "1.05"     ,     "1.05"     ,  "1.05"        ,     "1.05"     ,     "1.05"     ,    "1.05"     ,    "1.05"     ,    "1.100"    ,    "1.100"    ,  "1.100"     ,    "1.100"     ,   "1.100"      ,    "1.100"     ,    "1.100"     ,     "-"        ,      "-"       ,  "-"           ,   "-"          ,     "-"        ,    "-"         ,     "-"        ,    "-"         ,    "-"         ,    "-"        ,     "-"        ,      "-"         ,     "-"       ,    "-"         ,     "-"      , "-"       , "-"    ]
#0.5/1/1.5 x lepton
	lepton_ID_opt      =[     "1.005"    ,    "1.005"     ,    "1.005"     ,     "1.005"    ,    "1.005"     ,    "1.005"    ,    "1.005"    ,    "-"        ,    "-"        ,  "-"         ,    "-"         ,   "-"          ,  "-"           ,    "-"         ,    "1.01 "     ,   "1.01 "      ,  "1.01 "       ,   "1.01 "      ,    "1.01 "     ,   "-"          ,   "-"          ,    "-"         ,   "-"          ,    "-"        ,      "-"       ,    "-"           ,    "-"        ,    "-"         ,    "-"		 , "-"       , "-"    ]
	lepton_ID_int      =[     "1.010"    ,     "1.010"    ,    "1.010"     ,     "1.010"    ,     "1.010"    ,    "1.010"    ,    "1.010"    ,    "-"        ,    "-"        ,  "-"         ,     "-"        ,   "-"          ,    "-"         ,     "-"        ,     "1.020"    ,      "1.020"   ,  "1.020"       ,   "1.020"      ,     "1.020"    ,    "-"         ,     "-"        ,    "-"         ,    "-"         ,    "-"        ,     "-"        ,      "-"         ,      "-"      ,    "-"         ,     "-"      , "-"       , "-"    ]
	lepton_ID_pes      =[     "1.015"    ,     "1.015"    ,    "1.015"     ,     "1.015"    ,     "1.015"    ,    "1.015"    ,    "1.015"    ,    "-"        ,    "-"        ,  "-"         ,     "-"        ,   "-"          ,    "-"         ,     "-"        ,     "1.030"    ,      "1.030"   ,  "1.030"       ,   "1.030"      ,     "1.030"    ,    "-"         ,     "-"        ,    "-"         ,    "-"         ,    "-"        ,     "-"        ,      "-"         ,      "-"      ,    "-"         ,     "-"      , "-"       , "-"    ]

	lumi_opt           =[     "1.005"    ,    "1.005"     ,    "1.005"     ,     "1.005"    ,    "1.005"     ,    "1.005"    ,    "1.005"    ,    "1.005"    ,    "1.005"    ,  "1.005"     ,    "1.005"     ,   "1.005"      ,  "1.005"       ,    "1.005"     ,    "1.005"     ,   "1.005"      ,  "1.005"       ,   "1.005"      ,    "1.005"     ,   "1.005"      ,   "1.005"      ,    "-"         ,   "1.005"      ,    "-"        ,      "1.005"   ,    "1.005"       ,    "1.005"    ,    "1.005"     ,    "-"		 , "1.005"   , "1.005"]
	lumi_int           =[     "1.010"    ,     "1.010"    ,    "1.010"     ,     "1.010"    ,     "1.010"    ,    "1.010"    ,    "1.010"    ,    "1.010"    ,    "1.010"    ,  "1.010"     ,     "1.010"    ,   "1.010"      ,    "1.010"     ,     "1.010"    ,     "1.010"    ,      "1.010"   ,  "1.010"       ,   "1.010"      ,     "1.010"    ,    "1.010"     ,     "1.010"    ,    "-"         ,    "1.010"     ,    "-"        ,     "1.010"    ,      "1.010"     ,    "1.010"    ,    "1.010"     ,     "-"      , "1.010"   , "1.010"]
	lumi_pes           =[     "1.020"    ,     "1.020"    ,    "1.020"     ,     "1.020"    ,     "1.020"    ,    "1.020"    ,    "1.020"    ,    "1.020"    ,    "1.020"    ,  "1.020"     ,     "1.020"    ,   "1.020"      ,    "1.020"     ,     "1.020"    ,     "1.020"    ,      "1.020"   ,  "1.020"       ,   "1.020"      ,     "1.020"    ,    "1.020"     ,     "1.020"    ,    "-"         ,    "1.020"     ,    "-"        ,     "1.020"    ,      "1.020"     ,    "1.020"    ,    "1.020"     ,     "-"      , "1.020"   , "1.020"]
#1/2/3.5 x jet (same as tau)
	jets_ID_opt        =[     "-"        ,    "-"         ,    "-"         ,     "-"        ,    "-"         ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "-"         ,    "-"         ,   "-"          ,  "-"           ,	  "-"       ,     "-"        ,   "-"          ,  "-"           ,   "-"          ,    "1.020"     ,   "-"          ,   "-"          ,    "-"         ,   "-"          ,    "-"        ,     "-"        ,    "-"           ,    "-"        ,    "-"         ,    "-"		 , "-"       , "-"    ]
	jets_ID_int        =[     "-"        ,    "-"         ,    "-"         ,     "-"        ,     "-"        ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "-"         ,     "-"        ,   "-"          ,    "-"         ,     "-"        ,     "-"        ,      "-"       ,  "-"           ,   "-"          ,     "1.040"    ,    "-"         ,     "-"        ,    "-"         ,    "-"         ,    "-"        ,     "-"        ,      "-"         ,      "-"      ,    "-"         ,     "-"      , "-"       , "-"    ]
	jets_ID_pes        =[     "-"        ,    "-"         ,    "-"         ,     "-"        ,     "-"        ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "-"         ,     "-"        ,   "-"          ,    "-"         ,     "-"        ,     "-"        ,      "-"       ,  "-"           ,   "-"          ,     "1.070"    ,    "-"         ,     "-"        ,    "-"         ,    "-"         ,    "-"        ,     "-"        ,      "-"         ,      "-"      ,    "-"         ,     "-"      , "-"       , "-"    ]
#0.5/1/2 x b-jet
	btag_opt           =[     "1.010"    ,    "-"         ,  "1.01"        ,     "-"        ,    "-"         ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "1.010"     ,    "-"         ,   "1.01"       ,  "-"           ,    "-"         ,    "1.010"     ,   "-"          ,  "1.010"       ,   "1.010"      ,    "1.010"     ,   "1.010"      ,   "1.010"      ,    "-"         ,   "-"          ,    "-"        ,   "1.01"       ,    "1.02 "       ,    "1.02 "    ,    "1.010"     ,     "-"      , "1.02"     , "1.01" ] #1.01
	btag_int           =[     "1.020"    ,     "-"        ,  "1.02"        ,     "-"        ,     "-"        ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "1.020"     ,      "-"       ,   "1.02"       ,    "-"         ,     "-"        ,     "1.020"    ,      "-"       ,  "1.020"       ,   "1.020"      ,     "1.020"    ,    "1.020"     ,     "1.020"    ,    "-"         ,    "-"         ,    "-"        ,   "1.02"       ,    "1.04 "       ,    "1.04 "    ,    "1.020"     ,     "-"      , "1.04"     , "1.02" ] #1.02
	btag_pes           =[     "1.040"    ,     "-"        ,  "1.04"        ,     "-"        ,     "-"        ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "1.040"     ,      "-"       ,   "1.04"       ,    "-"         ,     "-"        ,     "1.040"    ,      "-"       ,  "1.040"       ,   "1.040"      ,     "1.040"    ,    "1.040"     ,     "1.040"    ,    "-"         ,    "-"         ,    "-"        ,   "1.04"       ,    "1.08 "       ,    "1.08 "    ,    "1.040"     ,     "-"      , "1.08"     , "1.04" ] #1.04

	xsecHH_opt         =[     "1.005"    ,    "-"         ,  "-"           ,     "-"        ,    "-"         ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "1.005"     ,    "-"         ,   "-"          ,  "-"           ,    "-"         ,    "1.005"     ,     "-"        ,  "-"           ,   "-"          ,      "-"       ,   "1.005"      ,    "-"         ,    "-"         ,   "-"          ,    "-"        ,   "-"          ,    "1.005 "       ,    "-"       ,    "-"         ,     "-"      , "-"         , "-" ]
	xsecHH_int         =[     "1.010"    ,     "-"        ,  "-"           ,     "-"        ,     "-"        ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "1.010"     ,      "-"       ,   "-"          ,    "-"         ,     "-"        ,     "1.010"    ,      "-"       ,  "-"           ,   "-"          ,      "-"       ,    "1.010"     ,    "-"         ,    "-"         ,    "-"         ,    "-"        ,   "-"          ,    "1.010 "       ,    "-"       ,    "-"         ,     "-"      , "-"         , "-" ]
	xsecHH_pes         =[     "1.015"    ,     "-"        ,  "-"           ,     "-"        ,     "-"        ,    "-"        ,    "-"        ,    "-"        ,    "-"        ,  "1.015"     ,      "-"       ,   "-"          ,    "-"         ,     "-"        ,     "1.015"    ,      "-"       ,  "-"           ,   "-"          ,      "-"       ,    "1.015"     ,    "-"         ,    "-"         ,    "-"         ,    "-"        ,   "-"          ,    "1.015 "       ,    "-"       ,    "-"         ,     "-"      , "-"         , "-" ]

	###
	listOfNuis = ["xsec_tt","xsec_ttH","xsec_QCD","xsec_Zbb","gamma_ID","tauEff","lepton_ID","lumi","jets_ID","btagaa","gamma_ID_bkg","xsec_HH"]
	if "booste" in opt.tipo : listOfNuis = ["xsec_tt","xsec_ttH","xsec_QCD","xsec_Zbb","gamma_ID","tauEff","lepton_ID","lumi","jets_ID","btagbb","gamma_ID_bkg","xsec_HH"]
	if opt.scenario == 1 : 
		listOfNuisArr = [xsec_tt_opt,xsec_ttH_opt,xsec_QCD_opt,xsec_Zbb_opt,gamma_ID_opt,tauEff_opt,lepton_ID_opt,lumi_opt,jets_ID_opt,btag_opt,gamma_ID_bkg_opt,xsecHH_opt,xsec_ZZ_opt,xsec_Zjets_opt]
		keyword = "optimist"
	elif opt.scenario == 2 : 
		listOfNuisArr = [xsec_tt_int,xsec_ttH_int,xsec_QCD_int,xsec_Zbb_int,gamma_ID_int,tauEff_int,lepton_ID_int,lumi_int,jets_ID_int,btag_int,gamma_ID_bkg_int,xsecHH_int,xsec_ZZ_int,xsec_Zjets_int]
		keyword = "intermediate"
	else  : 
		listOfNuisArr = [xsec_tt_pes,xsec_ttH_pes,xsec_QCD_pes,xsec_Zbb_pes,gamma_ID_pes,tauEff_pes,lepton_ID_pes,lumi_pes,jets_ID_pes,btag_pes,gamma_ID_bkg_pes,xsecHH_pes,xsec_ZZ_pes,xsec_Zjets_pes]
		keyword = "pessimistic"
	
	#for scenario in opt/int/pes
	for nuis in range(len(listOfNuis)) :
		for iArray in range(len(channel)):
			dd [( keyword,channel[iArray],process[iArray],listOfNuis[nuis] )] = listOfNuisArr[nuis][iArray]	
	return dd

def parseOptions():

    usage = ('usage: %prog [options] datasetList\n'+ '%prog -h for help')
    parser = optparse.OptionParser(usage)
    parser.add_option('-t', '--tipo', dest='tipo', type='string', default="tmva_bdt", help='')
    parser.add_option('-c', '--forComb', action="store_true", dest='combined', default=False, help='histo card for combination')
    parser.add_option('-u', '--unfold', dest='unfold', type='int', default=0, help='unfold (1) or not (0)')
    parser.add_option('-p', '--non-parametric', action="store_true", dest='parametric', default=False, help='use parametric')
    parser.add_option('-m', '--morphing', action="store_true", dest='morphing', default=False, help='use morphing')
    parser.add_option('-l', '--leptonic', action="store_true", dest='leptonic', default=False, help='semileptonic or fully had')
    parser.add_option('-s', '--sel',  type='int', dest='selection', default=0, help='selection level [0-11]')
    parser.add_option('-k', '--constant-lambda', action="store_true", dest='constlambda', default=False, help='use constant lambda for mhh shape')
    parser.add_option('-x', '--systScenario', type='int', dest='scenario', default=1, help='syst_scenario')
    parser.add_option('-L', '--lambda', type='float', dest='inlambda', default=1.0, help='lambda')
    parser.add_option('-F', '--folder', dest='folderSuffix', type='string', default="", help='suffix for folder')
    parser.add_option('-v', '--version', dest='v45setup', action='store_true', default=False, help='use single beff nuisance')
    #parser.add_option('-s', '--stop', dest='stop', type='int', default=1, help='stop to see the plot')
    global opt, args
    (opt, args) = parser.parse_args()

parseOptions()
global opt, args

#bins2D
# 50 = 5*5*2
# 75 = 5*5*3
#sel8: #10-15 OK < 10-10 OK < 5-10 KO ~ 10-5 OK < 10-3 OK
#10-3 = 5*25 = 125 bins
#sel9 (single points) : 5-3 = 10*25 = 250 bins
print "tipo = "+opt.tipo
tipo = opt.tipo # hmaa_mhh, sel9

#tipo = "hmaa_mbb" # hmaa_mhh, sel8
#tipo = "hh_m" #sel10
#tipo = "haa_m" #sel9
if opt.unfold == 0 :
	unfold = False
else:
	unfold = True

rebin0 =2
rebin1 = 5
rebin2 = 3
selection = "sel{0}".format(opt.selection) #"sel1"
dim = 1
folder = "/eos/user/s/selvaggi/Analysis/hh_comb/hhbbtahtah_v58/hhbbtahtah"
if opt.leptonic :
	folder = "/eos/user/s/selvaggi/Analysis/hh_comb/hhbbtahtal_v58/hhbbtahtal"
	#folder = "hhbbtahtal_v6"
folder = folder +opt.folderSuffix

alphaMorph = RooRealVar("beff","beff",0,-20,20)

alphaMorphHH = RooRealVar("beffHH","beffHH",0,-20,20)
alphaMorphZ = RooRealVar("beffZ","beffZ",0,-20,20)
alphaMorphSH = RooRealVar("beffSH","beffSH",0,-20,20)
alphaMorphTop = RooRealVar("beffTop","beffTop",0,-20,20)

#processes = ["HH","ggH","ttH","zjets","ZZ","ttbar","data_obs"]
#processes = ["HH","ggH","ttH","zjets","ZZ","ttbar","VH","data_obs"]
#processes = ["HH","ttbar","data_obs"]
processes = ["HH","singleH","zjets","ZZ","ttbar","ttV","ttVV","data_obs"]
#lambdas = [0.5,0.9,0.95,1.0,1.03,1.05,1.1,1.5]
#lambdas = [0.5,0.9,0.95,0.96,0.97,0.98,0.99,1.00,1.01,1.02,1.03,1.04,1.05,1.1,1.5]
#lambdas = [0.9,0.95,0.96,0.98,1.00,1.02,1.04,1.05,1.1]
#lambdas = [0.9,0.95,0.96,0.97,0.98,0.99,1.00,1.01,1.02,1.03,1.04,1.05,1.1]
#lambdas = [0.9,0.95,0.96,0.97,0.98,0.99,1.00,1.02,1.03,1.04,1.05,1.1]
lambdas = [opt.inlambda]

x = RooRealVar("x","x",115,135) #maa
x.setBins(50)
if tipo == "hmaa_mbb" :
	y = RooRealVar("y","y",80,140) #mbb
	y.setBins(50)		
elif opt.tipo == "boosted" :
	y = RooRealVar("y","y",380,2140) #mHH
	y.setBins(44)
	rebin0 = 1
	#y = RooRealVar("y","y",220,2500) #mHH
	#y.setBins(57)
elif tipo == "haa_m" :
	y = RooRealVar("y","y",115,135) #maa
	y.setBins(50)
elif "bdt" in tipo:
	rebin0=1
	fileref = TFile.Open("{0}/sel_HH_kappa_lambda_1.00/root_HH_kappa_lambda_1.00/shapes.root".format(folder))
	if not fileref : fileref = TFile.Open("{0}/root_HH_kappa_lambda_1.00/shapes.root".format(folder))
	href =  fileref.Get("{2}_{0}_{1}{3}".format(selection,tipo,"HH",opt.folderSuffix))
	if opt.leptonic :
		y = RooRealVar("ybdtlep","ybdtlep",href.GetXaxis().GetXmin(),href.GetXaxis().GetXmax()) #maa
		y.setBins(href.GetNbinsX()/rebin0) 
		#y = RooRealVar("ybdtlep","ybdtlep",-0.5,0.5) #bdt
		#y.setBins(15)
		#y = RooRealVar("ybdtlep","ybdtlep",-1.0,1.0) #bdt
		#y.setBins(100)
	else :	
		y = RooRealVar("ybdt","ybdt",href.GetXaxis().GetXmin(),href.GetXaxis().GetXmax()) #maa
		y.setBins(href.GetNbinsX()/rebin0) 
		#y = RooRealVar("ybdt","ybdt",-1.0,1.0) #bdt
		#y.setBins(100)
elif "drbb" in tipo :
	y = RooRealVar("ccbbtt","ccbbtt",0,6.0) #cut & count, too few events after bdt cut
	y.setBins(10)
else :
	y = RooRealVar("y","y",240,1500) #mHH
	y.setBins(75)
### 
if dim == 1 :
	varList = RooArgList(y)
	varSet = RooArgSet(y)
	unfold = False
else :
	varList = RooArgList(x,y)
	varSet = RooArgSet(x,y)

tipo = tipo+opt.folderSuffix 

kl = RooRealVar("kl","kl",1.00,0.7,1.3)
klConst = RooRealVar("klConst","klConst",1.00)
klConst.setConstant(True) 
smearPhoton = RooRealVar("smearPhoton","smearPhoton",1.30292)
datasets = []

for klambda in lambdas : 
	rates = []
	histos = []    
	openString =    "{1}/sel_HH_kappa_lambda_{0:.2f}/root_HH_kappa_lambda_{0:.2f}/shapes.root".format(klambda,folder) 
	openStringUp =  "{1}_beffUp/sel_HH_kappa_lambda_{0:.2f}/root_HH_kappa_lambda_{0:.2f}/shapes.root".format(klambda,folder)
	openStringDo =  "{1}_beffDown/sel_HH_kappa_lambda_{0:.2f}/root_HH_kappa_lambda_{0:.2f}/shapes.root".format(klambda,folder)
	openStringOne = "{1}/sel_HH_kappa_lambda_{0:.2f}/root_HH_kappa_lambda_{0:.2f}/shapes.root".format(1.0,folder)

	inFile = TFile.Open(openString)
	inFileUp = TFile.Open(openStringUp)
	inFileDo = TFile.Open(openStringDo)
	inFileOne = TFile.Open(openStringOne)
	if not inFile :
		openString = "{1}/root_HH_kappa_lambda_{0:.2f}/shapes.root".format(klambda,folder) #sel_HH_kappa_lambda_{0:.2f}/
		inFile = TFile.Open(openString)
	if not inFileUp :
		openStringUp =    "{1}_beffUp/root_HH_kappa_lambda_{0:.2f}/shapes.root".format(klambda,folder)  
		inFileUp = TFile.Open(openStringUp)
	if not inFileDo :
		openStringDo =   "{1}_beffDown/root_HH_kappa_lambda_{0:.2f}/shapes.root".format(klambda,folder)
		inFileDo = TFile.Open(openStringDo)
	if not inFileOne :
		openStringOne =   "{1}/root_HH_kappa_lambda_{0:.2f}/shapes.root".format(1.0,folder) 
		inFileOne = TFile.Open(openStringOne)


	#if opt.leptonic : inFile = TFile.Open("{1}/root_HH_kappa_lambda_{0:.2f}/shapes.root".format(klambda,folder))
	suffix = "_sel{}".format(opt.selection)
	if opt.leptonic : suffix += "_semilep"
	if opt.combined : suffix += "_forComb"
	suffix += "_syst{0}".format(opt.scenario)
	suffix += "{0}".format(opt.folderSuffix)
	outFile = open("card{0:.2f}_bbtt{1}.txt".format(klambda,suffix),"w")
	#outWS = TFile.Open("hhbbaa/root_HH_kappa_l_{0:.2f}/ws.root","RECREATE")
	ws = RooWorkspace("w")


	allPdfs = []
	for iproc in processes :
		if "HH" in iproc and not "bb" in tipo and opt.parametric and not "boosted" in opt.tipo:
			print "do stuff to generate rooprodpdf"
			#// Declare variables x,mean,sigma with associated name, title, initial value and allowed range
			if tipo == "hmaa_mhh" : pdf = RooProdPdf("HH","HH",gauss,gauss) #RooProdPdf("HH","HH",landau,gauss)
			elif tipo == "hh_m" : pdf = gauss #landau
			elif tipo == "haa_m" : pdf = gauss
			pdf.SetNameTitle("HH","HH")
			allPdfs.append(pdf) 
			if "boosted" in opt.tipo : rates.append( 1.235831e-04 * 30000000.0) #rates.append(11639.5)
			else : rates.append (395.634641002) #rates.append(3271.07673397) #rates.append(7239.516396) #rates.append(10211.10624)
			#wFunc = RooRealVar ("weight","event weight",1) 
			#tempdata = pdf.generate(RooArgSet(x,y),5009.4*1-15732*1+20938)
			#datasets.append(tempdata)
			#wFunc = RooRealVar ("weight","event weight",1) 
			#tempdata.addColumn(wFunc)
			#	RooDataSet (const char *name, const char *title, RooDataSet *data, const RooArgSet &vars, const char *cuts=0, const char *wgtVarName=0)
			#datasets.append(RooDataSet(tempdata.GetName(),tempdata.GetTitle(),tempdata,RooArgSet(x,y,wFunc),"True",wFunc.GetName()))
			#datasets.append()
		else :
			print "{2}_{0}_{1}".format(selection,tipo,iproc)
			htemp = inFile.Get("{2}_{0}_{1}".format(selection,tipo,iproc))
			htempUp = inFileUp.Get("{2}_{0}_{1}".format(selection,tipo,iproc))
			htempDo = inFileDo.Get("{2}_{0}_{1}".format(selection,tipo,iproc))
			print "BinningX,y",iproc, htemp.GetNbinsX(), htemp.GetNbinsY()
			#if dim == 1 : htemp.Rebin(rebin0)
			#else : 
			#	htemp.RebinX(rebin1) #5
			#	htemp.RebinY(rebin2) #5
			#	print "Re-BinningX,y",iproc, htemp.GetNbinsX(), htemp.GetNbinsY()
#			if unfold :
#				h = TH1F(iproc,iproc,htemp.GetNbinsX()*htemp.GetNbinsY(),htemp.GetXaxis().GetXmin(),htemp.GetXaxis().GetXmax()*htemp.GetNbinsY())
#				ibin=1
#				for xbin in range(1,htemp.GetNbinsX()+1) :
#					for ybin in range(1,htemp.GetNbinsY()+1) :
#						h.SetBinContent(ibin,htemp.GetBinContent(xbin,ybin))
#						ibin += 1
#			else : 
#				if not "boosted" in opt.tipo : 
			h = htemp
			#if "drbb" in tipo : h.Rebin(2)
#				else : 
#					h = TH1F(iproc,iproc,44,380,2140)
#					for ibin in range(0,44) :
#						h.SetBinContent(ibin,htemp.GetBinContent(ibin+8))

			print "Binning",iproc, h.GetNbinsX()
			h.SetName(iproc)
			h.SetTitle(iproc)
			if opt.v45setup:
				htempUp.SetName(iproc+"beffUp")
				htempUp.SetTitle(iproc+"beffUp")
				htempDo.SetName(iproc+"beffDown")
				htempDo.SetTitle(iproc+"beffDown")
			else: 
				if "single" in iproc :
					htempUp.SetName(iproc+"beffSHUp")
					htempUp.SetTitle(iproc+"beffSHUp")
					htempDo.SetName(iproc+"beffSHDown")
					htempDo.SetTitle(iproc+"beffSHDown")
				elif "tt" in iproc:
					htempUp.SetName(iproc+"beffTopUp")
					htempUp.SetTitle(iproc+"beffTopUp")
					htempDo.SetName(iproc+"beffTopDown")
					htempDo.SetTitle(iproc+"beffTopDown")
				elif "zjets" in iproc or "ZZ" in iproc :
					htempUp.SetName(iproc+"beffZUp")
					htempUp.SetTitle(iproc+"beffZUp")
					htempDo.SetName(iproc+"beffZDown")
					htempDo.SetTitle(iproc+"beffZDown")
				else :
					htempUp.SetName(iproc+"beffHHUp")
					htempUp.SetTitle(iproc+"beffHHUp")
					htempDo.SetName(iproc+"beffHHDown")
					htempDo.SetTitle(iproc+"beffHHDown")
			#if iproc == "HH" : 
	 		#print "scaling"
			print h.Integral(), 30000000.0*h.Integral()
	 		h.Scale(30000000.0)
	 		htempUp.Scale(30000000.0)
	 		htempDo.Scale(30000000.0)
			for xbin in range(1,h.GetNbinsX()+1) :
	 			if h.GetBinContent(xbin)<=0 : 
	 				if "ttbar" in iproc :
	 					if not opt.leptonic : h.SetBinContent(xbin,0.001)#*30000000.0)
	 					else: h.SetBinContent(xbin,h.GetBinContent(xbin-1)/2.0)#*30000000.0)
	 				else : h.SetBinContent(xbin,0.00001)#)	
	 			#if xbin == 44 and "ttbar" in iproc and not opt.leptonic : h.SetBinContent(xbin,300000.)
	 			#if "ttbar" in iproc and opt.leptonic : 
	 			#	if xbin == 44 : h.SetBinContent(xbin,2500000.)
	 			#	elif xbin == 46: h.SetBinContent(xbin,1500000.)
	 			#	elif xbin == 47: h.SetBinContent(xbin,1200000.)
	 			#	elif xbin == 49: h.SetBinContent(xbin,600000.)
	 			#	elif xbin == 50: h.SetBinContent(xbin,450000.)
	
	 		#if "HH" in iproc : h.Scale(1000.0)
	 		if dim == 1 : 
	 			h.Rebin(rebin0)
	 			htempUp.Rebin(rebin0)
	 			htempDo.Rebin(rebin0)
	 		print h.Integral()
	 		if "HH" in iproc :
				#if opt.leptonic : inFileOne = TFile.Open("{1}/sel_HH_kappa_lambda_{0:.2f}/root_HH_kappa_lambda_{0:.2f}/shapes.root".format(klambda,folder))
				#else : inFileOne = TFile.Open("{1}/root_HH_kappa_lambda_{0:.2f}/shapes.root".format(klambda,folder))
				inFileOne = TFile.Open(openStringOne)
	 			htempOne = inFileOne.Get("{2}_{0}_{1}".format(selection,tipo,iproc))
	 			htempOne.Scale(30000000.0)
	 			h.Scale(htempOne.Integral()/h.Integral())
	 			htempDo.Scale(htempOne.Integral()/htempDo.Integral())
	 			htempUp.Scale(htempOne.Integral()/htempUp.Integral())
			#if tipo == "haa_m" : rates.append(h.Integral(h.FindBin(120),h.FindBin(130)))
			if opt.tipo == "hh_m" : rates.append(h.Integral(h.FindBin(240),h.FindBin(1500)))
			else : rates.append(h.Integral())
			#htoappend = h.Rebin(4*dim)
			histos.append(h)
			histos.append(htempUp)
			histos.append(htempDo)
			#print "Normalizations", h.Integral(), h.Integral(h.FindBin(120),h.FindBin(130))
			h.Sumw2()
			suffr = "rdh"
			if opt.leptonic : suffr = "rdhlep"
			rdh = RooDataHist(iproc+suffr,iproc+suffr,varList,h)
			rdhUp = RooDataHist(iproc+"Up"+suffr,iproc+"Up"+suffr,varList,htempUp)
			rdhDo = RooDataHist(iproc+"Do"+suffr,iproc+"Do"+suffr,varList,htempDo)
			#print "Normalizations", rdh.sumEntries(), h.Integral(), h.Integral(h.FindBin(120),h.FindBin(130))
			if not "obs" in iproc : 
				#if "HH" in iproc and tipo == "hmaa_mbb" and opt.parametric :
				#	#qui fare la conditional rooprodpdf
				#	#if tipo == "hmbb_mhh" : pdf = RooProdPdf("HH","HH",landau,gauss) #questo non esiste perche non ha senso
				#	#elif tipo == "hbb_m" : pdf = RooHistPdf(iproc,iproc,varSet,rdh)
				#	#elif tipo == "hmaa_mbb":
				#	pdftemp = RooHistPdf(iproc+"temp",iproc+"temp",varSet,rdh)
				#	pdf = RooProdPdf("HH","HH",RooArgSet(gauss),RooFit.Conditional(RooArgSet(pdftemp),RooArgSet(y)) )
				#else : 
				pdfNo = RooHistPdf(iproc+"nominal"+suffr,iproc+"nominal"+suffr,varSet,rdh)
				pdfUp = RooHistPdf(iproc+"beffUp"+suffr,iproc+"beffUp"+suffr,varSet,rdhUp)
				pdfDo = RooHistPdf(iproc+"beffDown"+suffr,iproc+"beffDown"+suffr,varSet,rdhDo)
				if opt.v45setup: 
					pdf = FastVerticalInterpHistPdf(iproc,iproc,y,RooArgList(pdfNo,pdfUp,pdfDo),RooArgList(alphaMorph))
				else :
					if "single" in iproc : pdf = FastVerticalInterpHistPdf(iproc,iproc,y,RooArgList(pdfNo,pdfUp,pdfDo),RooArgList(alphaMorphSH))
					elif "tt" in iproc: pdf = FastVerticalInterpHistPdf(iproc,iproc,y,RooArgList(pdfNo,pdfUp,pdfDo),RooArgList(alphaMorphTop))
					elif "zjets" in iproc or "ZZ" in iproc : pdf = FastVerticalInterpHistPdf(iproc,iproc,y,RooArgList(pdfNo,pdfUp,pdfDo),RooArgList(alphaMorphZ))
					else : pdf = FastVerticalInterpHistPdf(iproc,iproc,y,RooArgList(pdfNo,pdfUp,pdfDo),RooArgList(alphaMorphHH))
#				pdf.Print()
				allPdfs.append(pdf)
				#allPdfs.append(pdfUp)
				#allPdfs.append(pdfDo)
				#getattr(ws,'import')(pdfUp,RooFit.RecycleConflictNodes())
				#getattr(ws,'import')(pdfDo,RooFit.RecycleConflictNodes())
#				print "generating"
#				if dim==2 :  datasets.append(pdf.generate(RooArgSet(x,y),h.Integral()))
#				else : datasets.append(pdf.generate(RooArgSet(y),h.Integral()))
#				print pdf
				print "LEN ", len(allPdfs)
			else : 
				pdf = rdh
				print "Normalizations", rdh.sumEntries(), h.Integral()
				pdf.SetNameTitle("data_obs","data_obs")
				pdf.SetName("data_obs")
				pdf.SetTitle("data_obs")
				allPdfs.append(pdf)
				#pdf = datasetFull
		getattr(ws,'import')(pdf,RooFit.RecycleConflictNodes())
			#rfvSigRate_HH = RooFormulaVar("HH_norm","1.6096-0.6081*@0",RooArgList(kl))
		#coeff = 0
		#if "v1" in folder : #sel,tipo,version
		#	coeff=getLinearCoeff(opt.selection,opt.leptonic,1)
		#elif "v2" in folder or "v3" in folder or "v4" in folder or "v5" in folder or "v6" in folder: 
		#	coeff=getLinearCoeff(opt.selection,opt.leptonic,2)
		#elif "FCC" in folder : coeff=getLinearCoeff(opt.selection,opt.leptonic,3)
		#else : coeff=getLinearCoeff(opt.selection,0,0)
		#rfvSigRate_FCC = RooFormulaVar("HH_norm","1.5264*@0*@0-3.6952*@0+3.1688",RooArgList(kl))  #y =   # 1.6307-0.6302*@0 Questo forse dipenderebbe dalla sel? da verificare
		#rfvSigRate_FCC = RooFormulaVar("HH_norm","{0:.4f}*@0+1-{0:.4f}".format(coeff),RooArgList(kl)) # = a*L+1-a = 1+a*(L-1)
		if opt.leptonic: rfvSigRate_FCC = RooFormulaVar("HH_norm",getRatebbtahtal(getScenario(opt.folderSuffix),getBwP(opt.folderSuffix),getLwP(opt.folderSuffix)),RooArgList(kl))		
		else : rfvSigRate_FCC = RooFormulaVar("HH_norm",getRatebbtahtah(getScenario(opt.folderSuffix),getBwP(opt.folderSuffix),getLwP(opt.folderSuffix)),RooArgList(kl))		
		rfvSigRate_HELHC = RooFormulaVar("HH_norm","-0.6136*@0 + 1.6694",RooArgList(kl)) 
		rfvSigRate_HH = rfvSigRate_FCC
		if not opt.morphing : getattr(ws,'import')(rfvSigRate_HH,RooFit.RecycleConflictNodes())
		#if iproc = "HH" : obs = inFile.Get("{2}_{0}_{1}".format(sel,tipo,iproc)).Clone("data_obs")
		#else : obs.Add(inFile.Get("{2}_{0}_{1}".format(sel,tipo,iproc)))
	#
	listOfProc = processes[:-1] #dovrei crearla da processes droppando data_obs ma ok
	channelID = "ch2"
	if opt.leptonic : channelID = "ch1"
	scenarioID = "optimist"
	if opt.scenario == 2 : scenarioID = "intermediate"
	elif opt.scenario == 3 : scenarioID = "pessimistic"
	#nuisances = ["xsec_tt","xsec_ttH","xsec_QCD","gamma_ID","tauEff","lepton_ID","lumi","jets_ID","btag"]
	#nuisances = ["xsec_tt","xsec_ttH","xsec_HH","tauEff","lepton_ID","lumi","jets_ID","btag"]
	nuisances = ["xsec_tt","xsec_ttH","xsec_HH","tauEff","lepton_ID","lumi"]


	dd = createDict()

	#obs.SetName("data_obs")
	#obs.SetTitle("data_obs")
	#ws.writeToFile("hhbbaa/root_HH_kappa_l_{0:.2f}/ws.root".format(klambda))
	print rates 
	outFile.write("imax 1\n")
	#if opt.tipo == "boosted" :outFile.write("jmax 1\n")
	#else: 
	outFile.write("jmax 6\n")
	outFile.write("kmax *\n")
	outFile.write("----------------------\n")
	#if opt.leptonic :
	testFile = TFile.Open("{0}/sel_HH_kappa_lambda_1.00/root_HH_kappa_lambda_1.00/shapes.root".format(folder))
	if not testFile : 
		if opt.morphing or opt.combined : outFile.write("shapes * * {1}/root_HH_kappa_lambda_{0:.2f}/wsbbtt_{2}{3}.root $PROCESS $PROCESS$SYSTEMATIC \n".format(klambda,folder,opt.selection,opt.folderSuffix)) #histograms
		else :  outFile.write("shapes * * {1}/root_HH_kappa_lambda_{0:.2f}/ws_{2}{3}.root w:$PROCESS w:$PROCESS$SYSTEMATIC \n".format(klambda,folder,opt.selection,opt.folderSuffix)) #workspace
	else : 
		if opt.morphing or opt.combined : outFile.write("shapes * * {1}/sel_HH_kappa_lambda_{0:.2f}/root_HH_kappa_lambda_{0:.2f}/wsbbtt_{2}{3}.root $PROCESS $PROCESS$SYSTEMATIC \n".format(klambda,folder,opt.selection,opt.folderSuffix)) #histograms
		else :  outFile.write("shapes * * {1}/sel_HH_kappa_lambda_{0:.2f}/root_HH_kappa_lambda_{0:.2f}/ws_{2}{3}.root w:$PROCESS w:$PROCESS$SYSTEMATIC \n".format(klambda,folder,opt.selection,opt.folderSuffix)) #workspace
	#else :
	#	if opt.morphing or opt.combined : outFile.write("shapes * * {1}/root_HH_kappa_lambda_{0:.2f}/wsbbtt_{2}.root $PROCESS $PROCESS$SYSTEMATIC \n".format(klambda,folder,opt.selection)) #histograms
	#	else : outFile.write("shapes * * {1}/root_HH_kappa_lambda_{0:.2f}/ws_{2}.root w:$PROCESS w:$PROCESS$SYSTEMATIC \n".format(klambda,folder,opt.selection)) #workspace
	#outFile.write("shapes * * {1}/root_HH_kappa_l_{0:.2f}/wsbbtt_{2}.root $PROCESS \n".format(klambda,folder,opt.selection)) #histograms
	#else : outFile.write("shapes * * {1}/root_HH_kappa_l_{0:.2f}/wsbbtt_{2}.root $PROCESS \n".format(klambda,folder,opt.selection)) #workspace
	#outFile.write("shapes * * wsbbtt1.root w:$PROCESS \n".format(klambda,folder))
	outFile.write("----------------------\n")
	if opt.leptonic : outFile.write("bin binlep\n")
	else : outFile.write("bin binhad\n")
	outFile.write("observation {0}\n".format(rates[len(rates)-1]))
	outFile.write("------------------------------\n")
	if opt.leptonic : outFile.write("bin             binlep  binlep binlep  binlep binlep binlep binlep\n")		
	else : outFile.write("bin binhad  binhad   binhad  binhad binhad binhad binhad\n")		
	outFile.write("process   HH   singleH zjets ZZ ttbar ttV ttVV \n") #"HH","singleH","zjets","ZZ","ttbar"
	outFile.write("process   0    1        2     3   4   5     6   \n")
	outFile.write("rate      {0} {1} {2} {3}   {4} {5} {6}  \n".format(rates[0],rates[1],rates[2],rates[3],rates[4],rates[5],rates[6]))
	outFile.write("--------------------------------\n")
	if opt.v45setup: 
		outFile.write("beff shape 1 1 1 1 1 1 1  \n")
	else :
		outFile.write("beffHH shape 1 - - - - - -  \n")
		outFile.write("beffSH shape - 1 - - -  - -   \n")
		outFile.write("beffZ shape - - 1 1 -  - -  \n")
		outFile.write("beffTop shape - - - - 1 1 1 \n")
	#outFile.write("beff param 0  1  [-3,3]\n")
	for nuis in nuisances : 
		outFile.write("{7}     lnN    {0} {1} {2} {3} {4} {5} {6} \n".format(dd[scenarioID,channelID,listOfProc[0],nuis],dd[scenarioID,channelID,listOfProc[1],nuis],dd[scenarioID,channelID,listOfProc[2],nuis],dd[scenarioID,channelID,listOfProc[3],nuis],dd[scenarioID,channelID,listOfProc[4],nuis],dd[scenarioID,channelID,listOfProc[5],nuis],dd[scenarioID,channelID,listOfProc[6],nuis],nuis)) #dd [( scenarioID,channel[iArray],process[iArray],listOfNuis[nuis] )] = listOfNuisArr[nuis][iArray]	

	#outFile.write("lumiSig     lnN    1.01       - \n")
	#outFile.write("lumiSig     lnN    1.01 - - - - - \n")
##	outFile.write("lumiAll     lnN    1.01 - - - - \n")
##	outFile.write("xsec_tt    lnN    - 1.01 1.01 1.01 1.01\n")		
##	#outFile.write("xsec_h     lnN    - 1.01 - - -\n")
##	if opt.optimistic == 1: 
##		outFile.write("btag_bbtt   lnN    1.02 - - - - \n")
##		if opt.leptonic :  
##			outFile.write("tauEff     lnN    1.05 - - - - \n")
##			outFile.write("eleID     lnN    1.01 - - - - \n")
##		else :  outFile.write("tauEff     lnN    1.1 - - - - \n")
##	elif opt.optimistic ==2 :
##		outFile.write("btag_bbtt   lnN    1.01 - - - -\n")
##		if opt.leptonic :  
##			outFile.write("tauEff     lnN    1.025 - - - - \n")
##			outFile.write("eleID     lnN    1.005 - - - - \n")
##		else :  outFile.write("tauEff     lnN    1.05 - - - - \n")
##	elif opt.optimistic ==3 :
##		outFile.write("btag_bbtt   lnN    1.005 - - - -\n")
##		if opt.leptonic :  
##			outFile.write("tauEff     lnN    1.01 - - - - \n")
##			outFile.write("eleID     lnN    1.0025 - - - - \n")
##		else :  outFile.write("tauEff     lnN    1.02 - - - - \n")
##	elif opt.optimistic ==4 :
##		outFile.write("btag_bbtt   lnN    1.000005 1.000005 1.000005 1.000005 1.000005\n")
##		if opt.leptonic :  
##			outFile.write("tauEff     lnN    1.01 1.01 1.01 1.01 1.01 \n")
##			outFile.write("eleID     lnN    1.0025 1.0025 1.0025 1.0025 1.0025 \n")
##		else :  outFile.write("tauEff     lnN    1.5 1.02 1.02 1.02 1.02 \n")
#	outFile.write("ttbarScaler rateParam * ttbar 1.0 \n")
#	outFile.write("ttbarScaler rateParam * zjets 1.0 \n")
#	outFile.write("ttbarScaler rateParam * singleH 1.0 \n")
#	outFile.write("ttbarScaler rateParam * ZZ 1.0 \n")
#	if opt.combined :
#		if opt.leptonic :
#			outFile.write("kl extArg 1.0 [0.7,1.3]\n")
#			outFile.write("paramL extArg {0:.5f}\n".format(coeff))
#			outFile.write("kl_scaling_lep rateParam * HH (@0*@1+1-@1) kl,paramL\n")
#		else :
#			outFile.write("kl extArg 1.0 [0.7,1.3]\n")
#			outFile.write("paramH extArg {0:.5f}\n".format(coeff))
#			outFile.write("kl_scaling_had rateParam * HH (@0*@1+1-@1) kl,paramH\n")
	coeff = 0.1601
	coeff2 = -0.4513
	if opt.leptonic :
		coeff = 0.1422
		coeff2 = -0.3854
	if opt.combined :
		if opt.inlambda < 1 :
			outFile.write("kl extArg 1.0 [-0.3,1.2]\n")
		elif opt.inlambda > 1.2 :
			outFile.write("kl extArg 1.0 [0.9,2.0]\n") 
		elif opt.inlambda > 1.6 :
			outFile.write("kl extArg 1.0 [1.0,3.5]\n") #kl = RooRealVar("kl","kl",opt.inlambda,1.0,3.5)
		else :
			outFile.write("kl extArg 1.0 [0.7,1.3]\n") #kl = RooRealVar("kl","kl",opt.inlambda,0.7,1.3)
	
	formString = ""
	if opt.leptonic : 
		formString = getRatebbtahtal(getScenario(opt.folderSuffix),getBwP(opt.folderSuffix),getLwP(opt.folderSuffix)) #"0.30975*@0*@0 + (-0.68143-2.0*0.30975)*@0 +0.30975 + 1.0 - -0.68143"
		formString = formString.replace(" ","")
		formString = formString.replace("--","+")
		outFile.write("kl_scaling_lep rateParam * HH {0} kl\n".format(formString))
	else : 
		formString = getRatebbtahtah(getScenario(opt.folderSuffix),getBwP(opt.folderSuffix),getLwP(opt.folderSuffix))
		formString = formString.replace(" ","")
		formString = formString.replace("--","+")
		outFile.write("kl_scaling_had rateParam * HH {0} kl\n".format(formString))	


#		if opt.leptonic :
#			outFile.write("paramL extArg {0:.5f}\n".format(coeff))
#			outFile.write("paramL2 extArg {0:.5f}\n".format(coeff2))
#			#outFile.write("kl_scaling_lep rateParam * HH (@1*@0*@0 + (@2-2.0*@1)*@0 +@1 + 1.0 - @2) kl,paramL,paramL2\n") #param2 = linear
#			outFile.write("kl_scaling_lep rateParam * HH (@1*@0*@0+@2*@0-2.0*@1*@0+@1+1.0-@2) kl,paramL,paramL2\n") #param2 = linear
#		else :
#			outFile.write("paramH extArg {0:.5f}\n".format(coeff))
#			outFile.write("paramH2 extArg {0:.5f}\n".format(coeff2))
#			#outFile.write("kl_scaling_had rateParam * HH (@1*@0*@0 + (@2-2.0*@1)*@0 +@1 + 1.0 - @2) kl,paramH,paramH2\n") #kl_scaling_had rateParam * HH (@0*@1+1-@1) kl,paramH
#			outFile.write("kl_scaling_had rateParam * HH (@1*@0*@0+@2*@0-2.0*@1*@0+@1+1.0-@2) kl,paramH,paramH2\n")

#		outFile.write("effScaler rateParam * ggjj 0.8 \n")
#		outFile.write("effScaler rateParam * zjets 0.895 \n")
#		outFile.write("btagger   rateParam * ttH 1.0 \n")
#		outFile.write("btagger   rateParam * VH 1.0 \n")
#		outFile.write("btagger   rateParam * ggH 1.0 \n")
#		outFile.write("btagger   rateParam * HH 1.0 \n")


	#outFile.write("bgnorm   lnN    1.00       1.3\n")
	#name rateParam bin process initial_value
	print "wrotecard"
	#if opt.leptonic : 
	if not testFile : outWS = TFile.Open("{1}/root_HH_kappa_lambda_{0:.2f}/wsbbtt_{2}{3}.root".format(klambda,folder,opt.selection,opt.folderSuffix),"RECREATE")
	else : outWS = TFile.Open("{1}/sel_HH_kappa_lambda_{0:.2f}/root_HH_kappa_lambda_{0:.2f}/wsbbtt_{2}{3}.root".format(klambda,folder,opt.selection,opt.folderSuffix),"RECREATE")
	#else : outWS = TFile.Open("{1}/root_HH_kappa_lambda_{0:.2f}/wsbbtt_{2}.root".format(klambda,folder,opt.selection),"RECREATE")
	outWS.cd()
	for h in histos :
		h.Write()
	outWS.Close()
	#ws.writeToFile("wsbbtt1.root")
	print "writing WS"
	if not testFile : ws.writeToFile("{1}/root_HH_kappa_lambda_{0:.2f}/ws_{2}{3}.root".format(klambda,folder,opt.selection,opt.folderSuffix))
	else : ws.writeToFile("{1}/sel_HH_kappa_lambda_{0:.2f}/root_HH_kappa_lambda_{0:.2f}/ws_{2}{3}.root".format(klambda,folder,opt.selection,opt.folderSuffix))
	print "done ALL"
	ws = 0

from ROOT import *
import os,re, optparse
from outRatesbbaa import getRatebbaa
from outRatesbbbb import getRatebbbb

#controllare hout per hhbbbb se serve ancora
#sel_HH_kappa_lambda_{0:.2f}/
#per qualche motivo parametrica non funziona piu, la gaussiana e' tutta sbagliata...ah no, in data obs ho anche un sacco di altra roba...
#selections:
# 1D(m_hh) : sel10
# 1D(m_aa) : sel9
# 1D(m_bb) : sel8 (skip this)
# 2D(m_hh,m_aa) : sel9/10 (is the same)
# 2D(m_aa,m_bb) : sel8
#-1893,7x + 5163,6

#ch1 bbtahtal
#ch2 bbtahtah
#ch3 bbZZ
#ch4 bbaa  ggH -> singleH
#ch5 bbbb "singleH","ttbar"

btagWPs = ['L','M','T']
photonWPs = ['M','T']
scenarios = ['I','II','III']

def getScenario(folderName):
	if "III" in folderName: return "III"
	elif "II" in folderName: return "II"
	else : return "I"

def getPwP(folderName):
	if "LM" in folderName: return "M"
	elif "LT" in folderName: return "T"
	elif "MM" in folderName: return "M"
	elif "MT" in folderName: return "T"
	elif "TM" in folderName: return "M"
	elif "TT" in folderName: return "T"
	else : return "CIAO"

def getBwP_bbaa(folderName):
	if "LM" in folderName: return "L"
	elif "LT" in folderName: return "L"
	elif "MM" in folderName: return "M"
	elif "MT" in folderName: return "M"
	elif "TM" in folderName: return "T"
	elif "TT" in folderName: return "T"
	else : return "CIAO"


def getBwP_bbbb(folderName):
	if "_L" in folderName: return "L"
	elif "_M" in folderName: return "M"
	elif "_T" in folderName: return "T"
	else : return "CIAO"

#for sc in I II III ; do for bwp in L M T ; do for pwp in M T ; do python cardMaker.py -F "_${sc}_${bwp}${pwp}" ; done ; done ; done

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

	###                                     [xsec_tt_ ,xsec_ttH_ ,xsec_QCD_ ,xsec_Zbb_ ,gamma_ID_ ,tauEff_ ,lepton_ID_ ,lumi_ ,jets_ID_ ,btag_ ,gamma_ID_bkg_ ,xsecHH_ ,xsec_ZZ_ ,xsec_Zjets_ ]
	listOfNuis =                           ["xsec_tt","xsec_ttH","xsec_QCD","xsec_Zbb","gamma_ID","tauEff","lepton_ID","lumi","jets_ID","btagaa","gamma_ID_bkg","xsec_HH","xsec_ZZ","xsec_Zjets"]
	if "booste" in opt.tipo : listOfNuis = ["xsec_tt","xsec_ttH","xsec_QCD","xsec_Zbb","gamma_ID","tauEff","lepton_ID","lumi","jets_ID","btagbb","gamma_ID_bkg","xsec_HH","xsec_ZZ","xsec_Zjets"]
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
    parser.add_option('-t', '--tipo', dest='tipo', type='string', default="bdth_bdtqcd", help='')
    parser.add_option('-u', '--unfold', dest='unfold', type='int', default=0, help='unfold (1) or not (0)')
    parser.add_option('-p', '--non-parametric', action="store_true", dest='parametric', default=False, help='if false use templates or morphing instead of parametric')
    parser.add_option('-k', '--constant-lambda', action="store_true", dest='constlambda', default=False, help='use constant lambda for mhh shape')
    #parser.add_option('-s', '--stop', dest='stop', type='int', default=1, help='stop to see the plot')
    parser.add_option('-s', '--scenario', dest='scenario', type='int', default=1, help='systematics 1=opt, 2=int, 3=pes')
    parser.add_option('-S', '--selection', dest='selection', type='int', default=0, help='selection')
    parser.add_option('-L', '--lambda', dest='inlambda', type='float', default=1.0, help='lambda value')
    parser.add_option('-F', '--folder', dest='folderSuffix', type='string', default="", help='suffix for folder')
    parser.add_option('-w', '--wpScaler', dest='wpScaler', type='float', default=0.8, help='apply wp scaler')
    parser.add_option('-v', '--version', dest='v45setup', action='store_true', default=False, help='use single beff nuisance')
    global opt, args
    (opt, args) = parser.parse_args()

print "started"
parseOptions()
global opt, args

print "parsed"

inputsprec = [0.0,0.4,0.7,1.0,1.3,1.5,1.7,2.0,2.2,2.4,2.6,3.0]

#applyEffScaler=True
applyjgjjScaler=1.0 #default 1
applyggjjScaler=1.0 #default 1 (gia applicato)
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
	print "HOBS 0"
	unfold = False
else:
	print "HOBS 1"
	unfold = True

rebin0 =1 #2
rebin1 = 1 #5
rebin2 = 1 #3
selection = "sel0" #"sel9"
dim = 2
#folder = "FCCworkshop3/hhbbaa_v7_2"
#folder = "FCCworkshop3/hhbbaa"+opt.folderSuffix
folder = "/eos/user/s/selvaggi/Analysis/hh_comb/hhbbaa_v58/hhbbaa"+opt.folderSuffix

if tipo == "hmaa_mhh" :
	selection = "sel10" #"sel9"
	dim = 2
	rebin1 = 2#10
	rebin2 = 2#5

elif tipo == "hmaa_mbb" :
	selection = "sel10" #"sel8"
	dim = 2
	rebin1 = 2
	rebin2 = 2

elif tipo == "hh_m" :
	selection = "sel10"
	dim =1 

elif tipo == "haa_m" :
	selection = "sel6" #sel9
	dim = 1

elif "bdth_bdtqcd" in tipo :
	selection = "sel{0}".format(opt.selection)
	dim = 2
	rebin1 = 1 #2    #2,1 funziona, 1,2 non funziona MACHECAZZO
	rebin2 = 1
	#unfold = False

elif "tmva_bdt_singleh" in tipo or "tmva_bdt_qcd" in tipo:
	selection = "sel0"
	dim = 1
	rebin0 = 1

elif tipo == "boosted" :
	#tipo = "hh_m"
	tipo = "tmva_bdt"
	selection = "sel0" #"sel6"
	dim =1 
	#folder = "FCCworkshop3/hhbbbb"+opt.folderSuffix #"hh_boosted"
	folder = "/eos/user/s/selvaggi/Analysis/hh_comb/hhbbbb_v58/hhbbbb"+opt.folderSuffix

	photonWPs = ['']

#klambda = 1.5
processes = ["HH","jgjj","ggjj","singleH","data_obs"]
#processes = ["HH","jgjj","data_obs"]

#processes = ["HH","jgjj","ggjj","ttH","data_obs"]
#processes = ["HH","jgjj","ggjj","ttH","ggH","VH","data_obs"]
#lambdas = [0.5,0.9,0.95,1.0,1.03,1.05,1.1,1.5]
#lambdas = [0.5,0.9,0.95,0.96,0.97,0.98,0.99,1.00,1.01,1.02,1.03,1.04,1.05,1.1,1.5]
#lambdas = [0.9,0.95,0.96,0.98,1.00,1.02,1.04,1.05,1.1]
#lambdas = [0.9,0.95,0.96,0.97,0.98,0.99,1.00,1.01,1.02,1.03,1.04,1.05,1.1]
#lambdas = [0.9,0.95,0.96,0.97,0.98,0.99,1.00,1.02,1.03,1.05,1.1]
lambdas = [opt.inlambda]
if opt.tipo == "boosted" : 
	processes = ["HH","singleH","ZZ","ttbar","Zbb","QCD","data_obs"] #->verificare che ci siano tutte le syst nel dict
	#processes = ["HH","singleH","EWK","ttbar","QCDEWK","QCD","data_obs"] # ->verificare che ci siano tutte le syst nel dict
	#lambdas = [1.0,0.5,0.9,0.95,1.05,1.1,1.5]

#if opt.tipo == "hh_m" :
#	x = RooRealVar("x","x",240,1500) #mhh
#	x.setBins(50)
#else:	
#x = RooRealVar("x","x",120,130) #maa

if tipo == "hmaa_mbb" :
	y = RooRealVar("y","y",80,140) #mbb
	y.setBins(50)	
	x = RooRealVar("x","x",115,135) #maa
	x.setBins(50)
	
elif opt.tipo == "boosted" :
#	y = RooRealVar("yboosted","yboosted",-1.0,1.0) #mHH
#	y.setBins(100) #50
#	rebin0 = 1
	x = RooRealVar("xboosted","xboosted",-1.0,1.0) #maa
	x.setBins(100) #50

	fileref = fileref = TFile.Open("{0}/sel_HH_kappa_lambda_1.00/root_HH_kappa_lambda_1.00/shapes.root".format(folder))
	if not fileref : TFile.Open("{0}/root_HH_kappa_lambda_1.00/shapes.root".format(folder))
	htmp =  fileref.Get("{2}_{0}_{1}{3}".format(selection,tipo,"HH",opt.folderSuffix))
	href = TH1F("href","href",15,htmp.GetBinLowEdge(10),htmp.GetBinLowEdge(25))
	y = RooRealVar("yboosted","yboosted",href.GetXaxis().GetXmin(),href.GetXaxis().GetXmax()) #maa
	y.setBins(href.GetNbinsX()/rebin0) 
#	y = RooRealVar("yboosted","yboosted",-0.5,0.7) #mHH
#	y.setBins(50)
#	rebin0 = 2
#	x = RooRealVar("xboosted","xboosted",-0.5,0.7) #maa
#	x.setBins(50)
elif tipo == "haa_m" :
	y = RooRealVar("y","y",115,135) #maa
	y.setBins(50)
	x = RooRealVar("x","x",115,135) #maa
	x.setBins(50)
elif tipo == "tmva_bdt_singleh" or tipo == "tmva_bdt_qcd" :
	y = RooRealVar("y","y",-1.0,1.0) #maa
	y.setBins(50)
	x = RooRealVar("x","x",-1.0,1.0) #maa
	x.setBins(50)

elif "bdth_bdtqcd" in tipo:
	fileref = TFile.Open("{0}/sel_HH_kappa_lambda_1.00/root_HH_kappa_lambda_1.00/shapes.root".format(folder))
	if not fileref : fileref = TFile.Open("{0}/root_HH_kappa_lambda_1.00/shapes.root".format(folder))
	href =  fileref.Get("{2}_{0}_{1}_100{3}".format(selection,tipo,"HH",opt.folderSuffix))
	x = RooRealVar("xbbaa","xbbaa",href.GetXaxis().GetXmin(),href.GetXaxis().GetXmax()) #maa
	x.setBins(href.GetNbinsX()/rebin1) 
	if unfold :
		y = RooRealVar("ybbaa","ybbaa",0,50) #maa
		y.setBins(2500) 
	else :
		y = RooRealVar("ybbaa","ybbaa",href.GetYaxis().GetXmin(),href.GetYaxis().GetXmax()) #maa
		y.setBins(href.GetNbinsY()/rebin2) 
#	x = RooRealVar("xbbaa","xbbaa",-1.0,1.0) #maa
#	x.setBins(50) 
#	if unfold :
#		y = RooRealVar("ybbaa","ybbaa",0,50) #maa
#		y.setBins(2500) 
#	else :
#		y = RooRealVar("ybbaa","ybbaa",-1.0,1.0) #maa
#		y.setBins(50) 
	#v6, v7
	#x = RooRealVar("xbbaa","xbbaa",-0.4,0.55) #maa
	#x.setBins(25) 
	#y = RooRealVar("ybbaa","ybbaa",0.0,0.7) #maa
	#y.setBins(25) 

#	x = RooRealVar("xbbaa","xbbaa",-0.4,0.8) #maa
#	x.setBins(50)
#	y = RooRealVar("ybbaa","ybbaa",0.0,0.8) #maa
#	y.setBins(50)
#	#y = RooRealVar("ybbaa","ybbaa",-0.4,20.0) #maa
#	#y.setBins(625)
#	x = RooRealVar("x","x",-0.22,0.5) #maa
#	x.setBins(18)
#	y = RooRealVar("y","y",0.1,0.5) #maa
#	y.setBins(15)
else :
	y = RooRealVar("y","y",240,1500) #mHH
	y.setBins(75)
### 
if dim == 1 or opt.unfold :
	varList = RooArgList(y)
	varSet = RooArgSet(y)
	#unfold = True
else :
	varList = RooArgList(x,y)
	varSet = RooArgSet(x,y)

if "hhbbaa" in folder : tipo = tipo+"_100"+opt.folderSuffix
else : tipo = tipo+opt.folderSuffix

if opt.inlambda < 1 :
	kl = RooRealVar("kl","kl",opt.inlambda,-0.3,1.2)
elif opt.inlambda > 1.2 :
	kl = RooRealVar("kl","kl",opt.inlambda,0.9,2.0)
elif opt.inlambda > 1.6 :
	kl = RooRealVar("kl","kl",opt.inlambda,1.0,3.5)
else :
	kl = RooRealVar("kl","kl",opt.inlambda,0.7,1.3)

klConst = RooRealVar("klConst","klConst",1.00)
klConst.setConstant(True) 
smearPhoton = RooRealVar("smearPhoton","smearPhoton",1.2756)#1.30292)
datasets = []

alphaMorph = RooRealVar("beff","beff",0,-20,20)

alphaMorphGJ = RooRealVar("beffGJ","beffGJ",0,-20,20)
alphaMorphHH = RooRealVar("beffHH","beffHH",0,-20,20)
alphaMorphSH = RooRealVar("beffSH","beffSH",0,-20,20)

meanG = RooRealVar("meanG","mean of gaussian",125.00)#,124.8,125.2) 
sigmaG = RooFormulaVar("sigmaG","sigmaG","1.0*@0",RooArgList(smearPhoton))#sigmaG= RooRealVar("sigmaG","width of gaussian",1.30292)#,1.12971-2.0/1000.0,1.12971+2.0/1000.0) 
meanG.setConstant()
smearPhoton.setConstant()
gauss = RooGaussian("gauss","gaussian PDF",x,meanG,sigmaG) 
#These values should be retuned for Boosted analysis (and probably for the normal analysis as well...)
###if not opt.constlambda :
###	constL = RooFormulaVar("constL","0.0437283+@0*1.34435-@0*@0*0.695253",RooArgList(kl)) 
###	meanL = RooFormulaVar("meanL","421.557+@0*25.7048",RooArgList(kl)) 
###	sigmaL= RooFormulaVar("sigmaL","135.194-@0*151.369+@0*@0*77.4694",RooArgList(kl)) 
###	expoC= RooFormulaVar("expoC","-0.00585114+@0*0.000626062",RooArgList(kl)) 
###	changer= RooFormulaVar("changer","615.666+@0*77.17",RooArgList(kl)) 
###else :
###	constL = RooFormulaVar("constL","0.0437283+@0*1.34435-@0*@0*0.695253",RooArgList(klConst)) 
###	meanL = RooFormulaVar("meanL","421.557+@0*25.7048",RooArgList(klConst)) 
###	sigmaL= RooFormulaVar("sigmaL","135.194-@0*151.369+@0*@0*77.4694",RooArgList(klConst)) 
###	expoC= RooFormulaVar("expoC","-0.00585114+@0*0.000626062",RooArgList(klConst)) 
###	changer= RooFormulaVar("changer","615.666+@0*77.17",RooArgList(klConst)) 
###landau = LandauExp("LandauExp","LandauExp",y,constL,meanL,sigmaL,expoC,changer)

for klambda in lambdas :
	rates = []
	histos = []
	openString =    "{1}/sel_HH_kappa_lambda_{0:.2f}/root_HH_kappa_lambda_{0:.2f}/shapes.root".format(klambda,folder) 
	openStringUp =    "{1}_beffUp/sel_HH_kappa_lambda_{0:.2f}/root_HH_kappa_lambda_{0:.2f}/shapes.root".format(klambda,folder)
	openStringDo =    "{1}_beffDown/sel_HH_kappa_lambda_{0:.2f}/root_HH_kappa_lambda_{0:.2f}/shapes.root".format(klambda,folder)
	openStringOne = "{1}/sel_HH_kappa_lambda_{0:.2f}/root_HH_kappa_lambda_{0:.2f}/shapes.root".format(1.0,folder)
	openStringOneUp = "{1}/sel_HH_kappa_lambda_{0:.2f}/root_HH_kappa_lambda_{0:.2f}/shapes.root".format(1.0,folder)
	openStringOneDo = "{1}/sel_HH_kappa_lambda_{0:.2f}/root_HH_kappa_lambda_{0:.2f}/shapes.root".format(1.0,folder)
	#if  "boosted" in opt.tipo :
	#	openString = "{1}/root_HH_kappa_lambda_{0:.2f}/shapes.root".format(klambda,folder)
	inFile = TFile.Open(openString)
	inFileUp = TFile.Open(openStringUp)
	inFileDo = TFile.Open(openStringDo)
	inFileOne = TFile.Open(openStringOne)
	inFileOneUp = TFile.Open(openStringOneUp)
	inFileOneDo = TFile.Open(openStringOneDo)
	if not inFile :
		openString =    "{1}/root_HH_kappa_lambda_{0:.2f}/shapes.root".format(klambda,folder)
		inFile = TFile.Open(openString)
	if not inFileUp : 
		openStringUp =    "{1}_beffUp/root_HH_kappa_lambda_{0:.2f}/shapes.root".format(klambda,folder)
		inFileUp = TFile.Open(openStringUp)
	if not inFileDo :
		openStringDo =   "{1}_beffDown/root_HH_kappa_lambda_{0:.2f}/shapes.root".format(klambda,folder) 
		inFileDo = TFile.Open(openStringDo)
	if not inFileOne :
		openStringOne =  "{1}/root_HH_kappa_lambda_{0:.2f}/shapes.root".format(1.0,folder)  
		inFileOne = TFile.Open(openStringOne)
	if not inFileOneUp :
		openStringOneUp =   "{1}_beffUp/root_HH_kappa_lambda_{0:.2f}/shapes.root".format(1.0,folder) 
		inFileOneUp = TFile.Open(openStringOneUp)
	if not inFileOneDo :
		openStringOneDo =   "{1}_beffDown/root_HH_kappa_lambda_{0:.2f}/shapes.root".format(1.0,folder) 
		inFileOneDo = TFile.Open(openStringOneDo)


	print inFile, inFileOne
	outString = "card{0:.2f}_syst{1}_sel{2}{3}.txt".format(klambda,opt.scenario,opt.selection,opt.folderSuffix)
	if "boosted" in opt.tipo : outString = "card{0:.2f}_boosted_syst{1}_sel{2}{3}.txt".format(klambda,opt.scenario,opt.selection,opt.folderSuffix)
	outFile = open(outString,"w")
	#outWS = TFile.Open("hhbbaa/root_HH_kappa_l_{0:.2f}/ws.root","RECREATE")
	ws = RooWorkspace("w")

	allPdfs = []
	for iproc in processes :
		if "HH" in iproc and not "bb" in tipo and opt.parametric and not "boosted" in opt.tipo:
			#do stuff to generate rooprodpdf
			#// Declare variables x,mean,sigma with associated name, title, initial value and allowed range
			print "option parametric disabled"
#			if tipo == "hmaa_mhh" : pdf = RooProdPdf("HH","HH",landau,gauss)
#			elif tipo == "hh_m" : pdf = landau
#			elif tipo == "haa_m" : pdf = gauss
#			pdf.SetNameTitle("HH","HH")
#			allPdfs.append(pdf) 
#			if "boosted" in opt.tipo : rates.append( 1.235831e-04 * 30000000.0) #rates.append(11639.5)
#			else : rates.append (395.634641002) #rates.append(3271.07673397) #rates.append(7239.516396) #rates.append(10211.10624)
#			#wFunc = RooRealVar ("weight","event weight",1) 
#			#tempdata = pdf.generate(RooArgSet(x,y),5009.4*1-15732*1+20938)
#			#datasets.append(tempdata)
#			#wFunc = RooRealVar ("weight","event weight",1) 
#			#tempdata.addColumn(wFunc)
#			#	RooDataSet (const char *name, const char *title, RooDataSet *data, const RooArgSet &vars, const char *cuts=0, const char *wgtVarName=0)
#			#datasets.append(RooDataSet(tempdata.GetName(),tempdata.GetTitle(),tempdata,RooArgSet(x,y,wFunc),"True",wFunc.GetName()))
#			#datasets.append()
		else :
			stringToGet = "{2}_{0}_{1}".format(selection,tipo,iproc)
#			if "bdth_bdtqcd" in tipo :
#				if klambda in inputsprec :
#					number_dec = str(klambda-int(klambda))[2:]
#	    			appString = "{0}{1}0".format(int(klambda),number_dec)
#	    			stringToGet = "{2}_{0}_{1}_{3}".format(selection,tipo,iproc,appString)
#	    		elif "boosted" in opt.tipo : stringToGet = "{2}_{0}_{1}".format(selection,tipo,iproc)
#	    		else : stringToGet = "{2}_{0}_{1}".format(selection,tipo,iproc)
			htemp = inFile.Get(stringToGet)				
			htempUp = inFileUp.Get(stringToGet)
			htempDo = inFileDo.Get(stringToGet)

			if "boosted" in opt.tipo: #remove first bins and last
				hrefNo = TH1F("hrefNo","hrefNo",15,htemp.GetBinLowEdge(10),htemp.GetBinLowEdge(25))
				hrefUp = TH1F("hrefUp","hrefUp",15,htempUp.GetBinLowEdge(10),htempUp.GetBinLowEdge(25))
				hrefDo = TH1F("hrefDo","hrefDo",15,htempDo.GetBinLowEdge(10),htempDo.GetBinLowEdge(25))

				for xbin in range(1,16):
					hrefNo.SetBinContent(xbin,htemp.GetBinContent(xbin+14))
					hrefUp.SetBinContent(xbin,htempUp.GetBinContent(xbin+14))
					hrefDo.SetBinContent(xbin,htempDo.GetBinContent(xbin+14))
				htemp = hrefNo
				htempUp = hrefUp
				htempDo = hrefDo

			print htemp, stringToGet
			oneIntegral = 1.0
			oneUpIntegral = 1.0
			oneDoIntegral = 1.0
			if "HH" in iproc : 
				if not "boosted" in opt.tipo : 
					htempOne = inFileOne.Get("{2}_{0}_{1}".format(selection,tipo,iproc))
					htempOne.Scale(opt.wpScaler)
					htempOneUp = inFileOneUp.Get("{2}_{0}_{1}".format(selection,tipo,iproc))
					htempOneUp.Scale(opt.wpScaler)
					htempOneDo = inFileOneDo.Get("{2}_{0}_{1}".format(selection,tipo,iproc))
					htempOneDo.Scale(opt.wpScaler)
				else : 
					htempOne = inFileOne.Get("{2}_{0}_{1}".format(selection,tipo,iproc))
					htempOneUp = inFileOneUp.Get("{2}_{0}_{1}".format(selection,tipo,iproc))
					htempOneDo = inFileOneDo.Get("{2}_{0}_{1}".format(selection,tipo,iproc))

					#remove first bins
					hrefOneNo = TH1F("hrefOneNo","hrefOneNo",15,htempOne.GetBinLowEdge(10),htempOne.GetBinLowEdge(25))
					hrefOneUp = TH1F("hrefOneUp","hrefOneUp",15,htempOneUp.GetBinLowEdge(10),htempOneUp.GetBinLowEdge(25))
					hrefOneDo = TH1F("hrefOneDo","hrefOneDo",15,htempOneDo.GetBinLowEdge(10),htempOneDo.GetBinLowEdge(25))
				
					for xbin in range(1,16):
						hrefOneNo.SetBinContent(xbin,htempOne.GetBinContent(xbin+14))
						hrefOneUp.SetBinContent(xbin,htempOneUp.GetBinContent(xbin+14))
						hrefOneDo.SetBinContent(xbin,htempOneDo.GetBinContent(xbin+14))
					htempOne = hrefOneNo
					htempOneUp = hrefOneUp
					htempOneDo = hrefOneDo

				htempOne.Scale(30000000.0)
				htempOneUp.Scale(30000000.0)
				htempOneDo.Scale(30000000.0)

				oneIntegral = htempOne.Integral()
				oneIntegralUp = htempOneUp.Integral()
				oneIntegralDo = htempOneDo.Integral()
			#if "boosted" in opt.tipo : 
			#	hout = TH1F(iproc,iproc,40,-0.28,0.6)     
			#	for xbin in range(1,41):     
			#		hout.SetBinContent(xbin,htemp.GetBinContent(10+xbin))     
			#	htemp = hout     
			print "BinningX,y",iproc, htemp.GetNbinsX(), htemp.GetNbinsY()
			if dim == 1 : 
				htemp.Rebin(rebin0)
				htempUp.Rebin(rebin0)
				htempDo.Rebin(rebin0)
			else : 
				htemp.RebinX(rebin1) #5
				htemp.RebinY(rebin2) #5
				htempUp.RebinX(rebin1) #5
				htempUp.RebinY(rebin2) #5
				htempDo.RebinX(rebin1) #5
				htempDo.RebinY(rebin2) #5
				print "Re-BinningX,y",iproc, htemp.GetNbinsX(), htemp.GetNbinsY()
			if unfold :
				print "HOBSUNFOLD"
				#h = TH1F(iproc,iproc,htemp.GetNbinsX()*htemp.GetNbinsY(),htemp.GetXaxis().GetXmin(),htemp.GetXaxis().GetXmax()*htemp.GetNbinsY())
				#hUp = TH1F(iproc+"Up",iproc+"Up",htemp.GetNbinsX()*htemp.GetNbinsY(),htemp.GetXaxis().GetXmin(),htemp.GetXaxis().GetXmax()*htemp.GetNbinsY())
				#hDo = TH1F(iproc+"Do",iproc+"Do",htemp.GetNbinsX()*htemp.GetNbinsY(),htemp.GetXaxis().GetXmin(),htemp.GetXaxis().GetXmax()*htemp.GetNbinsY())
				h = TH1F(iproc,iproc,htemp.GetNbinsX()*htemp.GetNbinsY(),0,50)
				hUp = TH1F(iproc+"Up",iproc+"Up",htemp.GetNbinsX()*htemp.GetNbinsY(),0,50)
				hDo = TH1F(iproc+"Do",iproc+"Do",htemp.GetNbinsX()*htemp.GetNbinsY(),0,50)
				ibin=1
				for xbin in range(1,htemp.GetNbinsX()+1) :
					for ybin in range(1,htemp.GetNbinsY()+1) :
						h.SetBinContent(ibin,htemp.GetBinContent(xbin,ybin))
						if htemp.GetBinContent(xbin,ybin) < 0 : print "ALLARMEALLARMEALLARMEALLARMEALLARMEALLARMEALLARMEALLARME"
						hUp.SetBinContent(ibin,htempUp.GetBinContent(xbin,ybin))
						hDo.SetBinContent(ibin,htempDo.GetBinContent(xbin,ybin))
						ibin += 1
			else : 
				h = htemp   #QUICORREZBIN
				hUp = htempUp   #QUICORREZBIN
				hDo = htempDo   #QUICORREZBIN
#				if not "boosted" in opt.tipo : h = htemp
#				else : 
#					h = TH1F(iproc,iproc,44,380,2140)
#					for ibin in range(0,44) :
#						h.SetBinContent(ibin,htemp.GetBinContent(ibin+8))
#			if "bdth_bdtqcd" in opt.tipo : 
#				#rescale to remove empty areas: -0.22:0.5 X 0.1:0.5
#				nbx = 18
#				nby = 15
#				h = TH2F(iproc,iproc,nbx,-0.22,0.5,nby,0.1,0.5)
#				for xbin in range(0,nbx) :
#					for ybin in range(0,nby): 
#						h.SetBinContent(xbin+1,ybin+1, htemp.GetBinContent( htemp.FindBin( h.GetXaxis().GetBinCenter(xbin+1),h.GetYaxis().GetBinCenter(xbin+1) ) ) )
#				#h.RebinX(2)
#				#h.RebinY(3)
			print "Binning",iproc, h.GetNbinsX()
			h.SetName(iproc)
			h.SetTitle(iproc)
			hUp.SetName(iproc+"beffUp")
			hUp.SetTitle(iproc+"beffUp")
			hDo.SetName(iproc+"beffDown")
			hDo.SetTitle(iproc+"beffDown")
			#if iproc == "HH" : 
	 		#print "scaling"
			print h.Integral(), 30000000.0*h.Integral()
	 		h.Scale(30000000.0)
	 		hUp.Scale(30000000.0)
	 		hDo.Scale(30000000.0)
	 		#if "boosted" in opt.tipo and "QCD" in iproc : h.Scale(0.001)
	 		if "HH" in iproc and not "boosted" in opt.tipo : 
	 			h.Scale(opt.wpScaler)
	 			hUp.Scale(opt.wpScaler)
	 			hDo.Scale(opt.wpScaler)
	 		if "ggjj" in iproc and not "boosted" in opt.tipo: 
	 			h.Scale(opt.wpScaler)
	 			hUp.Scale(opt.wpScaler)
	 			hDo.Scale(opt.wpScaler)
	 		if "jgjj" in iproc and not "boosted" in opt.tipo: 
	 			h.Scale(TMath.Sqrt(opt.wpScaler))
	 			hUp.Scale(TMath.Sqrt(opt.wpScaler))
	 			hDo.Scale(TMath.Sqrt(opt.wpScaler))
	 		#if ("jgjj" in iproc or "ggjj" in iproc or "QCD" in iproc) : #QUI ricontrollare
	 		#	#h.Scale(0.895)
	 		#	if "jgjj" in iproc : h.Scale(applyjgjjScaler)
	 		#	if "ggjj" in iproc : h.Scale(applyggjjScaler)
	 		#	integral_pre = h.Integral()
	 		#	h.Smooth()
	 		#	h.Scale(integral_pre/h.Integral())
	 		print h.Integral()
			#if tipo == "haa_m" : rates.append(h.Integral(h.FindBin(120),h.FindBin(130)))
			#htoappend = h.Rebin(4*dim)
			if dim == 1: 
				for xbin in range(1,h.GetNbinsX()+1) :
	 				if h.GetBinContent(xbin)<=0 : 
	 					if "QCD" in iproc : h.SetBinContent(xbin,h.GetBinContent(xbin-1)/2.0) #1.7*30000000)
	 					else : h.SetBinContent(xbin,0.000001)
	 				if hUp.GetBinContent(xbin)<=0 : 
	 					if "QCD" in iproc : hUp.SetBinContent(xbin,hUp.GetBinContent(xbin-1)/2.0) #1.7*30000000)
	 					else : hUp.SetBinContent(xbin,0.000001)
	 				if hDo.GetBinContent(xbin)<=0 : 
	 					if "QCD" in iproc : hDo.SetBinContent(xbin,hDo.GetBinContent(xbin-1)/2.0) #1.7*30000000)
	 					else : hDo.SetBinContent(xbin,0.000001)
#	 				if h.GetBinContent(xbin)<=0 : 
#	 					if "QCD" in iproc : h.SetBinContent(xbin,1.7*30000000.) #1.7*30000000)
#	 					else : h.SetBinContent(xbin,0.000001)
#	 				if hUp.GetBinContent(xbin)<=0 : 
#	 					if "QCD" in iproc : hUp.SetBinContent(xbin,1.7*30000000.) #1.7*30000000)
#	 					else : hUp.SetBinContent(xbin,0.000001)
#	 				if hDo.GetBinContent(xbin)<=0 : 
#	 					if "QCD" in iproc : hDo.SetBinContent(xbin,1.7*30000000.) #1.7*30000000)
#	 					else : hDo.SetBinContent(xbin,0.000001)
	 				#if "QCD" in iproc and xbin == 36: h.SetBinContent(xbin,220000000.)
	 				#elif "QCD" in iproc and xbin == 37: h.SetBinContent(xbin,150000000.)
	 				#elif "QCD" in iproc and xbin == 38: h.SetBinContent(xbin,110000000.)
	 				#elif "QCD" in iproc and xbin == 39: h.SetBinContent(xbin,75000000.)
	 				#elif "QCD" in iproc and xbin == 40: h.SetBinContent(xbin,50000000.)
	 				#if "QCD" in iproc : print xbin, h.GetBinContent(xbin)
	 		else : 
	 			valueFiller = 0.00001
	 			#if ((not "boosted" in opt.tipo ) and (opt.wpScaler < 0.99)):
	 			if "jgjj" in iproc : valueFiller = 27.0*opt.wpScaler #0.00001 # QUI->27 
	 			elif "ggjj" in iproc : valueFiller = 13.0*opt.wpScaler #0.00001 # QUI->27
	 				#if "HH" in iproc : 
	 			#if "jgjj" in iproc and not "boosted" in opt.tipo: valueFiller = 30*0.895*applyjgjjScaler/10 #factor 10 to reduce its importance
				for xbin in range(1,h.GetNbinsX()+1) :
					for ybin in range(1,h.GetNbinsY()+1) :
	 					#if h.GetBinContent(xbin,ybin)<=0 and not "HH" in iproc: h.SetBinContent(xbin,ybin,valueFiller)
	 					if h.GetBinContent(xbin,ybin)<=0 : 
	 						h.SetBinContent(xbin,ybin,valueFiller)
	 					if hUp.GetBinContent(xbin,ybin)<=0 : 
	 						hUp.SetBinContent(xbin,ybin,valueFiller*oneIntegralUp/oneIntegral)
	 					if hDo.GetBinContent(xbin,ybin)<=0 : 
	 						hDo.SetBinContent(xbin,ybin,valueFiller*oneIntegralDo/oneIntegral)

			if "HH"in iproc : 
				h.Scale(oneIntegral/h.Integral())
				hUp.Scale(oneIntegralUp/hUp.Integral())
				hDo.Scale(oneIntegralDo/hDo.Integral())
				hobs = h.Clone("obs")
			elif not "obs" in iproc  : hobs.Add(h) 
			else : 
				h = hobs 
				h.SetName("data_obs")
				h.SetTitle("data_obs")
				histos.append(h)
			#else : hobs = h 
			#print "Normalizations", h.Integral(), h.Integral(h.FindBin(120),h.FindBin(130))
			rdh = RooDataHist(iproc+"rdh",iproc+"rdh",varList,h)
			rdhUp = RooDataHist(iproc+"rdhUp",iproc+"rdhUp",varList,hUp)
			rdhDo = RooDataHist(iproc+"rdhDo",iproc+"rdhDo",varList,hDo)
			if "boosted" in opt.tipo and "single" in iproc : 
				rdh.SetNameTitle(iproc+"rdhboosted",iproc+"rdhboosted")
				rdhUp.SetNameTitle(iproc+"rdhboosted"+"Up",iproc+"rdhboosted"+"Up")
				rdhDo.SetNameTitle(iproc+"rdhboosted"+"Down",iproc+"rdhboosted"+"Down")

			if opt.tipo == "hh_m" : rates.append(h.Integral(h.FindBin(240),h.FindBin(1500)))
			else : rates.append(h.Integral())

			if not "obs" in iproc : 
				histos.append(h)
				histos.append(hUp)
				histos.append(hDo)

				if "HH" in iproc and tipo == "hmaa_mbb" and opt.parametric :
					#qui fare la conditional rooprodpdf
					#if tipo == "hmbb_mhh" : pdf = RooProdPdf("HH","HH",landau,gauss) #questo non esiste perche non ha senso
					#elif tipo == "hbb_m" : pdf = RooHistPdf(iproc,iproc,varSet,rdh)
					#elif tipo == "hmaa_mbb":
					pdftemp = RooHistPdf(iproc+"temp",iproc+"temp",varSet,rdh)
					pdf = RooProdPdf("HH","HH",RooArgSet(gauss),RooFit.Conditional(RooArgSet(pdftemp),RooArgSet(y)) )
				else : 
					#if "boosted" in opt.tipo and "single" in iproc : 
					#	pdf = RooHistPdf(iproc+"boosted",iproc+"boosted",varSet,rdh)
					#	pdfUp = RooHistPdf(iproc+"boostedbeffUp",iproc+"boostedbeffUp",varSet,rdhUp)
					#	pdfDo = RooHistPdf(iproc+"boostedbeffDown",iproc+"boostedbeffDown",varSet,rdhDo)
					#else : 
					#	pdf = RooHistPdf(iproc,iproc,varSet,rdh  )
					#	pdfUp = RooHistPdf(iproc+"beffUp",iproc+"beffUp",varSet,rdhUp  )
					#	pdfDo = RooHistPdf(iproc+"beffDown",iproc+"beffDown",varSet,rdhDo  )
					tmppdf = RooHistPdf(iproc+"tmp",iproc+"tmp",varSet,rdh  )
					tmppdfUp = RooHistPdf(iproc+"beffUp"+"tmp",iproc+"beffUp"+"tmp",varSet,rdhUp  )
					tmppdfDo = RooHistPdf(iproc+"beffDown"+"tmp",iproc+"beffDown"+"tmp",varSet,rdhDo  )
					if not unfold :
						#sigTemplateMorphPdf_ggH = ROOT.FastVerticalInterpHistPdf2D(TemplateName,TemplateName,CMS_zz4l_mass,D,true,funcList_ggH,morphVarListSig,1.0,1)
						if "boosted" in opt.tipo :
							pdf =  tmppdf
							pdfUp =  tmppdfUp
							pdfDo =  tmppdfDo
							pdf.SetNameTitle(iproc,iproc)
							if "single" in iproc :
								pdf.SetNameTitle(iproc+"boosted",iproc+"boosted")
								pdfUp.SetNameTitle(iproc+"boostedbeffSHUp",iproc+"boostedbeffSHUp")
								pdfDo.SetNameTitle(iproc+"boostedbeffSHDown",iproc+"boostedbeffSHDown")
							elif "Z" in iproc :
								pdfUp.SetNameTitle(iproc+"beffZUp",iproc+"beffZUp")
								pdfDo.SetNameTitle(iproc+"beffZDown",iproc+"beffZDown")
							elif "HH" in iproc :
								pdfUp.SetNameTitle(iproc+"beffHHUp",iproc+"beffHHUp")
								pdfDo.SetNameTitle(iproc+"beffHHDown",iproc+"beffHHDown")
							elif "QCD" in iproc :
								pdfUp.SetNameTitle(iproc+"beffQCDUp",iproc+"beffQCDUp")
								pdfDo.SetNameTitle(iproc+"beffQCDDown",iproc+"beffQCDDown")
							else :
								pdfUp.SetNameTitle(iproc+"beffTopUp",iproc+"beffTopUp")
								pdfDo.SetNameTitle(iproc+"beffTopDown",iproc+"beffTopDown")
							if opt.v45setup : 
								if "single" in iproc :
									pdfUp.SetNameTitle(iproc+"boostedbeffUp",iproc+"boostedbeffUp")
									pdfDo.SetNameTitle(iproc+"boostedbeffDown",iproc+"boostedbeffDown")
								else:
									pdfUp.SetNameTitle(iproc+"beffUp",iproc+"beffUp")
									pdfDo.SetNameTitle(iproc+"beffDown",iproc+"beffDown")
							getattr(ws,'import')(pdfUp,RooFit.RecycleConflictNodes())								
							getattr(ws,'import')(pdfDo,RooFit.RecycleConflictNodes())								
							#pdf = FastVerticalInterpHistPdf(iproc,iproc,y,RooArgList(tmppdf,tmppdfUp,tmppdfDo),RooArgList(alphaMorph))
							#if "single" in iproc : tmppdf.SetNameTitle(iproc+"boosted",iproc+"boosted")
						elif opt.v45setup : pdf = FastVerticalInterpHistPdf2D(iproc,iproc,x,y,False,RooArgList(tmppdf,tmppdfUp,tmppdfDo),RooArgList(alphaMorph),1.,-1)
						elif "single" in iproc : pdf = FastVerticalInterpHistPdf2D(iproc,iproc,x,y,False,RooArgList(tmppdf,tmppdfUp,tmppdfDo),RooArgList(alphaMorphSH),1.,-1)
						elif "HH" in iproc : pdf = FastVerticalInterpHistPdf2D(iproc,iproc,x,y,False,RooArgList(tmppdf,tmppdfUp,tmppdfDo),RooArgList(alphaMorphHH),1.,-1)
						else : pdf = FastVerticalInterpHistPdf2D(iproc,iproc,x,y,False,RooArgList(tmppdf,tmppdfUp,tmppdfDo),RooArgList(alphaMorphGJ),1.,-1)
						
						#pdf = RooProdPdf(iproc,iproc,RooArgSet(tmppdfX),RooFit.Conditional(RooArgSet(tmppdf),RooArgSet(y)) )
						#pdfUp = RooProdPdf(iproc+"beffUp",iproc+"beffUp",RooArgSet(tmppdfUpX),RooFit.Conditional(RooArgSet(tmppdfUp),RooArgSet(y)) )
						#pdfDo = RooProdPdf(iproc+"beffDown",iproc+"beffDown",RooArgSet(tmppdfDoX),RooFit.Conditional(RooArgSet(tmppdfDo),RooArgSet(y)) )
					else :
						"SONO NELLELSE"
						pdf = tmppdf
						#pdfUp = tmppdfUp
						#pdfDo = tmppdfDo
						pdf.SetNameTitle(iproc,iproc)
						#pdfUp.SetNameTitle(iproc+"beffUp",iproc+"beffUp")
							#pdfDo.SetNameTitle(iproc+"beffDown",iproc+"beffDown")
				pdf.Print()
				allPdfs.append(pdf)
				print "generating"
				#datasets.append(pdf.generate(RooArgSet(x,y),h.Integral()))
				print "LEN ", len(allPdfs)
			else : 
				pdf = rdh
				print "Normalizations", rdh.sumEntries(), h.Integral()
				pdf.SetNameTitle("data_obs","data_obs")
				pdf.SetName("data_obs")
				pdf.SetTitle("data_obs")

				#pdf = datasetFull
		getattr(ws,'import')(pdf,RooFit.RecycleConflictNodes())
		if opt.tipo == "boosted" :
			#rfvSigRate_HH = RooFormulaVar("HH_norm","-0.4673*@0 + 1.485",RooArgList(kl)) #RooFormulaVar("HH_norm","-0.4875*@0 + 1.4883",RooArgList(kl))
			#rfvSigRate_HH = RooFormulaVar("HH_norm","-0.4673*@0 + 1.4673",RooArgList(kl)) #RooFormulaVar("HH_norm","-0.4875*@0 + 1.4883",RooArgList(kl))
			#rfvSigRate_HH = RooFormulaVar("HH_norm","-0.392*@0 + 1.392",RooArgList(kl)) #v4: 0.3841
			#rfvSigRate_HH = RooFormulaVar("HH_norm","AAA*@0*@0 + (BBB-2.0*AAA)*@0 +AAA + 1.0 - BBB",RooArgList(kl)) #v4: 0.3841
			#rfvSigRate_HH = RooFormulaVar("HH_norm","0.1378*@0*@0 + (-0.3894-2.0*0.1378)*@0 +0.1378 + 1.0 + 0.3894",RooArgList(kl)) #v4: 0.3841
			rfvSigRate_HH = RooFormulaVar("HH_norm",getRatebbbb(getScenario(opt.folderSuffix),getBwP_bbbb(opt.folderSuffix),""),RooArgList(kl)) #v4: 0.3841
		else : #y = -0,6302x + 1,6307
			#rfvSigRate_HH = RooFormulaVar("HH_norm","1.6096-0.6081*@0",RooArgList(kl))
			#rfvSigRate_FCC = RooFormulaVar("HH_norm","-0.7493*@0 + 1.7493",RooArgList(kl))  #y =   # 1.6307-0.6302*@0 #0.476
			#rfvSigRate_FCC = RooFormulaVar("HH_norm","-0.676*@0 + 1.676",RooArgList(kl))  #y =   # 1.6307-0.6302*@0 #0.476
			#rfvSigRate_FCC = RooFormulaVar("HH_norm","0.2213*@0*@0 + (-0.7014-2.0*0.2213)*@0 +0.2213 + 1.0 + 0.7014",RooArgList(kl))  #v5 y = a x2 + (b-2a)x +a+1-b
			#rfvSigRate_FCC = RooFormulaVar("HH_norm","0.1918*@0*@0 + (-0.6733-2.0*0.1918)*@0 +0.1918 + 1.0 + 0.6733",RooArgList(kl))  #v6 y = a x2 + (b-2a)x +a+1-b
			#rfvSigRate_FCC = RooFormulaVar("HH_norm","0.1881*@0*@0 + (-0.6925-2.0*0.1881)*@0 +0.1881 + 1.0 + 0.6925",RooArgList(kl))  #v7 y = a x2 + (b-2a)x +a+1-b
			#rfvSigRate_FCC = RooFormulaVar("HH_norm","0.2228*@0*@0 + (-0.7121-2.0*0.2228)*@0 +0.2228 + 1.0 + 0.7121",RooArgList(kl))  #v7_1 y = a x2 + (b-2a)x +a+1-b
			#rfvSigRate_FCC = RooFormulaVar("HH_norm","0.2222*@0*@0 + (-0.7114-2.0*0.2222)*@0 +0.2222 + 1.0 + 0.7114",RooArgList(kl))  #v7_2 y = a x2 + (b-2a)x +a+1-b
			rfvSigRate_FCC = RooFormulaVar("HH_norm",getRatebbaa(getScenario(opt.folderSuffix),getBwP_bbaa(opt.folderSuffix),getPwP(opt.folderSuffix)),RooArgList(kl))  #v58 y = a x2 + (b-2a)x +a+1-b
			rfvSigRate_HELHC = RooFormulaVar("HH_norm","-0.6136*@0 + 1.6694",RooArgList(kl)) 
			rfvSigRate_HH = rfvSigRate_FCC
		getattr(ws,'import')(rfvSigRate_HH,RooFit.RecycleConflictNodes())
		#if iproc = "HH" : obs = inFile.Get("{2}_{0}_{1}".format(sel,tipo,iproc)).Clone("data_obs")
		#else : obs.Add(inFile.Get("{2}_{0}_{1}".format(sel,tipo,iproc)))
		
	dd = createDict()
	print rates
	print "Created dictionary of systematics"
	#listOfProc = ["HH", "jgjj", "ggjj", "ttH", "ggH", "VH"] #dovrei crearla da processes droppando data_obs ma ok
	listOfProc = processes[:-1] #dovrei crearla da processes droppando data_obs ma ok
	channelID = "ch4"
	if opt.tipo == "boosted" : channelID = "ch5"
	scenarioID = "optimist"
	if opt.scenario == 2 : scenarioID = "intermediate"
	elif opt.scenario == 3 : scenarioID = "pessimistic"
	#nuisances = ["xsec_tt","xsec_ttH","xsec_QCD","xsec_Zbb","gamma_ID","tauEff","lepton_ID","lumi","jets_ID","btagaa","xsec_HH"]
	nuisances = ["xsec_ttH","gamma_ID","lumi","xsec_HH"]
	if opt.tipo == "boosted" : 
		nuisances = ["xsec_tt","xsec_ttH","xsec_Zbb","lumi","xsec_HH","xsec_ZZ"]
		#nuisances = ["xsec_tt","xsec_ttH","xsec_QCD","xsec_Zbb","gamma_ID","tauEff","lepton_ID","lumi","jets_ID","btagbb","xsec_HH"]
	#obs.SetName("data_obs")
	#obs.SetTitle("data_obs")
	#ws.writeToFile("hhbbaa/root_HH_kappa_l_{0:.2f}/ws.root".format(klambda))
	print "starting card"
	outFile.write("imax 1\n")
	if opt.tipo == "boosted" :outFile.write("jmax 5\n")
	else: 
		outFile.write("jmax 3\n")
	outFile.write("kmax *\n")
	outFile.write("----------------------\n")
	if opt.tipo == "boosted" :  outFile.write("shapes * * ws{0:.2f}_sel{2}{3}_boosted.root w:$PROCESS w:$PROCESS$SYSTEMATIC \n".format(opt.inlambda,folder,opt.selection,opt.folderSuffix))
	#else  :  outFile.write("shapes * * {1}/sel_HH_kappa_lambda_{0:.2f}/root_HH_kappa_lambda_{0:.2f}/ws{2}.root $PROCESS $PROCESS$SYSTEMATIC \n".format(opt.inlambda,folder,opt.selection,opt.folderSuffix))
	else  :  outFile.write("shapes * * ws{0:.2f}_sel{2}{3}.root w:$PROCESS w:$PROCESS$SYSTEMATIC \n".format(opt.inlambda,folder,opt.selection,opt.folderSuffix))
	#else : outFile.write("shapes * * {1}/sel_HH_kappa_lambda_{0:.2f}/root_HH_kappa_lambda_{0:.2f}/shapes.root $PROCESS_sel0_bdth_bdtqcd \n".format(klambda,folder))
	outFile.write("----------------------\n")
	outFile.write("bin bin1\n")
	#if opt.tipo == "boosted" : outFile.write("observation {0}\n".format(rates[len(rates)-1]))
	#else : outFile.write("observation -1\n")
	outFile.write("observation {0}\n".format(rates[len(rates)-1]))
	outFile.write("------------------------------\n")
		
	if opt.tipo == "boosted" : 
		outFile.write("bin             bin1      bin1       bin1       bin1      bin1       bin1      \n")	
		outFile.write("process         HH        singleHboosted    ZZ        ttbar       Zbb     QCD     \n") #	processes = ["HH","singleH","EWK","ttbar","QCDEWK","QCD","data_obs"]processes = ["HH","singleH","ZZ","ttbar","Zbb","QCD","data_obs"] #->verificare che ci siano tutte le syst nel dict
		outFile.write("process         0          1        2           3          4            5\n")
		outFile.write("rate            {0} {1} {2} {3} {4} {5}\n".format(rates[0],rates[1],rates[2],rates[3],rates[4],rates[5])) #"HH","singleH","QCD","EWK","QCDEWK","ttbar"
	else : 
		outFile.write("bin             bin1  bin1 bin1  bin1   \n")	
		outFile.write("process         HH     jgjj ggjj singleH\n") #"HH","jgjj","ggjj","singleH"
		outFile.write("process         0       1    2    3 \n")
		outFile.write("rate            {0}    {1}   {2} {3}\n".format(rates[0],rates[1],rates[2],rates[3]))
		#outFile.write("bin             bin1    bin1   \n")	
		#outFile.write("process         HH      jgjj\n") #"HH","jgjj","ggjj","singleH"
		#outFile.write("process         0       1     \n")
		#outFile.write("rate            {0}    {1}   \n".format(rates[0],rates[1]))
	outFile.write("--------------------------------\n")
#	else : 
#		outFile.write("bin             bin1  bin1 bin1  bin1 bin1 bin1\n")	
#		outFile.write("process         HH        jgjj ggjj ttH ggH VH\n")
#		outFile.write("process         0          1 2 3 4 5\n")
#		outFile.write("rate            {0} {1} {2} {3} {4} {5}\n".format(rates[0],rates[1],rates[2],rates[3],rates[4],rates[5]))
#	outFile.write("--------------------------------\n")
	#outFile.write("lumiSig     lnN    1.01       - \n")
	#outFile.write("lumiSig     lnN    1.01 - - - - - \n")
	
	if opt.tipo == "boosted" : 
		if opt.v45setup :
			outFile.write("beff shape 1 1 1 1 1 1 \n")
		else :
			outFile.write("beffHH shape 1 - - - - - \n")
			outFile.write("beffZ shape - - 1 - 1 - \n")
			outFile.write("beffTop shape - - - 1 - - \n")
			outFile.write("beffQCD shape - - - - - 1 \n")
			outFile.write("beffSH shape - 1 - - - - \n")
		#outFile.write("lumiAll     lnN    1.01 - 1.01 -\n")
		for nuis in nuisances : 
			outFile.write("{6}     lnN     {0}  {1}  {2}  {3}  {4}  {5}\n".format(dd[scenarioID,channelID,listOfProc[0],nuis],dd[scenarioID,channelID,listOfProc[1],nuis],dd[scenarioID,channelID,listOfProc[2],nuis],dd[scenarioID,channelID,listOfProc[3],nuis],dd[scenarioID,channelID,listOfProc[4],nuis],dd[scenarioID,channelID,listOfProc[5],nuis],nuis)) #dd [( scenarioID,channel[iArray],process[iArray],listOfNuis[nuis] )] = listOfNuisArr[nuis][iArray]	
		#outFile.write("BkgScaler rateParam * QCD 1.0 \n")
		#outFile.write("BkgScaler rateParam * Zbb 1.0 \n")
		#outFile.write("BkgScaler rateParam * ZZ 1.0 \n")
		#outFile.write("fakeScaler rateParam * * 0.7 \n")
	else : 
		if opt.v45setup :
			outFile.write("beff param 0  1  [-3,3] \n")
		else :
			outFile.write("beffGJ param 0  1  [-3,3]\n")
			outFile.write("beffHH param 0  1  [-3,3]\n")
			outFile.write("beffSH param 0  1  [-3,3]\n")
			#outFile.write("beffgj lnN - - 1.02200884289/0.978192838685 -\n")
			#outFile.write("beffjg lnN - 1.02126330711/0.97890916122 - -\n")
			#outFile.write("beffsh lnN - - - 1.02253063332/0.977691511675\n")
			#outFile.write("beffhh lnN 1.02188540216/0.978335238561 - - -\n")

		for nuis in nuisances : 
			print dd[scenarioID,channelID,listOfProc[0],nuis],dd[scenarioID,channelID,listOfProc[1],nuis],dd[scenarioID,channelID,listOfProc[2],nuis],dd[scenarioID,channelID,listOfProc[3],nuis],nuis
			outFile.write("{4}     lnN    {0} {1} {2} {3} \n".format(dd[scenarioID,channelID,listOfProc[0],nuis],dd[scenarioID,channelID,listOfProc[1],nuis],dd[scenarioID,channelID,listOfProc[2],nuis],dd[scenarioID,channelID,listOfProc[3],nuis],nuis)) #dd [( scenarioID,channel[iArray],process[iArray],listOfNuis[nuis] )] = listOfNuisArr[nuis][iArray]	
			#outFile.write("{2}     lnN    {0} {1}  \n".format(dd[scenarioID,channelID,listOfProc[0],nuis],dd[scenarioID,channelID,listOfProc[1],nuis],nuis)) #dd [( scenarioID,channel[iArray],process[iArray],listOfNuis[nuis] )] = listOfNuisArr[nuis][iArray]	
		#outFile.write("lumiAll     lnN    1.01 - - 1.01 1.01 1.01\n")
		#outFile.write("lumiTwoAll  lnN    1.02 - - 1.02 1.02 1.02\n")
		outFile.write("BkgScaler_bbaa rateParam * jgjj 1.0 \n")
		outFile.write("BkgScaler_bbaa rateParam * ggjj 1.0 \n")
#		#outFile.write("BkgScaler rateParam * ttH 1.0 \n")
#		outFile.write("fakeRater rateParam * jgjj 1.0 \n")
#		outFile.write("effScaler rateParam * HH 0.8 \n") #NB questa mi sa che devo toglierla proprio no? O basta fissarla a 1? Devo fare delle prove
##		outFile.write("effScaler rateParam * ttH 0.8 \n")
##		outFile.write("effScaler rateParam * VH 0.8 \n")
##		outFile.write("effScaler rateParam * ggH 0.8 \n")
#		outFile.write("effScaler rateParam * ggjj 0.8 \n")
#		outFile.write("effScaler rateParam * jgjj 0.895 \n")
##		outFile.write("btagger   rateParam * ttH 1.0 \n")
##		outFile.write("btagger   rateParam * VH 1.0 \n")
##		outFile.write("btagger   rateParam * ggH 1.0 \n")
#		outFile.write("btagger   rateParam * HH 1.0 \n")

	print "card done"
	#outFile.write("bgnorm   lnN    1.00       1.3\n")
	#name rateParam bin process initial_value
	# outWS = TFile.Open("{1}/root_HH_kappa_lambda_{0:.2f}/ws{2}.root".format(klambda,folder,opt.selection),"RECREATE")
	# outWS.cd()
	# for h in histos :
	# 	h.Write()
	# print "wrote histograms"
	# outWS.Close()
	#if opt.scenario == 2 :
	if opt.tipo == "boosted" :  ws.writeToFile("ws{0:.2f}_sel{1}{2}_boosted.root".format(opt.inlambda,opt.selection,opt.folderSuffix))
	else  :  ws.writeToFile("ws{0:.2f}_sel{1}{2}.root".format(opt.inlambda,opt.selection,opt.folderSuffix))
	ws =0



#
#	zbbscaler rateParam bin1 Zbb 1.0
#QCDscaler rateParam bin1 QCD 1.0
#ttscaler rateParam bin1 ttbar 1.0
#shscaler rateParam bin1 singleHboosted 1.0


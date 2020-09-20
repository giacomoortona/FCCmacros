from ROOT import *
import os,re, optparse


def parseOptions():

    usage = ('usage: %prog [options] datasetList\n'+ '%prog -h for help')
    parser = optparse.OptionParser(usage)
    parser.add_option('-c', '--channel', dest='channel', type='string', default="bbaa", help='bbaa, bbbb, bbtahtal, bbtahtah')


    global opt, args
    (opt, args) = parser.parse_args()

#missing bbaa: 	   0.40 
#missing bbtahtah: NONE
#missing bbtahtal: 1.30 1.50 1.60
#missing bbbb:	   1.02 1.03 1.30 1.45 1.50
#missing total :   0.40 1.02 1.03 1.30 1.43
parseOptions()
global opt, args


#print "non voglio piu girare"
#return
#lambdas = [1.0,0.5,0.9,0.95,1.03,1.05,1.1,1.5]
#lambdas = [1.0,0.9,0.95,0.96,0.97,0.98,0.99,1.01,1.02,1.03,1.04,1.05,1.1]
#lambdas = [1.0,0.9,0.95,0.96,0.97,0.98,0.99,1.01,1.02,1.03,1.04,1.05,1.1]
lambaboos = [] #[1.0,0.5,0.9,0.95,1.05,1.1,1.5,2.00]
#lambdas = [0.5,0.75,0.8,0.875,0.9,0.925,0.95,0.975,1,1.025,1.05,1.075,1.1,1.125,1.15,1.2,1.25,1.5] ##HELHC
#lambdas = [1.0,0.0,0.2,0.4,0.6,0.7,0.8,0.85,0.9,0.92,0.94,0.96,0.97,0.98,0.99,1.01,1.02,1.03,1.04,1.06,1.08,1.1,1.2,1.3,1.4,1.45,1.5,1.55,1.60,1.7,1.9,2.00,2.2,2.4,2.6,2.8,3.0]
lambdas = [1.0,0.0,0.2,0.4,0.6,0.7,0.8,0.85,0.9,0.92,0.94,0.96,0.97,0.98,0.99,1.01,1.02,1.03,1.04,1.06,1.08,1.1,1.2,1.3,1.4,1.45,1.5,1.55,1.60,1.7,1.9,2.00,2.2,2.4,2.6,2.8,3.0]
lambdas = [1.00,0.85,0.98,1.04,1.40,1.80,2.80,0.20,0.90,0.99,1.06,1.45,1.90,3.00,0.40,0.92,0.00,1.08,1.50,2.00,0.60,0.94,1.01,1.10,1.55,2.20,0.70,0.96,1.02,1.20,1.60,2.40,0.80,0.97,1.03,1.30,1.70,2.60]
lambdas = [1.00,0.00,0.20,0.40,0.60,0.70,0.80,0.85,0.90,0.92,0.96,0.97,0.98,0.99,1.01,1.02,1.03,1.04,1.06,1.08,1.10,1.20,1.30,1.40,1.45,1.50,1.55,1.70,1.90,2.00,2.20,2.40,2.60,2.80,3.00]
#lambdas = [1.0]

#startDir = "hhbbtahtal_v6/"
#startDir = "FCCworkshop3/hhbbtahtah/"
#startDir = "FCCworkshop3/hhbbbb_v3/"
#startDir = "FCCworkshop3/hhbbtahtal/"	
#startDir = "FCCworkshop3/hhbbaa_v7_2/"	
startDirList = []
scenarios = ['I','II','III']
beffpoints = ["","_beffDown","_beffUp"]
#btagWPs = ['L','M','T']
#photonWPs = ["M","T"] #[""] #['M','T']
#if opt.channel == "bbbb" :
#	photonWPs = [""]
#elif "bbta" in opt.channel :
#	photonWPs = ['L','M','T']
btagWPs = ['M','T']
photonWPs = ["M","T"] #[""] #['M','T']
if opt.channel == "bbbb" :
	photonWPs = [""]

#>: error flushing file /eos/user/s/selvaggi/Analysis/hh_comb/hhbbtahtah_v58/hhbbtahtah_II_TL_beffDown/sel_HH_kappa_lambda_0.85/root_HH_kappa_lambda_0.85/shapes.root (Protocol error)
#lambdas = [1.00]#
#btagWPs =["M"]
#photonWPs=["T"]
#beffpoints= ["_beffDown"]
#scenarios = ['III']

print "starting", opt.channel
for sc in scenarios:
    for bwp in btagWPs:
        for pwp in photonWPs:
        	for beff in beffpoints:
        		#hhbbaa_III_LT/sel_HH_kappa_lambda_1.00/root_HH_kappa_lambda_1.00
        		startDirList.append('/eos/user/s/selvaggi/Analysis/hh_comb/hh{}_v58/hh{}_{}_{}{}{}/'.format(opt.channel,opt.channel,sc,bwp,pwp,beff))

#processes = ["ggH","ttH","zjets","ZZ","ttbar","VH"]	 
#processes = ["singleH","zjets","ZZ","ttbar","ttV","ttVV"]	 #bbtahtah processes
#processes = ["singleH","EWK","ttbar","QCDEWK","QCD"] 
#processes = ["singleH","ZZ","ttbar","Zbb","QCD"]	 #bbbb processes
processes = ["ggjj","jgjj","singleH"]	  #bbaa processes
if "bbta" in opt.channel :
	processes = ["singleH","zjets","ZZ","ttbar","ttV","ttVV"]	 #bbtahtal processes
elif "bbbb" in opt.channel :
	processes = ["singleH","ZZ","ttbar","Zbb","QCD"]

#upRange = 3 #bbtt
#upRange = 3 #bbbb
upRange = 1 #bbaa
#upRange = 1 #bbtahtal

bdtPoints = ["100"]
#bdtPoints = [
#  "000",
#  "040",
#  "070",
#  "100",
#  "130",
#  "150",
#  "170",
#  "200",
#  "220",
#  "240",
#  "260",
#  "300",
#]
tipi = []#"haa_m","hh_m","hmaa_mhh","hmaa_mbb","hbb_m"]
for suff in bdtPoints :
	tipi.append("tmva_bdt_qcd_"+suff)
	tipi.append("tmva_bdt_singleh_"+suff)
	tipi.append("bdth_bdtqcd_"+suff)

#tipi = ["hmaa_mhh","hmaa_mbb","hh_m","haa_m"] : #in bbgammagamma ho una h davanti a tutto
#tipi = ["pthtata_metcorr","mT2","nljets","ptta2","drbb","ptta1","ptb2","hh_metcorr_m","ptb1","etab2","etab1","hh_m","pthtata","ntajets","pthbb","bdt","drtata","etata1","met","nbjets","etata2","htata_metcorr_m","htata_m","nlep","hbb_m","hmtata_mbb_metcorr"] #bbtt
#tipi =  ["hh_m","h1_pt","h2_pt","h2_m","tmva_bdt","h1_m"] #tipi di 4b
#tipi =  ["tmva_bdt"] #tipi di 4b
#tipi =  ["tmva_bdt_qcd","hbb_m","tmva_bdt_singleh","haa_m","hh_m","hmaa_mhh","bdth_bdtqcd","hmaa_mbb"] #tipi di bbaa
if not "bbaa" in opt.channel :
	tipi =  ["tmva_bdt"]

#tipi = ["pthtata_metcorr","mT2","nljets","ptta2","drbb","ptta1","ptb2","hh_metcorr_m","ptb1","etab2","etab1","hh_m","pthtata","ntajets","pthbb","bdt","drtata","etata1","met","nbjets","etata2","htata_metcorr_m","htata_m","nlep","hbb_m","hmtata_mbb_metcorr"] #bbtt
for startDir in startDirList :
	#if "hhbbtahtal_III_TL" in startDir: continue
	#if "hhbbbb_III_T_beffUp" in startDir : continue
	histoSuffix = startDir.replace("FCCworkshop3/hhbbaa","")
	histoSuffix = histoSuffix.replace("FCCworkshop3/hhbbbb","")
	histoSuffix = histoSuffix.replace("FCCworkshop3/hhbbtahtah","")
	histoSuffix = histoSuffix.replace("FCCworkshop3/hhbbtahtal","")
	histoSuffix = histoSuffix.replace("/eos/user/s/selvaggi/Analysis/hh_comb/hhbbaa_v58/hhbbaa","")
	histoSuffix = histoSuffix.replace("/eos/user/s/selvaggi/Analysis/hh_comb/hhbbbb_v58/hhbbbb","")
	histoSuffix = histoSuffix.replace("/eos/user/s/selvaggi/Analysis/hh_comb/hhbbtahtah_v58/hhbbtahtah","")
	histoSuffix = histoSuffix.replace("/eos/user/s/selvaggi/Analysis/hh_comb/hhbbtahtal_v58/hhbbtahtal","")
	histoSuffix = histoSuffix.replace("/","")
	histoSuffix = histoSuffix.replace("_beffDown","")
	histoSuffix = histoSuffix.replace("_beffUp","")
	for klambda in lambdas :
		#print klambda
		extraString = "sel_HH_kappa_lambda_{0:.2f}/".format(klambda)
		extraOne = "sel_HH_kappa_lambda_{0:.2f}/".format(1.0)
		#if "bbbb" in opt.channel:
		#	extraString = "" "sel_HH_kappa_lambda_{0:.2f}/".format(klambda)
		#	extraOne = "" "sel_HH_kappa_lambda_{0:.2f}/".format(1.0)
		#if "bbtahtah" in startDir : 
		#	extraString = ""
		#	extraOne = ""
		inFile = TFile.Open("{1}{2}root_HH_kappa_lambda_{0:.2f}/histos.root".format(klambda,startDir,extraString))
		if not inFile : 
			extraString = "" #"sel_HH_kappa_lambda_{0:.2f}/".format(klambda)
			extraOne = "" #"sel_HH_kappa_lambda_{0:.2f}/".format(1.0)
			inFile = TFile.Open("{1}{2}root_HH_kappa_lambda_{0:.2f}/histos.root".format(klambda,startDir,extraString))
			#print "not available: {1}{2}root_HH_kappa_lambda_{0:.2f}/histos.root".format(klambda,startDir,extraString)
			if not inFile : continue
		#else : print "found"
		#outFile = TFile.Open("hhbbaa_v6/sel_HH_kappa_l_{0:.2f}/root_HH_kappa_l_{0:.2f}/shapes.root".format(klambda,klambda),"RECREATE")
		#outFile = TFile.Open("hhbbtahtal_v6/root_HH_kappa_l_{0:.2f}/shapes.root".format(klambda),"RECREATE")
		outFile = TFile.Open("{1}{2}root_HH_kappa_lambda_{0:.2f}/shapes.root".format(klambda,startDir,extraString),"RECREATE")
		for entry in inFile.GetListOfKeys() :
			#inFile.GetListOfKeys().Print() 
			#entry.Print()
			oldName = entry.GetName()
			outObj = inFile.Get(oldName)
			newName = oldName.replace('(#kappa_{#lambda}=',"") #HH(#kappa_{#lambda}=0.94)
			newName = newName.replace("{0:.2f})".format(klambda),"")
			newName = newName.replace("j#gamma + Jets","jgjj")
			newName = newName.replace("Z+jets","zjets")
			newName = newName.replace("Z+bb","Zbb")
			newName = newName.replace("#gamma#gamma + Jets","ggjj")
			newName = newName.replace('t#bar{t}',"ttbar")
			newName = newName.replace("single Higgs","singleH")
			newName = newName.replace("top pair","ttbar")
			newName = newName.replace("QCD+EWK","QCDEWK")
			outObj.SetName(newName)
			outObj.SetTitle(newName)
			#print "writing", newName
			outFile.cd()
			outObj.Write()
	
		#processes = ["jgjj","ggjj","VH","ggH","ttH","zjets","ZZ","ttbar"]	
		#processes = ["ggH","ttH","zjets","ZZ","ttbar","ttbar_tautau","VH"]	
	
		#create data_obs, for now I exclude ttbar_tautau
		for sel in range(0,upRange) : 
		#for sel in range(0,8) : 
			#for tipo in ["hmaa_mhh","hmaa_mbb","hh_m","haa_m"] : #in bbgammagamma ho una h davanti a tutto
			#for tipo in ["pthtata_metcorr","mT2","nljets","ptta2","drbb","ptta1","ptb2","hh_metcorr_m","ptb1","etab2","etab1","hh_m","pthtata","ntajets","pthbb","bdt","bdt2","drtata","etata1","met","nbjets","etata2","htata_metcorr_m","htata_m","nlep","hbb_m","hmtata_mbb_metcorr"]:
			for temptipo in tipi : #tipi di 4b
				tipo = temptipo
				#if "bdth_bdtqcd" in tipo : 
				tipo = tipo + histoSuffix
				if klambda ==1 : 
					#print "HH_sel{0}_{1}".format(sel,tipo)
					#if (inFile.Get("HH_sel{0}_h{1}".format(sel,tipo))):
					#obs = outFile.Get("jgjj_sel{0}_{1}".format(sel,tipo)).Clone("data_obs")
					#print outFile.Get("HH_sel{0}_{1}".format(sel,tipo))
					obs = outFile.Get("HH_sel{0}_{1}".format(sel,tipo)).Clone("data_obs")
					for iproc in processes :
						#print "{2}_sel{0}_h{1}".format(sel,tipo,iproc)
						#outFile.Get("{2}_sel{0}_h{1}".format(sel,tipo,iproc)).Print()
						#print klambda,sel,tipo,iproc
						obs.Add(outFile.Get("{2}_sel{0}_{1}".format(sel,tipo,iproc)))
						#print "done"
				else :
					#fileone = TFile.Open("hhbbaa/sel_HH_kappa_l_{0:.2f}/root_HH_kappa_l_{0:.2f}/shapes.root".format(1.0,1.0))
					fileone = TFile.Open("{1}{2}root_HH_kappa_lambda_{0:.2f}/shapes.root".format(1.0,startDir,extraOne))
					if not fileone : fileone = TFile.Open("{1}sel_HH_kappa_lambda_1.00/root_HH_kappa_lambda_{0:.2f}/shapes.root".format(1.0,startDir))
					obs = fileone.Get("HH_sel{0}_{1}".format(sel,tipo)).Clone("data_obs")
				#if sel == 1 and tipo == "bdt" : 
				#	#print "lambda", klambda, ";",inFile.Get("HH_sel{0}_h{1}".format(sel,tipo)).Integral()*30000000.0
				#	print "lambda",inFile.Get("HH_sel{0}_{1}".format(sel,tipo)).Integral()*30000000.0
				obs.SetName("data_obs_sel{0}_{1}".format(sel,tipo))
				obs.SetTitle("data_obs_sel{0}_{1}".format(sel,tipo))
				outFile.cd()
				obs.Write()
		outFile.Close()

##if boosted
#for klambda in lambaboos :
#	print klambda
#	inFile = TFile.Open("hh_boosted/root_HH_kappa_l_{0:.2f}/histos.root".format(klambda))
#	if not inFile : 
#		continue
#	else : print "found"
#	outFile = TFile.Open("hh_boosted/root_HH_kappa_l_{0:.2f}/shapes.root".format(klambda),"RECREATE")
#	for entry in inFile.GetListOfKeys() :
#		#inFile.GetListOfKeys().Print() 
#		#entry.Print()
#		oldName = entry.GetName()
#		outObj = inFile.Get(oldName)
#		newName = oldName.replace('(#kappa_{l}=',"") #
#		newName = newName.replace("{0:.2f})".format(klambda),"")
#		newName = newName.replace("+","")
#		#newName = newName.replace("#gamma#gamma + Jets","ggjj")
#		outObj.SetName(newName)
#		outObj.SetTitle(newName)
#		outFile.cd()
#		outObj.Write()
#	
#	processes = ["QCD","EWK","QCDEWK"]	
#	
#	for sel in range(0,7) : 
#		for tipo in ["mbb_mbb","h_m"] :
#			if klambda ==1 : obs = inFile.Get("HH_sel{0}_h{1}".format(sel,tipo)).Clone("data_obs")
#			else :
#				fileone = TFile.Open("hh_boosted/root_HH_kappa_l_{0:.2f}/shapes.root".format(1.0))
#				obs = fileone.Get("HH_sel{0}_h{1}".format(sel,tipo)).Clone("data_obs")
#			for iproc in processes :
#				#print "{2}_sel{0}_h{1}".format(sel,tipo,iproc)
#				#outFile.Get("{2}_sel{0}_h{1}".format(sel,tipo,iproc)).Print()
#				obs.Add(outFile.Get("{2}_sel{0}_h{1}".format(sel,tipo,iproc)))
#			obs.SetName("data_obs_sel{0}_h{1}".format(sel,tipo))
#			obs.SetTitle("data_obs_sel{0}_h{1}".format(sel,tipo))
#			outFile.cd()
#			obs.Write()
#	outFile.Close()

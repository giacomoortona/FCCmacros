from ROOT import *
import os,re, optparse

def parseOptions():

    usage = ('usage: %prog [options] datasetList\n'+ '%prog -h for help')
    parser = optparse.OptionParser(usage)
    parser.add_option('-c', '--channel', dest='channel', type='string', default="bbaa", help='bbaa bbbb bbtahtal bbtahtah')


    global opt, args
    (opt, args) = parser.parse_args()




def convertWord(word) :
	res = str(word)
	res = res.replace(".",",")
	return res
#inputs = [0.0,0.2,0.4,0.6,0.7,0.8,0.85,0.9,0.92,0.96,0.97,0.98,0.99,1.04,1.06,1.08,1.00,1.1,1.2,1.3,1.4,1.45,1.5,1.55,1.60,1.7,1.9,2.00,2.2,2.4,2.6,2.8,3.0]
#inputs = [0.0,0.2,0.6,0.7,0.8,0.9,0.92,0.94,0.96,0.97,0.98,0.99,1.01,1.02,1.03,1.04,1.08,1.00,1.1,1.2,1.3,1.4,1.45,1.5,1.55,1.60,1.7,1.9,2.00,2.2,2.4,2.6,2.8,3.0]
#inputs = [0.9,0.95,0.96,0.97,0.98,0.99,1,1.01,1.02,1.03,1.04,1.05,1.1]
#inputs = [0.0,0.2,0.6,0.7,0.8,0.85,0.9,0.92,0.94,0.96,0.97,0.98,0.99,1.01,1.02,1.03,1.04,1.06,1.08,1.00,1.1,1.2,1.4,1.45,1.55,1.60,1.7,1.9,2.00,2.2,2.4,2.6,2.8,3.0]
#inputs = [0.0,0.2,0.4,0.6,0.7,0.8,0.85,0.9,0.92,0.94,0.96,0.97,0.98,0.99,1.01,1.04,1.06,1.08,1.00,1.1,1.2,1.4,1.45,1.55,1.60,1.7,1.9,2.00,2.2,2.4,2.6,2.8,3.0]
#inputs = [0.0,0.2,0.4,0.6,0.7,0.8,0.85,0.9,0.92,0.94,0.96,0.97,0.98,0.99,1.01,1.02,1.03,1.04,1.06,1.08,1.00,1.1,1.2,1.4,1.45,1.55,1.60,1.7,1.9,2.00,2.2,2.4,2.6,2.8,3.0]
inputs = [0.0,0.2,0.4,0.6,0.7,0.8,0.85,0.9,0.92,0.94,0.96,0.97,0.98,0.99,1.0,1.01,1.02,1.03,1.04,1.06,1.08,1.1,1.2,1.3,1.4,1.45,1.5,1.55,1.60,1.7,1.9,2.00,2.2,2.4,2.6,2.8,3.0]

inputsprec = [0.0,0.4,0.7,1.0,1.3,1.5,1.7,2.0,2.2,2.4,2.6,3.0]

inputs = [1.00,0.85,0.98,1.04,1.40,1.80,2.80,0.20,0.90,0.99,1.06,1.45,1.90,3.00,0.40,0.92,0.00,1.08,1.50,2.00,0.94,1.01,1.10,1.55,2.20,0.70,0.96,1.02,1.20,1.60,2.40,0.80,0.97,1.03,1.30,1.70,2.60]
inputs = [1.00,0.00,0.20,0.40,0.60,0.70,0.80,0.85,0.90,0.92,0.96,0.97,0.98,0.99,1.01,1.02,1.03,1.04,1.06,1.08,1.10,1.20,1.30,1.40,1.45,1.50,1.55,1.70,1.90,2.00,2.20,2.40,2.60,2.80,3.00]
#inputs = [1.00,0.00,2.00]

parseOptions()
global opt, args

channel = opt.channel

tipo = "tmva_bdt"
startDirList = []
btagWPs = ['M','T']
photonWPs = ["M","T"] #[""] #['M','T']
if channel == "bbbb" :
	photonWPs = [""]
elif "bbta" in channel :
	photonWPs = ['M','T']
elif channel == "bbaa" :
	tipo = "bdth_bdtqcd_100"
scenarios = ['I','II','III']
#beffpoints = ["","_beffDown","_beffUp"]

#scenarios = ['I']
#btagWPs = ["L"]
#photonWPs = ["T"]


rateForSel=[]
c = TCanvas("a")
colors = [kRed,kGreen,kYellow,kCyan,kBlack,kBlue,kMagenta,kRed+1,kGreen+2,kGray+3,kRed+4,kCyan+2,kGreen+4,kYellow-5]

histos = []
i = 0
ref = 0
sel = 0

g = TGraph()
parabola = TF1("parabola","[0]*x*x+[1]*x+1",min(inputs)-1.0,max(inputs)-1.0) 

First = True


outFile = open("outRates{0}.py".format(opt.channel),"w")
outFile.write("def getRate{0}(scenario,bwp,pwp):\n".format(opt.channel))
outFile.write("    outString = \"CIAO\"\n".format(opt.channel))
for sc in scenarios:
    for bwp in btagWPs:
        for pwp in photonWPs:
        	#for beff in beffpoints:
        		#hhbbaa_III_LT/sel_HH_kappa_lambda_1.00/root_HH_kappa_lambda_1.00
        	#startDirList.append('FCCworkshop3/BatchOutput/hh{}_{}_{}{}/'.format(channel,sc,bwp,pwp))
        	startDir = '/eos/user/s/selvaggi/Analysis/hh_comb/hh{}_v58/hh{}_{}_{}{}/'.format(channel,channel,sc,bwp,pwp)
        	#startDirList.append('/eos/user/s/selvaggi/Analysis/hh_comb/hh{}_v58/hh{}_{}_{}{}/'.format(channel,channel,sc,bwp,pwp))
        	#for startDir in startDirList : 
        	print "======"
    		#print "SEL ",sel
    		print startDir
    		points = []
    		for inputL in inputs:
    		    fileIn = fileIn = TFile.Open("{1}sel_HH_kappa_lambda_{0:.2f}/root_HH_kappa_lambda_{0:.2f}/shapes.root".format(inputL,startDir))
    		    #fileIn = TFile.Open("FCCworkshop3/hhbbtahtah/root_HH_kappa_lambda_{0:.2f}/shapes.root".format(inputL))
    		    if not fileIn : TFile.Open("{1}root_HH_kappa_lambda_{0:.2f}/shapes.root".format(inputL,startDir))
                    if not fileIn : continue
    		    #if fileIn : hist = fileIn.Get("HH_sel{0}_bdt".format(sel)) #hist = fileIn.Get("HH_sel{0}_bdth_bdtqcd".format(sel)) #
    		    if fileIn : 
    		    	#if inputL in inputsprec:
    		    	#	#farequalcos
    		    	#	number_dec = str(inputL-int(inputL))[2:]
    		    	#	appString = "{0}{1}0".format(int(inputL),number_dec)
    		    	#else:
    		    	#	appString = "100"
    		    	appString = "{}_{}{}".format(sc,bwp,pwp)
    		    	hist = fileIn.Get("HH_sel{0}_{2}_{1}".format(sel,appString,tipo)) #
    		    if hist : 
    		    	if inputL == 1 : ref = hist.Integral()
    		    	#print convertWord(inputL),";", convertWord(inputL-1), ";", convertWord(hist.Integral()*30000000)
    		    	g.SetPoint(g.GetN(),inputL-1,hist.Integral()/ref)
    		    	points.append(hist.Integral()/ref)
    		    else : print "HH_sel{0}_{2}_{1} not found".format(sel,appString,tipo) 
    				#rateForSel.append(hist.Integral()*30000000)
    				#		hnew = hist.Clone("lambda{0}".format(inputL))
    				#		hist.SetLineColor(colors[i])
    				#		hist.DrawNormalized("LSAME")
    				#		histos.append(hist)
    				#		i = i +1
    		g.Fit(parabola)
    	
    		#c.cd()
    		##g.Draw("ALP")
    		#if First :
    		#	parabola.Draw()
    		#	First = False
    		#else : parabola.DrawCopy("SAME")
    		#c.Modified()
    		#c.Update()
    		print startDir
    		print points
    		print "{0:.5f}*@0*@0 + ({1:.5f}-2.0*{0:.5f})*@0 +{0:.5f} + 1.0 - {1:.5f}".format(parabola.GetParameter(0),parabola.GetParameter(1)) #y = a x2 + (b-2a)x +a+1-b
    		outFile.write("    if scenario is \"{0}\" and bwp is \"{1}\" and pwp is \"{2}\":\n".format(sc,bwp,pwp))
    		outFile.write("        outString = \"{0:.5f}*@0*@0 + ({1:.5f}-2.0*{0:.5f})*@0 +{0:.5f} + 1.0 - {1:.5f}\"\n".format(parabola.GetParameter(0),parabola.GetParameter(1)))
    		for ipoint in range(len(points)) :
    			if abs(parabola.Eval(inputs[ipoint]-1.0) - points[ipoint])/points[ipoint] > 0.1 : print "ERROR evaluation at ", inputs[ipoint]-1.0,":",parabola.Eval(inputs[ipoint]-1.0),"(fit) vs",points[ipoint]
#raw_input()
outFile.write("    return outString")
	#c.SaveAs("bdt.root")
#print histos
#for h in range(len(histos)) :
#	histos[h].Print()
#	histos[h].SetLineColor(colors[h])
#	histos[h].DrawNormalized("SAME")
#print rateForSel

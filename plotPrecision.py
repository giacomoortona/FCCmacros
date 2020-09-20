from ROOT import *
import optparse

#higgsCombinelumiScan_I_lumi_forPrec.FitDiagnostics.mH120.root

def parseOptions():

    usage = ('usage: %prog [options] datasetList\n'+ '%prog -h for help')
    parser = optparse.OptionParser(usage)
    parser.add_option('-i', '--input', dest='source', type='string', default="comb", help='')
    parser.add_option('-p', '--plotStyle', dest='style', type='string', default="max", help='max, average, min, errors')
    parser.add_option('-s', '--scale', dest='scale', type='int', default="1", help='scale to SM value')
    global opt, args
    (opt, args) = parser.parse_args()

parseOptions()
global opt, args

combSourcelow = [0,0,0,0] #PaperLinear/higgsCombinecombCard_1.00_syst2.txt_kl_2.MultiDimFit.mH120.root
combSourcehigh = [0,0,0,0] #PaperLinear/higgsCombinecombCard_1.00_syst2.txt_kl_2.MultiDimFit.mH120.root
if opt.scale>0 :
	fileLoader = ["/eos/user/g/gortona/FCC/Results_v49/higgsCombinelumiScan_III_lumi1.0_forPrec.FitDiagnostics.mH120.root",
	"/eos/user/g/gortona/FCC/Results_v49/higgsCombinelumiScan_II_lumi1.0_forPrec.FitDiagnostics.mH120.root",
	"/eos/user/g/gortona/FCC/Results_v49/higgsCombinelumiScan_I_lumi1.0_forPrec.FitDiagnostics.mH120.root",
	"/eos/user/g/gortona/FCC/Results_v49/higgsCombinelumiScan_I_lumi1.0_noSyst_forPrec.FitDiagnostics.mH120.root"]
	for ic in range(len(combSourcelow)) :
		fileIn =  TFile.Open(fileLoader[ic])
		tree = fileIn.Get("limit")
		lowBase = 1
		highBase =1
		deltaL = 9999.0
		deltaH = 9999.0
		for entry in tree :
			if entry.kl < 1.0 :
				if abs(2.0*entry.deltaNLL - 1) > deltaL : continue
				else :
					deltaL = abs(2.0*entry.deltaNLL - 1)
					lowBase = entry.kl
			elif entry.kl > 1.0 : 
				if abs(2.0*entry.deltaNLL - 1) > deltaH : continue
				else :
					deltaH = abs(2.0*entry.deltaNLL - 1)
					highBase = entry.kl				
#		for entry in tree:
#			if entry.kl < 1.0 :
#				if 2.0*entry.deltaNLL < 1 : continue
#				lowBase = entry.kl
#			else :
#				if 2.0*entry.deltaNLL > 1 : continue
#				highBase = entry.kl	
		combSourcelow[ic] = 1.0-lowBase
		combSourcehigh[ic] = highBase-1.0

print combSourcelow
print combSourcehigh
plotLumi = True
mdf = True
#lambdas = [1.0,0.0,0.2,0.4,0.6,0.7,0.8,0.85,0.9,0.92,0.94,0.96,0.97,0.98,0.99,1.01,1.02,1.03,1.04,1.06,1.08,1.1,1.2,1.3,1.4,1.45,1.5,1.55,1.60,1.7,1.9,2.00,2.2,2.4,2.6,2.8,3.0]
#skipLambdas = [0.4,0.9,0.94,1.00,1.01,1.02,1.03,1.3,1.5,1.9,2.00,0.7,0.85,1.06,0.98]
lambdas = [1.0,0.0,0.4,0.7,1.3,1.5,1.7,2.0,2.2,2.4,2.6,3.0] #1.5, 0.4
skipLambdas = []
#for lambdas in 1.00 0.00 0.20 0.60 0.70 0.80 0.85 0.90 0.92 0.96 0.97 0.98 0.99 1.04 1.06 1.08 1.10 1.20 1.30 1.40 1.45 1.50 1.55 1.60 1.70 1.90 2.00 2.20 2.40 2.60 2.80 3.00

if plotLumi :
	lambdas = [0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
#fileNameComb = "190113/higgsCombinecombCard_3.00_syst3.txt_kl_NoSyst_forPrec.FitDiagnostics.mH120.root"
#verde, rosso, blu, nero
if opt.source == "comb" :
	fileNameComb = ["/eos/user/g/gortona/FCC/Results_v49/higgsCombinelumiScan_III_lumi1.0_forPrec.FitDiagnostics.mH120.root",
	"/eos/user/g/gortona/FCC/Results_v49/higgsCombinelumiScan_II_lumi1.0_forPrec.FitDiagnostics.mH120.root",
	"/eos/user/g/gortona/FCC/Results_v49/higgsCombinelumiScan_I_lumi1.0_forPrec.FitDiagnostics.mH120.root",
	"/eos/user/g/gortona/FCC/Results_v49/higgsCombinelumiScan_I_lumi1.0_forPrec_noSyst.FitDiagnostics.mH120.root"]
else : 
	fileNameComb = ["precision_v1/higgsCombinecard3.00_syst3_sel0.txt_kl_3_forPrec.MultiDimFit.mH120.root",
	"precision_v1/higgsCombinecard3.00_syst2_sel0.txt_kl_2_forPrec.MultiDimFit.mH120.root",
	"precision_v1/higgsCombinecard3.00_syst1_sel0.txt_kl_1_forPrec.MultiDimFit.mH120.root",
	"precision_v1/higgsCombinecard3.00_syst2_sel0.txt_kl_NoSyst_forPrec.MultiDimFit.mH120.root"]
graph = [TGraph(),TGraph(),TGraph(),TGraph()]#TGraphAsymmErrors()
if opt.style == "errors" : graph = [TGraphAsymmErrors(),TGraphAsymmErrors(),TGraphAsymmErrors(),TGraph()]
colors = [kBlue,kRed+1,kGreen+1,kBlack]
#colors = [kGray,kGray+2,kGray+3,kBlack]
titles = ["Combined - syst. III ","Combined - syst. II ","Combined - syst. I","Combined - no syst. unc."]
legend = ()
for ila in lambdas :
	if ila in skipLambdas and not plotLumi: continue
	ig = 0
	for iname in fileNameComb :
		if plotLumi : 
			fname = iname.replace("3.00","1.00")
			#fname = iname.replace("3.00","{0:.2f}".format(ila))
			if ila >0.092 :fname = fname.replace("forPrec","forLumi{0:.1f}".format(ila))
			else : fname = fname.replace("forPrec","forLumi{0:.2f}".format(ila))
		else :
			#fname = iname.replace("kl","mu")
			fname = iname.replace("3.00","{0:.2f}".format(ila))
		inF = TFile.Open(fname)
		if not inF : continue
		tree = inF.Get("limit")
		if not tree : 
			print "Tree",ila,"not found"
			continue
		low = -1
		high = -1
		for entry in tree :
			if plotLumi :
				if mdf:
					if entry.quantileExpected>-0.5 and  entry.quantileExpected<-0.3 : low = ila- entry.r 
					elif entry.quantileExpected>0 : high = entry.r -ila				
				else :
					if entry.quantileExpected>0.83 and  entry.quantileExpected<0.88 : high = entry.limit -ila 
					elif entry.quantileExpected>0.15 and  entry.quantileExpected<0.17 : low = ila - entry.limit
			else :
				if mdf:
					if entry.quantileExpected>-0.5 and  entry.quantileExpected<-0.3 : low = ila- entry.kl 
					elif entry.quantileExpected>0 : high = entry.kl -ila				
				else :
					if entry.quantileExpected>0.83 and  entry.quantileExpected<0.88 : high = entry.limit -ila 
					elif entry.quantileExpected>0.15 and  entry.quantileExpected<0.17 : low = ila - entry.limit
		#print ig, ila, high, low

		if abs(ila-1.0)<0.1 : 
			#find offset
			combSourcelow[ig]=low-combSourcelow[ig]
			combSourcehigh[ig]=high-combSourcehigh[ig]
			if ig == 3 : 
				print combSourcelow
				print combSourcehigh			
		print ig, ila, high, low,high-combSourcehigh[ig],low-combSourcelow[ig]
		#if high-combSourcehigh[ig] > 0 : high = high-combSourcehigh[ig]
		#if low-combSourcelow[ig] > 0 : low = low-combSourcelow[ig]
		high = high-combSourcehigh[ig]
		low = low-combSourcelow[ig]
		if opt.style == "max" : val = max(high,low)
		elif opt.style == "min" : val = min(high,low)
		else  : val = (high+low)/2.0
		multX = 30
		if not plotLumi : multX = 1
		#if val > 0.1 : val = min(high,low)
		#if val < 0.29 and val > 0.01: 
		if (val > 0.001 and ila >= 0) or True:
			graph[ig].SetPoint(graph[ig].GetN(),ila*multX,val)
			if opt.style == "errors" and ig < 3:  
				graph[ig].SetPointError(graph[ig].GetN()-1,0,0,(val-low),(high-val))
			ig = ig+1

#prec=0.22
#precComb=0.17
#val = val-0.05
c = TCanvas()
c.SetTicks(1,1)
c.SetLeftMargin(0.14)
c.SetRightMargin(0.08)
c.cd()
gStyle.SetOptTitle(0)

for ig in range(len(fileNameComb)):
	graph[ig].Sort()
	#graph[ig].Print()
	graph[ig].SetPoint(graph[ig].GetN(),2.1,(graph[ig].GetY()[7]+graph[ig].GetY()[8])/2.0)
	graph[ig].Sort()
	graph[ig].SetPoint(graph[ig].GetN(),2.15,(graph[ig].GetY()[8]+graph[ig].GetY()[9])/2.0)
	graph[ig].Sort()
	graph[ig].Print()
	graph[ig].RemovePoint(5)
	graph[ig].SetTitle(titles[ig])
	graph[ig].SetMarkerStyle(22)
	graph[ig].SetMarkerSize(0)
	graph[ig].SetMarkerColor(colors[ig])
	if opt.style == "errors" : graph[ig].SetFillColor(colors[ig])
	else : graph[ig].SetFillColor(0)
	graph[ig].SetLineWidth(3)
	graph[ig].SetLineColor(colors[ig])
	graph[ig].GetXaxis().SetTitle("Collected luminosity (ab^{-1})")
	#graph[ig].GetYaxis().SetTitle("#delta k_{#lambda}/k_{#lambda}, #mu=1 (%)")
	graph[ig].GetYaxis().SetTitle("#delta k_{#lambda}, #mu=1 (%)")

	if ig == 0 : 
		if opt.style == "errors" : graph[ig].Draw("A3P")
		else : graph[ig].Draw("acp")
		graph[ig].GetXaxis().SetTitle("Collected luminosity (ab^{-1})")
		if plotLumi : graph[ig].GetYaxis().SetTitle("#delta k_{#lambda}/k_{#lambda}, #mu=1 (%)")
		else: graph[ig].GetYaxis().SetTitle("#delta k_{#lambda}")
		if plotLumi : c.SetLogx()
		c.Modified()
		c.Update()

	else: 
		if opt.style == "errors" : graph[ig].Draw("3PSAME")
		else : graph[ig].Draw("cpSAME")
	if plotLumi :
		graph[ig].GetXaxis().SetTitle("Collected luminosity (ab^{-1})")
		graph[ig].GetYaxis().SetTitle("#delta k_{#lambda}/k_{#lambda}, #mu=1")
		#graph[ig].GetYaxis().SetTitle("#delta k_{#lambda}, #mu=1 (%)")
	else :
		graph[ig].GetXaxis().SetTitle("k_{#lambda}")
		#graph[ig].GetYaxis().SetTitle("Expected Precision on k_{#lambda}")
		#graph[ig].GetYaxis().SetTitle("#delta#mu/#mu, #mu=1 (%)")
		#graph[ig].GetYaxis().SetTitle("#delta k_{#lambda}/k_{#lambda}, #mu=1 (%)")
		graph[ig].GetYaxis().SetTitle("#delta k_{#lambda}")
		graph[ig].GetYaxis().SetTitleOffset(1.1)
		graph[ig].GetYaxis().SetTitleSize(0.05)
		graph[ig].GetXaxis().SetTitleSize(0.05)
		graph[ig].GetXaxis().SetTitleOffset(0.9)


#graph[3].Print()
graph[3].SetLineStyle(2)

leg = c.BuildLegend()
#leg.SetHeader("NB: 2.4 ha errore molto asimmetrico (-20/+90)")
leg.SetHeader("Assuming SM couplings.")
leg.SetLineColor(0)
leg.SetLineStyle(0)
leg.SetLineWidth(0)
leg.SetFillStyle(0)
leg.SetShadowColor(10)
leg.SetTextSize(0.030)
leg.SetTextFont(42)
leg.SetX1(0.37)
leg.SetX2(0.6)
leg.SetY1(0.63)
leg.SetY2(0.88)

Text = TPaveText(0.58, 0.88,0.93,0.95,'brNDC')
#Text.SetNDC() 
Text.SetTextAlign(31);
Text.SetTextSize(0.04)
leftText = "FCC-hh Simulation (Delphes)"
re = "#sqrt{s} = 100 TeV, L = 30 ab^{-1}"
text = '#it{' + leftText +'}'
#Text.DrawLatex(0.90, 0.92, text) 
Text.AddText(text)
Text.SetFillStyle(0)
Text.SetLineStyle(0)
Text.SetBorderSize(0)
Text.Draw()

Text2 = TPaveText(0.20, 0.71,0.35,0.85,'brNDC')
rightText = re.split(",")#, rightText)
text = '#bf{#it{' + rightText[0] +'}}'
Text2.SetTextAlign(12);
#Text.SetNDC(True) 
Text2.SetTextSize(0.036)
Text2.AddText(text)
text = '#bf{#it{' + rightText[1] +'}}'
Text2.AddText(text)
#Text2.SetFillStyle(0)
Text2.SetFillColor(kWhite)
Text2.SetLineStyle(0)
Text2.SetBorderSize(0)
Text2.Draw()

if plotLumi :
	line = TLine(0*30,5,1.1*30,5) #9 per CLIC, aggiungere testo 5%
	line.SetLineColor(kGray+2)
	line.SetLineStyle(2)
	line.Draw("SAME")
	line2 = TLine(0*30,10,1.1*30,10) 
	line2.SetLineColor(kGray+2)
	line2.SetLineStyle(2)
	line2.Draw("SAME")
	line3 = TLine(0*30,15,1.1*30,15) 
	line3.SetLineColor(kGray+2)
	line3.SetLineStyle(2)
	line3.Draw("SAME")
	graph[0].GetXaxis().SetRangeUser(0.008*30,1.1*30)
	graph[0].GetYaxis().SetRangeUser(0,30)
	c.Modified()
	graph[0].GetXaxis().SetLimits(0.008*30,1.1*30)
	graph[0].GetYaxis().SetLimits(0,30)
	c.Modified()
	c.Update()
else : 
	graph[0].GetXaxis().SetRangeUser(0,3.1)
	graph[0].GetYaxis().SetRangeUser(0.0,0.45)
	c.Modified()
	graph[0].GetXaxis().SetLimits(0,3.1)
	graph[0].GetYaxis().SetLimits(0.0,0.45)
	#c.SetLogy()
	c.Modified()
	c.Update()
graph[3].Print()
raw_input()
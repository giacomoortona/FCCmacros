from ROOT import *
#

## plottare bbZZ prima di 4b
## fare legenda bianca

#

plotMu = True
eosDir = "/eos/user/g/gortona/FCC/Results_v58/"
pWP = ["M","M","M"]
bgWP = ["M","M","M"]
btWP = ["M","M","M"]
bWP = ["M","M","M"]
lWP = ["M","M","M"]
suffix = "v58_TMMMM"
#def plotPrecision() :
#	#y = [] #file syst default
#	#ys1 = [] #file syst optimistic
#	#ys2 = [] #file syst pessimistic
#	#x = []
#	#xe = []
#	graph = TGraphAsymmErrors()
#	for ix in range(0,21) :
#		x = 0.9+ix*0.01
#		y = 0.11-ix*0.001
#		ys1 = y+(0.11-ix*0.00083)
#		ys2 = y-(0.11-ix*0.0011)
#		xe = 0
#		graph.SetPoint(graph.GetN(),x,y)
#		graph.SetPointError(graph.GetN()-1,xe,xe,ys2,ys1)
#	c1=TCanvas()
#	c1.SetTicks(1,1)
#	c1.SetLeftMargin(0.14)
#	c1.SetRightMargin(0.08)
#	c1.cd()
#
#	graph.Print()
#	graph.Draw("AP")
#	#graph.SetPoint() 

#fileList = ["higgsCombinebbgg_scankl_syst1_bkTimes1.MultiDimFit.mH120.root","higgsCombinebbtt_scankl_syst1_bkTimes1.MultiDimFit.mH120.root","higgsCombinebbcombno4b_scankl_syst3_bkTimes1.MultiDimFit.mH120.root","higgsCombinebbcombno4b_scankl_syst2_bkTimes1.MultiDimFit.mH120.root","higgsCombinebbcombno4b_scankl_syst1_bkTimes1.MultiDimFit.mH120.root"]
#fileList = ["higgsCombinebbgg_scankl_syst1_bkTimes1.MultiDimFit.mH120.root","higgsCombinebbtt_scankl_syst1_bkTimes1.MultiDimFit.mH120.root","higgsCombinebbbb_scankl_syst1_bkTimes1.MultiDimFit.mH120.root","higgsCombinebb4l_scankl_syst1_bkTimes1.MultiDimFit.mH120.root","higgsCombinebbcombno4b_scankl_syst1_bkTimes1.MultiDimFit.mH120.root","higgsCombinebbcombno4b_scankl_sel2_syst1noSyst_bkTimes1.MultiDimFit.mH120.root"]
#fileList = ["higgsCombinebbcomb_scankl_syst3_bkTimes1.MultiDimFit.mH120.root","higgsCombineTest0.MultiDimFit.mH120.root","higgsCombineTest2.MultiDimFit.mH120.root","higgsCombinebbcomb_scankl_syst1noSyst_bkTimes1.MultiDimFit.mH120.root","higgsCombinebbcomb_scankl_syst1noSyst_bkTimes1.MultiDimFit.mH120.root"]
#fileErrList = ["higgsCombinebbcomb_scankl_syst3_bkTimes1.MultiDimFit.mH120.root","higgsCombineTest0.MultiDimFit.mH120.root","higgsCombineTest2.MultiDimFit.mH120.root","higgsCombinebbcomb_scankl_syst1noSyst_bkTimes1.MultiDimFit.mH120.root","higgsCombinebbcomb_scankl_syst1noSyst_bkTimes1.MultiDimFit.mH120.root"]
#fileErrListLow = ["higgsCombinebbcomb_scankl_syst3_bkTimes1.MultiDimFit.mH120.root","higgsCombineTest0.MultiDimFit.mH120.root","higgsCombineTest2.MultiDimFit.mH120.root","higgsCombinebbcomb_scankl_syst1noSyst_bkTimes1.MultiDimFit.mH120.root","higgsCombinebbcomb_scankl_syst1noSyst_bkTimes1.MultiDimFit.mH120.root"]

#bb4l, bbbb, bbtt, bbtahtah, bbtahtal, bbgg, comb, combnosyst

appender = ""
if plotMu : appender = "_mu"

fileList = ["higgsCombinecard1.00_bb4l_syst2.txt_kl_2.MultiDimFit.mH120.root",
			"higgsCombine1.00_bbbb_btag_2_II{0}{1}.MultiDimFit.mH120.root".format(bWP[1],appender),
			
			#"higgsCombinecard1.00_bbtt_sel0_forComb_syst2.txt_kl_2.MultiDimFit.mH120.root",
			#"higgsCombinecard1.00_bbtt_sel0_semilep_forComb_syst2.txt_kl_.MultiDimFit.mH120.root",			
			"higgsCombine1.00_bbaa_btag_2_II{0}{1}{2}.MultiDimFit.mH120.root".format(pWP[1],bgWP[1],appender),
			"higgsCombine1.00_comb_2_II{0}{1}{2}{3}{4}{5}.MultiDimFit.mH120.root".format(pWP[1],bgWP[1],btWP[1],bWP[1],lWP[1],appender),
			"higgsCombine1.00_bbttcomb_btag_2_II{0}{1}{2}.MultiDimFit.mH120.root".format(lWP[1],btWP[1],appender),
			"higgsCombine1.00_comb_1_I{0}{1}{2}{3}{4}_noSyst{5}.MultiDimFit.mH120.root".format(pWP[0],bgWP[0],btWP[0],bWP[0],lWP[0],appender),
			] 
fileErrList = ["higgsCombinecard1.00_bb4l_syst1.txt_kl_1.MultiDimFit.mH120.root",
			"higgsCombine1.00_bbbb_btag_1_I{0}{1}.MultiDimFit.mH120.root".format(bWP[0],appender),
			
			#"higgsCombinecard1.00_bbtt_sel0_forComb_syst2.txt_kl_2.MultiDimFit.mH120.root",
			#"higgsCombinecard1.00_bbtt_sel0_semilep_forComb_syst2.txt_kl_.MultiDimFit.mH120.root",			
			"higgsCombine1.00_bbaa_btag_1_I{0}{1}{2}.MultiDimFit.mH120.root".format(pWP[0],bgWP[0],appender),
			"higgsCombine1.00_comb_1_I{0}{1}{2}{3}{4}{5}.MultiDimFit.mH120.root".format(pWP[0],bgWP[0],btWP[0],bWP[0],lWP[0],appender),
			"higgsCombine1.00_bbttcomb_btag_1_I{0}{1}{2}.MultiDimFit.mH120.root".format(lWP[0],btWP[0],appender),
			"higgsCombine1.00_comb_1_I{0}{1}{2}{3}{4}_noSyst{5}.MultiDimFit.mH120.root".format(pWP[0],bgWP[0],btWP[0],bWP[0],lWP[0],appender),
			] 

fileErrListLow = ["higgsCombinecard1.00_bb4l_syst3.txt_kl_3.MultiDimFit.mH120.root",
			"higgsCombine1.00_bbbb_btag_3_III{0}{1}.MultiDimFit.mH120.root".format(bWP[2],appender),
			
			#"higgsCombinecard1.00_bbtt_sel0_forComb_syst2.txt_kl_2.MultiDimFit.mH120.root",
			#"higgsCombinecard1.00_bbtt_sel0_semilep_forComb_syst2.txt_kl_.MultiDimFit.mH120.root",			
			"higgsCombine1.00_bbaa_btag_3_III{0}{1}{2}.MultiDimFit.mH120.root".format(pWP[2],bgWP[2],appender),
			"higgsCombine1.00_comb_3_III{0}{1}{2}{3}{4}{5}.MultiDimFit.mH120.root".format(pWP[2],bgWP[2],btWP[2],bWP[2],lWP[2],appender),
			"higgsCombine1.00_bbttcomb_btag_3_III{0}{1}{2}.MultiDimFit.mH120.root".format(lWP[2],btWP[2],appender),
			"higgsCombine1.00_comb_1_I{0}{1}{2}{3}{4}_noSyst{5}.MultiDimFit.mH120.root".format(pWP[0],bgWP[0],btWP[0],bWP[0],lWP[0],appender),
			] 

#colors =   [kGreen-2,kRed+1,kPink,kBlue,kBlack,kBlack,kYellow+2,kCyan]
#colors =   [kGreen-2,kYellow-8,kRed+1,kBlue,kBlack,kBlack,kYellow+2,kCyan]
colors =   [kRed+1,kGreen-2,kBlue,kBlack,kYellow-8,kBlack,kYellow+2,kCyan]
#titles = ["bbgg1","bbtt1","c3","c2","c1"]
#titles = ["bbbb","bb#tau_{h}#tau_{h}","bb#tau_{h}#tau_{l}","bb#gamma#gamma","Combined","Combined - no syst.","bb4l1","c1","nosyst"]
titles = ["bbZZ(4l)","bbbb","bb#gamma#gamma","Combined","bb#tau_{h}#tau_{h}+bb#tau_{h}#tau_{l}","Combined - no syst.","bb4l1","c1","nosyst"]
fillstyle = [3001,3002,3002,3005,3006,0]
#titles = ["bbZZ(4l)","bbbb","bb#tau#tau","bb#gamma#gamma","Combined","Combined - no syst.","bb4l1","c1","nosyst"]
graphs = []
grapherrs = []
grapherrslow = []
#plotPrecision()
#raw_input()
for i in range(len(fileList)) : 
	graphs.append(TGraphAsymmErrors())
	#grapherrs.append(TGraph())
	#grapherrslow.append(TGraph())
for ifile in range(len(fileList)):
	if plotMu : inF = TFile.Open(eosDir+fileList[ifile].replace("kl","mu"),"READ")
	else : inF = TFile.Open(eosDir+fileList[ifile],"READ")
	tree = inF.Get("limit")
	if plotMu : inFErr = TFile.Open(eosDir+fileErrList[ifile].replace("kl","mu"),"READ")
	else : inFErr = TFile.Open(eosDir+fileErrList[ifile],"READ")
	treeErr = inFErr.Get("limit")
	if plotMu : inFErrLow = TFile.Open(eosDir+fileErrListLow[ifile].replace("kl","mu"),"READ")
	else : inFErrLow = TFile.Open(eosDir+fileErrListLow[ifile],"READ")
	treeErrLow = inFErrLow.Get("limit")

	#ipoint = 0
	print ifile, fileList[ifile]
	firstEntry = True
	for entry in tree :
		if firstEntry : 
			firstEntry = False
			continue
		#print ifile, ipoint
		if(entry.deltaNLL<80): 
			yval = 2.0*entry.deltaNLL #*1.35
			if plotMu : graphs[ifile].SetPoint(graphs[ifile].GetN(),entry.r,yval)
			else : graphs[ifile].SetPoint(graphs[ifile].GetN(),entry.kl,yval)
			if ifile == 5 : ###TO BE REMOVED ###
				graphs[ifile].SetPointError(graphs[ifile].GetN()-1,0,0,0,0)
			else :
				for elow in treeErrLow :
					if plotMu :
						if abs(elow.r-entry.r)<0.0001 : 
							errlow = 2.0*elow.deltaNLL
					else :
						#print elow.kl, entry.kl
						if abs(elow.kl-entry.kl)< 0.0001 : 
							errlow = 2.0*elow.deltaNLL
				for ehigh in treeErr :
					if plotMu :
						if abs(ehigh.r-entry.r)<0.0001 : 
							errhigh = 2.0*ehigh.deltaNLL
					else :
						if abs(ehigh.kl-entry.kl)<0.0001 : 
							errhigh = 2.0*ehigh.deltaNLL
				if plotMu : xval = entry.r
				else : xval = entry.kl
				if abs(1.0-xval)<0.0001 :
					errlow = yval
					errhigh = yval
				graphs[ifile].SetPointError(graphs[ifile].GetN()-1,0,0,yval-errlow,errhigh-yval)
			#grapherrs[ifile].SetPoint(ipoint,entry.kl*0.85,2.0*entry.deltaNLL)
			#grapherrslow[ifile].SetPoint(ipoint,entry.kl*1.25,2.0*entry.deltaNLL)
			#ipoint = ipoint+1
print "canvas"
c=TCanvas()
c.SetTicks(1,1)
c.SetLeftMargin(0.14)
c.SetRightMargin(0.08)
c.cd()
gStyle.SetOptTitle(0)

#mg = TMultiGraph()
minx =0.7
maxx =1.3
if plotMu :
	minx=0.8
	maxx=1.2
graphs[0].SetLineColor(colors[0])
graphs[0].SetLineWidth(3)
graphs[0].Sort()
graphs[0].SetTitle(titles[0])
graphs[0].SetFillColorAlpha(colors[0],0.35)
graphs[0].SetFillStyle(3001)
graphs[0].Draw("AL3")
#mg.Add(graphs[0])
graphs[0].GetYaxis().SetRangeUser(0,12)
graphs[0].GetXaxis().SetRangeUser(minx,maxx)
c.Modified()
graphs[0].GetYaxis().SetLimits(0,12)
graphs[0].GetXaxis().SetLimits(minx,maxx)
c.Modified()
c.Update()

#SetRangeUser (applicato a entrambi gli assi), Modified(), SetLimits (applicato a entrambi gli assi), Modified(), Update()
graphs[0].GetXaxis().SetTitle("k_{#lambda}")
if plotMu : graphs[0].GetXaxis().SetTitle("#mu=#sigma/#sigma_{obs}")
graphs[0].GetYaxis().SetTitle("-2#Delta ln L")
graphs[0].GetYaxis().SetTitleOffset(0.9)
graphs[0].GetXaxis().SetTitleOffset(0.85)
graphs[0].GetXaxis().SetTitleSize(0.05)
graphs[0].GetYaxis().SetTitleSize(0.05)
graphs[0].GetYaxis().SetRangeUser(0,12)
graphs[0].GetXaxis().SetRangeUser(minx,maxx)
c.Modified()
graphs[0].GetYaxis().SetLimits(0,12)
graphs[0].GetYaxis().SetLimits(minx,maxx)
c.Modified()
c.Update()

mini = graphs[0].GetXaxis().GetXmin()
maxi = graphs[0].GetXaxis().GetXmax()

for ig in range(1,len(graphs)) :
	graphs[ig].SetLineColor(colors[ig])
	graphs[ig].SetFillColorAlpha(colors[ig],0.35)
	graphs[ig].SetFillStyle(fillstyle[ig])
	#if ig == 2 : graphs[ig].SetFillStyle(3345)
	#if ig == 1 : graphs[ig].SetFillStyle(3354)
	graphs[ig].SetLineWidth(3)
	graphs[ig].SetTitle(titles[ig])
	graphs[ig].Sort()
	if ig == len(graphs)-1 : 
		graphs[ig].SetLineStyle(2)
		graphs[ig].SetFillStyle(0)
		graphs[ig].SetFillColor(0)
		graphs[ig].Draw("LSAME")
	else :graphs[ig].Draw("L3SAME")
	#mg.Add(graphs[ig])
#mg.Draw("L3")
leg = TLegend(0.4,0.62,0.8,0.87) #c.BuildLegend()
leg.SetLineColor(0)
leg.SetLineStyle(0)
leg.SetLineWidth(0)
leg.SetFillStyle(0)
leg.SetShadowColor(10)
leg.SetTextSize(0.030)
leg.SetTextFont(42)
leg.AddEntry(graphs[0]) #4l
leg.AddEntry(graphs[1]) #4b
leg.AddEntry(graphs[4]) #bbtt
leg.AddEntry(graphs[2]) #bbgg
leg.AddEntry(graphs[3]) #comb
leg.AddEntry(graphs[5]) #comb NS

leg.Draw("SAME")
#leg.SetX1(0.4)
#leg.SetX2(0.8)
#leg.SetY1(0.62)
#leg.SetY2(0.87)

print mini, maxi
mini = 0.7
maxi = 1.3
maxY = 12
print mini, maxi


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

Text2 = TPaveText(0.18, 0.71,0.33,0.85,'brNDC')
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


graphs[0].GetYaxis().SetRangeUser(0,maxY)
graphs[0].GetXaxis().SetRangeUser(mini,maxi)
c.Modified()
graphs[0].GetYaxis().SetLimits(0,maxY)
graphs[0].GetXaxis().SetLimits(mini,maxi)
c.Modified()
c.Update()

lineone = TLine(0.7,1,1.3,1)
linetwo = TLine(0.7,3.84,1.3,3.84)
lineone.SetLineColor(kGray+1)
linetwo.SetLineColor(kGray+1)
lineone.SetLineWidth(3)
lineone.SetLineStyle(2)
linetwo.SetLineWidth(3)
linetwo.SetLineStyle(2)
lineone.Draw("SAME")
linetwo.Draw("SAME")

Text1sigma = TPaveText(0.84, 0.14,0.9,0.14+0.07,'brNDC')
#text = "1#sigma"
text = "68% C.I."
Text1sigma.SetTextAlign(12);
#Text.SetNDC(True) 
Text1sigma.SetTextSize(0.036)
Text1sigma.AddText(text)
Text1sigma.SetFillStyle(0)
Text1sigma.SetFillColor(kWhite)
Text1sigma.SetLineStyle(0)
Text1sigma.SetTextColor(kGray+1)
Text1sigma.SetBorderSize(0)
#Text1sigma.Draw()

Text2sigma = TPaveText(0.84, 0.4,0.9,0.4+0.07,'brNDC')
#text = "2#sigma"
text = "95% C.I."
Text2sigma.SetTextAlign(12);
#Text.SetNDC(True) 
Text2sigma.SetTextSize(0.036)
Text2sigma.AddText(text)
Text2sigma.SetFillStyle(0)
Text2sigma.SetFillColor(kWhite)
Text2sigma.SetLineStyle(0)
Text2sigma.SetTextColor(kGray+1)
Text2sigma.SetBorderSize(0)
#Text2sigma.Draw()
if plotMu : 
	c.SaveAs("plot2020_mu"+suffix+".pdf")
	c.SaveAs("plot2020_mu"+suffix+".png")
else : 
	c.SaveAs("plot2020_kl"+suffix+".pdf")
	c.SaveAs("plot2020_kl"+suffix+".png")
#ig.Print()

#graphs[3].Print()
#graphs[4].Print()

#raw_input()
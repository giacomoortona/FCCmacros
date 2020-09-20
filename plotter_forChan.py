from ROOT import *

plotAll = 5 # 0->bbtt;1->bbtl;2->bbaa;3->bbbb;-1->disable feature
plotMu = True
channel = ["bbtt","bbtt_semilep","boosted","bbaa","combCard","bb4l"]
fileListAll = []
if plotAll == 0 :
	fileListAll = ["higgsCombinecard1.00_bbtt_sel0_forComb_syst1.txt_kl_.MultiDimFit.mH120.root",
			   "higgsCombinecard1.00_bbtt_sel0_forComb_syst2.txt_kl_.MultiDimFit.mH120.root",
			   "higgsCombinecard1.00_bbtt_sel0_forComb_syst3.txt_kl_.MultiDimFit.mH120.root",
			   "higgsCombinecard1.00_bbtt_sel0_forComb_syst3.txt_kl_NoSyst.MultiDimFit.mH120.root",
				]
if plotAll == 2 :
	fileListAll = ["higgsCombinecard1.00_boosted_syst1.txt_kl_.MultiDimFit.mH120.root",
			   "higgsCombinecard1.00_boosted_syst2.txt_kl_.MultiDimFit.mH120.root",
			   "higgsCombinecard1.00_boosted_syst3.txt_kl_.MultiDimFit.mH120.root",
			   "higgsCombinecard1.00_boosted_syst3.txt_kl_NoSyst.MultiDimFit.mH120.root",
				]
elif plotAll == 3 : 
	fileListAll = ["higgsCombinecard1.00_syst1_sel0.txt_kl_.MultiDimFit.mH120.root",
			   "higgsCombinecard1.00_syst2_sel0.txt_kl_.MultiDimFit.mH120.root",
			   "higgsCombinecard1.00_syst3_sel0.txt_kl_.MultiDimFit.mH120.root",
			   "higgsCombinecard1.00_syst3_sel0.txt_kl_NoSyst.MultiDimFit.mH120.root",
			   #"higgsCombinecard1.00_syst2_sel0.txt_kl_NoSyst_sel0.MultiDimFit.mH120.root",
				]
elif plotAll == 4 : 
	fileListAll = ["higgsCombinecombCard_1.00_syst1.txt_kl_.MultiDimFit.mH120.root",
			   "higgsCombinecombCard_1.00_syst2.txt_kl_.MultiDimFit.mH120.root",
			   "higgsCombinecombCard_1.00_syst3.txt_kl_.MultiDimFit.mH120.root",
			   "higgsCombinecombCard_1.00_syst3.txt_kl_NoSyst.MultiDimFit.mH120.root",
			   #"higgsCombinecard1.00_syst2_sel0.txt_kl_NoSyst_sel0.MultiDimFit.mH120.root",
				]
elif plotAll == 5 : 
	fileListAll = ["higgsCombinecard1.00_bb4l_syst1.txt_kl_.MultiDimFit.mH120.root",
			   "higgsCombinecard1.00_bb4l_syst2.txt_kl_.MultiDimFit.mH120.root",
			   "higgsCombinecard1.00_bb4l_syst3.txt_kl_.MultiDimFit.mH120.root",
			   "higgsCombinecard1.00_bb4l_syst3.txt_kl_NoSyst.MultiDimFit.mH120.root",
			   #"higgsCombinecard1.00_syst2_sel0.txt_kl_NoSyst_sel0.MultiDimFit.mH120.root",
				]

outString = "test"
if plotAll >= 0: outString="all"+channel[plotAll]
if plotMu : 
	for ifile in range(len(fileListAll)) : 
		fileListAll[ifile] = fileListAll[ifile].replace("kl","mu")

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
colors =   [kBlue,kRed+1,kPink,kGreen-2,kBlack,kBlack,kYellow+2,kCyan]
#titles = ["bbgg1","bbtt1","c3","c2","c1"]
titles = ["bb#gamma#gamma","bb#tau_{h}#tau_{h}","bb#tau_{h}#tau_{l}","bbbb","Combined","Combined - no syst.","bb4l1","c1","nosyst"]

#fileList = ["higgsCombinebbgg_scankl_syst1_bkTimes1.MultiDimFit.mH120.root","higgsCombinebbtt_scankl_syst1_bkTimes1.MultiDimFit.mH120.root","higgsCombinebbcombno4b_scankl_syst3_bkTimes1.MultiDimFit.mH120.root","higgsCombinebbcombno4b_scankl_syst2_bkTimes1.MultiDimFit.mH120.root","higgsCombinebbcombno4b_scankl_syst1_bkTimes1.MultiDimFit.mH120.root"]
#fileList = ["higgsCombinebbgg_scankl_syst1_bkTimes1.MultiDimFit.mH120.root","higgsCombinebbtt_scankl_syst1_bkTimes1.MultiDimFit.mH120.root","higgsCombinebbbb_scankl_syst1_bkTimes1.MultiDimFit.mH120.root","higgsCombinebb4l_scankl_syst1_bkTimes1.MultiDimFit.mH120.root","higgsCombinebbcombno4b_scankl_syst1_bkTimes1.MultiDimFit.mH120.root","higgsCombinebbcombno4b_scankl_sel2_syst1noSyst_bkTimes1.MultiDimFit.mH120.root"]
fileErrList = ["higgsCombinebbcomb_scankl_syst3_bkTimes1.MultiDimFit.mH120.root","higgsCombineTest0.MultiDimFit.mH120.root","higgsCombineTest2.MultiDimFit.mH120.root","higgsCombinebbcomb_scankl_syst1noSyst_bkTimes1.MultiDimFit.mH120.root","higgsCombinebbcomb_scankl_syst1noSyst_bkTimes1.MultiDimFit.mH120.root"]
fileErrListLow = ["higgsCombinebbcomb_scankl_syst3_bkTimes1.MultiDimFit.mH120.root","higgsCombineTest0.MultiDimFit.mH120.root","higgsCombineTest2.MultiDimFit.mH120.root","higgsCombinebbcomb_scankl_syst1noSyst_bkTimes1.MultiDimFit.mH120.root","higgsCombinebbcomb_scankl_syst1noSyst_bkTimes1.MultiDimFit.mH120.root"]
#fileList = ["higgsCombinebbtt_scankl_all_sel0_syst1Syst_bkTimes1_forComb.MultiDimFit.mH120.root","higgsCombinebbbb_scankl_all_sel0_syst1Syst_bkTimes1.MultiDimFit.mH120.root","higgsCombinebbaa_1.MultiDimFit.mH120.root"]
fileList = ["higgsCombinebbtt_scankl_all_sel0_syst1Syst_bkTimes1_forComb.MultiDimFit.mH120.root","higgsCombinebbaa_1_nosyst.MultiDimFit.mH120.root","higgsCombinebbaa_1.MultiDimFit.mH120.root"]
colors =   [kBlue,kRed+1,kGreen,kBlack,kBlack,kYellow+2,kCyan]
#titles = ["bbgg1","bbtt1","c3","c2","c1"]
titles = ["bbtt","bbaa_nosyst","bbaa"]
if plotAll>=0: 
	fileList = fileListAll
	if plotAll == 0 :
		titles = ["bb#tau_{h}#tau_{h} - I (opt.)","bb#tau_{h}#tau_{h} - II (real.)","bb#tau_{h}#tau_{h} - III (pes.)","bb#tau_{h}#tau_{h} - no syst."]
		colors =   [kRed+3,kRed+1,kMagenta,kBlack]
	elif plotAll == 2 :
		titles = ["bbbb - I (opt.)","bbbb - II (real.)","bbbb - III (pes.)","bbbb - no syst."]
		colors =   [kGreen+3,kGreen+1,kGreen-2,kBlack]
	elif plotAll == 3 : 
		titles  = ["bb#gamma#gamma - I (opt.)","bb#gamma#gamma - II (real.)","bb#gamma#gamma - III (pes.)","bb#gamma#gamma - no syst."]
		#titles  = ["bb#gamma#gamma - sel0","bb#gamma#gamma - sel1","bb#gamma#gamma - sel2","bb#gamma#gamma - sel3"]
		colors =   [kBlue+2,kBlue,kCyan+2,kBlack]
	elif plotAll == 4 : 
		titles  = ["Combined - opt","Combined - int","Combined - pes","Combined - NoSyst"]
		#titles  = ["bb#gamma#gamma - sel0","bb#gamma#gamma - sel1","bb#gamma#gamma - sel2","bb#gamma#gamma - sel3"]
		colors =   [kBlue+2,kBlue,kCyan+2,kBlack]
	elif plotAll == 5 : 
		titles  = ["bbZZ(4l) - I (opt.)","bbZZ(4l) - II (real.)","bbZZ(4l) - III (pes.)","bbZZ(4l) - no syst."]
		#titles  = ["bb#gamma#gamma - sel0","bb#gamma#gamma - sel1","bb#gamma#gamma - sel2","bb#gamma#gamma - sel3"]
		colors =   [kOrange-2,kYellow-8,kYellow-3,kBlack]

graphs = []
grapherrs = []
grapherrslow = []
#plotPrecision()
#raw_input()
for i in range(len(fileList)) : 
	graphs.append(TGraph())
	#grapherrs.append(TGraph())
	#grapherrslow.append(TGraph())
for ifile in range(len(fileList)):
	inF = TFile.Open(fileList[ifile],"READ")
	tree = inF.Get("limit")


	ipoint = 0
	for entry in tree :
		if ifile == 3 :
			if plotMu : print entry.r, 2.0*entry.deltaNLL
		if(entry.deltaNLL<10): 
			if ifile == 10 or plotMu: graphs[ifile].SetPoint(ipoint,entry.r,2.0*entry.deltaNLL)
			else : graphs[ifile].SetPoint(ipoint,entry.kl,2.0*entry.deltaNLL)
			#graphs[ifile].SetPointError(ipoint,0,0,2.0*entry.deltaNLL*0.1,2.0*entry.deltaNLL*0.15)
			#grapherrs[ifile].SetPoint(ipoint,entry.kl*0.85,2.0*entry.deltaNLL)
			#grapherrslow[ifile].SetPoint(ipoint,entry.kl*1.25,2.0*entry.deltaNLL)
			ipoint = ipoint+1

c=TCanvas()#"","",600,600)
c.SetTicks(1,1)
c.SetLeftMargin(0.14)
c.SetRightMargin(0.08)
c.cd()
gStyle.SetOptTitle(0)

graphs[0].SetLineColor(colors[0])
graphs[0].SetLineWidth(3)
#graphs[3].SetLineStyle(3)
graphs[0].Sort()
graphs[0].SetTitle(titles[0])
graphs[0].SetFillColor(colors[0])
graphs[0].SetFillStyle(3001)
if plotAll >= 0 : 
	graphs[0].SetFillStyle(0)
	graphs[0].SetFillColor(0)


mini = 0.9 #graphs[3].GetXaxis().GetXmin()
maxi = 1.1 #graphs[3].GetXaxis().GetXmax()
maxY = 6
if plotAll>2 : maxY = 12
#if plotMu :
#	mini = 0.9
#	maxi = 1.1
if plotAll == 2 or plotAll == 5:
	mini = 0.7
	maxi = 1.3


graphs[0].Draw("AL3")
graphs[0].GetXaxis().SetTitle("k_{#lambda}")
if plotMu : graphs[0].GetXaxis().SetTitle("#mu=#sigma/#sigma_{obs}")
graphs[0].GetYaxis().SetTitle("-2#Delta ln L")
graphs[0].GetYaxis().SetTitleOffset(0.9)
graphs[0].GetXaxis().SetTitleOffset(0.85)
graphs[0].GetXaxis().SetTitleSize(0.05)
graphs[0].GetYaxis().SetTitleSize(0.05)

graphs[0].GetYaxis().SetRangeUser(0,maxY)
graphs[0].GetXaxis().SetRangeUser(mini,maxi)
c.Modified()
graphs[0].GetYaxis().SetLimits(0,maxY)
#graphs[0].GetXaxis().SetRangeUser(mini,maxi)
graphs[0].GetXaxis().SetLimits(mini,maxi)
c.Modified()
c.Update()

if plotAll >= 0 : graphs[3].SetLineStyle(2)

for ig in range(1,len(graphs)) :
	graphs[ig].SetLineColor(colors[ig])
	graphs[ig].SetFillColor(colors[ig])
	graphs[ig].SetFillStyle(3002)
	graphs[ig].SetLineWidth(3)
	graphs[ig].SetTitle(titles[ig])
	graphs[ig].Sort()
	if ig == 4 : graphs[ig].SetLineStyle(2)
	if ig == 4 or plotAll >= 0 :
		graphs[ig].SetFillStyle(0)
		graphs[ig].SetFillColor(0)
		graphs[ig].Draw("LSAME")
	else : graphs[ig].Draw("L3SAME")
#leg = c.BuildLegend()

print mini, maxi
lineone = TLine(mini,1,maxi,1)
linetwo = TLine(mini,3.84,maxi,3.84)
lineone.SetLineColor(kGray+1)
linetwo.SetLineColor(kGray+1)
lineone.SetLineWidth(3)
lineone.SetLineStyle(2)
linetwo.SetLineWidth(3)
linetwo.SetLineStyle(2)
lineone.Draw("SAME")
linetwo.Draw("SAME")

leg = TLegend(0.4,0.8,0.83,0.63)
leg.SetLineColor(0)
leg.SetLineStyle(0)
leg.SetLineWidth(0)
leg.SetFillStyle(0)
leg.SetShadowColor(10)
leg.SetTextSize(0.030)
leg.SetTextFont(42)
leg.AddEntry(graphs[3])
leg.AddEntry(graphs[2])
leg.AddEntry(graphs[1])
leg.AddEntry(graphs[0])
leg.Draw("SAME")

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

Text2 = TPaveText(0.18, 0.71,0.4,0.85,'brNDC')
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
#graphs[0].GetXaxis().SetRangeUser(mini,maxi)
graphs[0].GetXaxis().SetLimits(mini,maxi)
c.Modified()
c.Update()

graphs[3].Print()
#c.Modified()
#c.Update()


raw_input()
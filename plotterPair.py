from ROOT import *

#higgsCombinecard1.00_syst2_sel0.txt_kl_2_default.MultiDimFit.mH120.root
#higgsCombinecard1.00_syst2_sel0.txt_kl_NoSyst_default.MultiDimFit.mH120.root
#higgsCombinecard1.00_syst2_sel0.txt_kl_2_13.MultiDimFit.mH120.root
#higgsCombinecard1.00_syst2_sel0.txt_kl_NoSyst_13.MultiDimFit.mH120.root
#higgsCombinecard1.00_syst2_sel0.txt_kl_2_27.MultiDimFit.mH120.root
#higgsCombinecard1.00_syst2_sel0.txt_kl_NoSyst_27.MultiDimFit.mH120.root
#higgsCombine1.00_syst3_sel0_II_MT.MultiDimFit.mH120.root
#higgsCombine1.00_comb_3_ITTT_noSyst.MultiDimFit.mH120.root
#for sc in I II III ; do for bwp in L M T ; do for pwp in M T

#best WP: comb I - MLMLL : [0.9728,1.0273] 68% CL  -->  delta_kl = 0.0272
#best WP: comb II - MLMLM : [0.9556,1.0447] 68% CL  -->  delta_kl = 0.0446
#best WP: comb III - MLLLT : [0.9349,1.0662] 68% CL  -->  delta_kl = 0.0657

#${pwp}${bwpgamma}${bwptau}${bwpb}${lwp}
#bbaa : pwp/bwp
#bbbb: bwp
#bbtt: lwp/bwp



import os,re, optparse

def parseOptions():

    usage = ('usage: %prog [options] datasetList\n'+ '%prog -h for help')
    parser = optparse.OptionParser(usage)
    parser.add_option('-p', '--channel', dest='plotChan', type='int', default=0, help='comb , bbaa , bbbb , bbtt , bbtahtah , bbtahtal , bb4l')
    parser.add_option('-w', '--wait', dest='wait', action="store_true",default=False, help='raw input')
    parser.add_option('-m', '--plotmu', dest='plotmu', action="store_true",default=False, help='mu instead of kl')
    global opt, args
    (opt, args) = parser.parse_args()

print "started"
parseOptions()
global opt, args


pWP = ["M","M","M"]
bgWP = ["M","M","M"]
btWP = ["M","M","M"]
bWP = ["M","M","M"]
lWP = ["M","M","M"]
suffix = "v58_MMMMM"

plotAll = opt.plotChan # 0->bbtt;1->bbtl;2->bbbb;3->bbaa;4->combined,5->bbZZ4l,6->bbttcombined -1->disable feature
eosDir = "/eos/user/g/gortona/FCC/Results_v58/"
plotMu = False
if opt.plotmu : plotMu = True

appender = ""
if plotMu : appender = "_mu"

#channel = ["bbtt","bbtt_semilep","boosted","bbaa","combCard","bb4l","bbttcomb"]
channel = ["comb","bbaa","bbbb","bbtt","bbtahtah","bbtahtal","bb4l"]
fileListAll = []
if plotAll == 0 :#higgsCombinecard1.00_syst1_sel0.txt_kl_1_default.MultiDimFit.mH120.root
#	fileListAll = ["higgsCombinecard1.00_bbtt_sel0_forComb_syst1.txt_kl_1.MultiDimFit.mH120.root",
#			   "higgsCombinecard1.00_bbtt_sel0_forComb_syst2.txt_kl_2.MultiDimFit.mH120.root",
#			   "higgsCombinecard1.00_bbtt_sel0_forComb_syst3.txt_kl_3.MultiDimFit.mH120.root",
#			   "higgsCombinecard1.00_bbtt_sel0_forComb_syst2.txt_kl_NoSyst.MultiDimFit.mH120.root",
#				]
	fileListAll = ["higgsCombine1.00_comb_1_I{0}{1}{2}{3}{4}{5}.MultiDimFit.mH120.root".format(pWP[0],bgWP[0],btWP[0],bWP[0],lWP[0],appender),
			   "higgsCombine1.00_comb_2_II{0}{1}{2}{3}{4}{5}.MultiDimFit.mH120.root".format(pWP[1],bgWP[1],btWP[1],bWP[1],lWP[1],appender),
			   "higgsCombine1.00_comb_3_III{0}{1}{2}{3}{4}{5}.MultiDimFit.mH120.root".format(pWP[2],bgWP[2],btWP[2],bWP[2],lWP[2],appender),
			   "higgsCombine1.00_comb_1_I{0}{1}{2}{3}{4}_noSyst{5}.MultiDimFit.mH120.root".format(pWP[0],bgWP[0],btWP[0],bWP[0],lWP[0],appender),
				]
if plotAll == 1 :
	fileListAll = ["higgsCombine1.00_bbaa_btag_1_I{0}{1}{2}.MultiDimFit.mH120.root".format(pWP[0],bgWP[0],appender),
			   "higgsCombine1.00_bbaa_btag_2_II{0}{1}{2}.MultiDimFit.mH120.root".format(pWP[1],bgWP[1],appender),
			   "higgsCombine1.00_bbaa_btag_3_III{0}{1}{2}.MultiDimFit.mH120.root".format(pWP[2],bgWP[2],appender),
			   "higgsCombine1.00_bbaa_btag_1_I{0}{1}_noSyst{2}.MultiDimFit.mH120.root".format(pWP[0],bgWP[0],appender),
			   #"higgsCombine1.00_bbaa_btag_3_ITT.MultiDimFit.mH120.root",
			   #"higgsCombine1.00_bbaa_btag_3_ITT.MultiDimFit.mH120.root",
				]

if plotAll == 2 :
	fileListAll = ["higgsCombine1.00_bbbb_btag_1_I{0}{1}.MultiDimFit.mH120.root".format(bWP[0],appender),
			   "higgsCombine1.00_bbbb_btag_2_II{0}{1}.MultiDimFit.mH120.root".format(bWP[1],appender),
			   "higgsCombine1.00_bbbb_btag_3_III{0}{1}.MultiDimFit.mH120.root".format(bWP[2],appender),
			   "higgsCombine1.00_bbbb_btag_1_I{0}_noSyst{1}.MultiDimFit.mH120.root".format(bWP[0],appender),
				]
#if plotAll == 2 :
#	fileListAll = ["FCCW3_results/higgsCombinecard1.00_boosted_syst1.txt_kl_.MultiDimFit.mH120.root",
#			   "FCCW3_results/higgsCombinecard1.00_boosted_syst2.txt_kl_.MultiDimFit.mH120.root",
#			   "FCCW3_results/higgsCombinecard1.00_boosted_syst3.txt_kl_.MultiDimFit.mH120.root",
#			   "FCCW3_results/higgsCombinecard1.00_boosted_syst3.txt_kl_NoSyst.MultiDimFit.mH120.root",
#				]
elif plotAll == 3 : 
	fileListAll = ["higgsCombine1.00_bbttcomb_btag_1_I{0}{1}{2}.MultiDimFit.mH120.root".format(lWP[0],btWP[0],appender),
			   "higgsCombine1.00_bbttcomb_btag_2_II{0}{1}{2}.MultiDimFit.mH120.root".format(lWP[1],btWP[1],appender),
			   "higgsCombine1.00_bbttcomb_btag_3_III{0}{1}{2}.MultiDimFit.mH120.root".format(lWP[2],btWP[2],appender),
			   "higgsCombine1.00_bbttcomb_btag_1_I{0}{1}_noSyst{2}.MultiDimFit.mH120.root".format(lWP[0],btWP[0],appender),
				]
elif plotAll == 4 : 
	fileListAll = ["higgsCombine1.00_bbtt_btag_1_I{0}{1}{2}.MultiDimFit.mH120.root".format(lWP[0],btWP[0],appender),
			   "higgsCombine1.00_bbtt_btag_2_II{0}{1}{2}.MultiDimFit.mH120.root".format(lWP[1],btWP[1],appender),
			   "higgsCombine1.00_bbtt_btag_3_III{0}{1}{2}.MultiDimFit.mH120.root".format(lWP[2],btWP[2],appender),
			   "higgsCombine1.00_bbtt_btag_1_I{0}{1}_noSyst{2}.MultiDimFit.mH120.root".format(lWP[0],btWP[0],appender),
				]
elif plotAll == 5 : 
	fileListAll = ["higgsCombine1.00_bbtl_btag_1_I{0}{1}{2}.MultiDimFit.mH120.root".format(lWP[0],btWP[0],appender),
			   "higgsCombine1.00_bbtl_btag_2_II{0}{1}{2}.MultiDimFit.mH120.root".format(lWP[1],btWP[1],appender),
			   "higgsCombine1.00_bbtl_btag_3_III{0}{1}{2}.MultiDimFit.mH120.root".format(lWP[2],btWP[2],appender),
			   "higgsCombine1.00_bbtl_btag_1_I{0}{1}_noSyst{2}.MultiDimFit.mH120.root".format(lWP[0],btWP[0],appender),
				]
elif plotAll == 6 :#higgsCombinecombCardbbtt_1.00_syst2
	fileListAll = ["higgsCombinecard1.00_bb4l_syst1.txt_kl_1.MultiDimFit.mH120.root",
			   "higgsCombinecard1.00_bb4l_syst2.txt_kl_2.MultiDimFit.mH120.root",
			   "higgsCombinecard1.00_bb4l_syst3.txt_kl_3.MultiDimFit.mH120.root",
			   "higgsCombinecard1.00_bb4l_syst2.txt_kl_NoSyst.MultiDimFit.mH120.root",
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
#titles = ["bbtt","bbaa_nosyst","bbaa"]
channel = ["comb","bbaa","bbbb","bbtt","bbtahtah","bbtahtal","bb4l"]

if plotAll>=0: 
	fileList = fileListAll
	if plotAll == 0 :
		#titles = ["bb#tau_{h}#tau_{h} - syst. I","bb#tau_{h}#tau_{h} - syst. II","bb#tau_{h}#tau_{h} - syst. III","bb#tau_{h}#tau_{h} - no syst."]
		titles  = ["Combined - scenario I","Combined - scenario II","Combined - scenario III","Combined - no syst."]
		
	elif plotAll == 1 :
		#titles = ["bb#tau_{h}#tau_{l} - scenario I","bb#tau_{h}#tau_{l} - scenario II","bb#tau_{h}#tau_{l} - scenario III","bb#tau_{h}#tau_{l} - no syst."]
		titles = ["bb#gamma#gamma - scenario I","bb#gamma#gamma - scenario II","bb#gamma#gamma - scenario III","bb#gamma#gamma - no syst."]
		#colors =   [kRed+3,kRed+1,kMagenta,kBlue+2,kBlue,kCyan+2]
		colors =   [kBlue+2,kBlue,kCyan+2,kBlack]
	elif plotAll == 2 :
		titles = ["bbbb - scenario I","bbbb - scenario II","bbbb - scenario III","bbbb - no syst."]
		colors =   [kGreen+3,kGreen+1,kGreen-2,kBlack]
	elif plotAll == 3 : 
		titles = ["bb#tau_{h}#tau_{h} + bb#tau_{h}#tau_{l} - scenario I","bb#tau_{h}#tau_{h} + bb#tau_{h}#tau_{l} - scenario II","bb#tau_{h}#tau_{h} + bb#tau_{h}#tau_{l} - scenario III","bb#tau_{h}#tau_{h} + bb#tau_{h}#tau_{l} - no syst."]
		#titles  = ["bb#gamma#gamma - sel0","bb#gamma#gamma - sel1","bb#gamma#gamma - sel2","bb#gamma#gamma - sel3"]
		colors =   [kOrange-2,kYellow-8,kYellow-3,kBlack] #colors =   [kRed+3,kRed+1,kMagenta,kBlack,kBlue+2kBlue,kCyan+2]
	elif plotAll == 4 : 
		titles  = ["bb#tau_{h}#tau_{h} - scenario I","bb#tau_{h}#tau_{h} - scenario II","bb#tau_{h}#tau_{h} - scenario III","bb#tau_{h}#tau_{h} - no syst."]
		#titles  = ["bb#gamma#gamma - sel0","bb#gamma#gamma - sel1","bb#gamma#gamma - sel2","bb#gamma#gamma - sel3"]
		colors =   [kOrange-2,kYellow-8,kYellow-3,kBlack] #colors =   [kRed+3,kRed+1,kMagenta,kBlack,kBlue+2,kBlue,kCyan+2]
	elif plotAll == 5 : 
		titles  = ["bb#tau_{h}#tau_{l} - scenario I","bb#tau_{h}#tau_{l} - scenario II","bb#tau_{h}#tau_{l} - scenario III","bb#tau_{h}#tau_{l} - no syst."]
		#titles  = ["bb#gamma#gamma - sel0","bb#gamma#gamma - sel1","bb#gamma#gamma - sel2","bb#gamma#gamma - sel3"]
		colors =   [kOrange-2,kYellow-8,kYellow-3,kBlack]
		colors =   [kRed+3,kRed+1,kMagenta,kBlack,kBlue+2,kBlue,kCyan+2]
	elif plotAll == 6 :
		titles  = ["bbZZ(4l) - scenario I","bbZZ(4l) - scenario II","bbZZ(4l) - scenario III","bbZZ(4l) - no syst."]
		colors =   [kRed+3,kRed+1,kMagenta,kBlue+2,kBlue,kCyan+2]

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
	inF = TFile.Open(eosDir+fileList[ifile],"READ")
	tree = inF.Get("limit")


	#ipoint = 0
	for entry in tree :
		#if ifile == 3 :
		#	if plotMu : print entry.r, 2.0*entry.deltaNLL
		if ifile == 10 or plotMu: 
			if plotAll == 4 and ifile == 2:
				if entry.r > 1.08 and entry.r <  1.09 : continue
				elif entry.r > 0.94 and entry.r <  0.944 : continue
			graphs[ifile].SetPoint(graphs[ifile].GetN(),entry.r,2.0*entry.deltaNLL)
		else : 
			if plotAll == 4 and ifile == 2:
				if entry.kl > 1.136 and entry.kl <  1.142 : continue
				elif entry.kl > 0.847 and entry.kl <  0.87 : continue
			graphs[ifile].SetPoint(graphs[ifile].GetN(),entry.kl,2.0*entry.deltaNLL)
			#if plotAll is not 0 : 
			#if not plotAll == 4 or entry.kl < 1.136 or entry.kl >  1.142 : 
			#elif entry.kl <0.95 or entry.kl >1.04 or (entry.kl>0.99 and entry.kl<1.008) or ifile is not 2 :graphs[ifile].SetPoint(graphs[ifile].GetN(),entry.kl,2.0*entry.deltaNLL)
			#graphs[ifile].SetPointError(ipoint,0,0,2.0*entry.deltaNLL*0.1,2.0*entry.deltaNLL*0.15)
			#grapherrs[ifile].SetPoint(ipoint,entry.kl*0.85,2.0*entry.deltaNLL)
			#grapherrslow[ifile].SetPoint(ipoint,entry.kl*1.25,2.0*entry.deltaNLL)
			

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
graphs[0].SetMarkerColor(colors[0])
graphs[0].SetMarkerStyle(0)
if plotAll >= 0 : 
	graphs[0].SetFillStyle(0)
	graphs[0].SetFillColor(0)


y168 = 0.135
y195 = 0.34
mini = 0.8 #graphs[3].GetXaxis().GetXmin()
maxi = 1.2 #graphs[3].GetXaxis().GetXmax()
maxY = 6
if plotAll == 1 : 
	maxY = 12
	y168 = 0.15
if (plotAll >=2) and not plotMu:
	mini = 0.7 #graphs[3].GetXaxis().GetXmin()
	maxi = 1.3 #graphs[3].GetXaxis().GetXmax()
	y168 = 0.22
	y195 = 0.595

#if plotAll == 1 and not plotMu : maxY = 2
#if plotMu :
#	mini = 0.9
#	maxi = 1.1



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
	graphs[ig].SetMarkerColor(colors[ig])
	graphs[ig].SetMarkerStyle(0)
	graphs[ig].SetFillStyle(3002)
	graphs[ig].SetLineWidth(3)
	print ig, titles
	graphs[ig].SetTitle(titles[ig])
	graphs[ig].Sort()
	if ig == len(fileList) : graphs[ig].SetLineStyle(2)
	if ig == len(fileList) or plotAll >= 0 :
		graphs[ig].SetFillStyle(0)
		graphs[ig].SetFillColor(0)
		#graphs[ig].Draw("LSAME")
	#else : 
	graphs[ig].Draw("L3SAME")
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
if not ( not plotMu and plotAll == 0): linetwo.Draw("SAME")
xleg = [0.4,0.8,0.63,0.63]
#if plotAll == 1 : 
#	xleg[0] = 0.75
#	xleg[2] = 0.9
leg = TLegend(xleg[0],xleg[1],xleg[2],xleg[3])
leg.SetLineColor(0)
leg.SetLineStyle(0)
leg.SetLineWidth(0)
leg.SetFillStyle(0)
leg.SetFillColor(0)
leg.SetShadowColor(10)
leg.SetTextSize(0.030)
leg.SetTextFont(42)
#leg.AddEntry(graphs[5])
#leg.AddEntry(graphs[4])
leg.AddEntry(graphs[3])
leg.AddEntry(graphs[0])
leg.AddEntry(graphs[1])
leg.AddEntry(graphs[2])
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
print Text.GetTextFont()

Text2 = TPaveText(0.18, 0.71,0.35,0.85,'brNDC')
rightText = re.split(",")#, rightText)
#text = '#it{#bf{' + rightText[0] +'}}'
text = '#it{' + rightText[0] +'}'
Text2.SetTextAlign(12);
#Text.SetNDC(True) 
Text2.SetTextSize(0.036)
Text2.AddText(text)
text = '#it{' + rightText[1] +'}'
Text2.AddText(text)
#Text2.SetFillStyle(0)
Text2.SetFillColor(kWhite)
Text2.SetLineStyle(0)
Text2.SetBorderSize(0)
Text2.SetTextFont(62)
Text2.Draw()
#print Text2.GetTextFont()

Text1sigma = TPaveText(0.14, y168,0.2,y168+0.07,'brNDC')
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
Text1sigma.Draw()

Text2sigma = TPaveText(0.14, y195,0.2,y195+0.07,'brNDC')
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
#if not ( not plotMu and plotAll == 0): 
Text2sigma.Draw()


graphs[0].GetYaxis().SetRangeUser(0,maxY)
graphs[0].GetXaxis().SetRangeUser(mini,maxi)
c.Modified()
graphs[0].GetYaxis().SetLimits(0,maxY)
#graphs[0].GetXaxis().SetRangeUser(mini,maxi)
graphs[0].GetXaxis().SetLimits(mini,maxi)
c.Modified()
c.Update()

#graphs[3].Print()
#c.Modified()
#c.Update()
if plotMu:
	c.SaveAs(channel[plotAll]+suffix+"Mu.pdf")
	c.SaveAs(channel[plotAll]+suffix+"Mu.png")
else : 
	c.SaveAs(channel[plotAll]+suffix+"Kl.pdf") 
	c.SaveAs(channel[plotAll]+suffix+"Kl.png")

if opt.wait : raw_input()

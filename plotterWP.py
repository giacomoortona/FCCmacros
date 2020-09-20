from ROOT import *
import os,re, optparse

#file notation: syst${syst}_${scen}${photon_wp}${b_wp}${lepton_wp}.root

def parseOptions():

    usage = ('usage: %prog [options] datasetList\n'+ '%prog -h for help')
    parser = optparse.OptionParser(usage)
    parser.add_option('-b', '--bwp', dest='bwp', type='string', default="M", help='b working point')
    parser.add_option('-l', '--lwp', dest='lwp', type='string', default="M", help='lepton working point')
    parser.add_option('-p', '--pwp', dest='pwp', type='string', default="M", help='photon working point')
    parser.add_option('-s', '--scenario', dest='scenario', type='string', default="II", help='scenario')
    parser.add_option('-x', '--syst', dest='systematic', type='string', default="2", help='systematic set')
    parser.add_option('-a', '--setup', dest='setup', type=int, default=1, help='predefined scenario')


    global opt, args
    (opt, args) = parser.parse_args()

def plotSetupbbaa(fileList, titles) :
	#sc = "II"
	#bwp = "M"
	#pwp = "M"
	#lwp = "M"
	#stringstart = "higgsCombine1.00_comb_2_" #IIITTM
	stringstart = "higgsCombine1.00_bbaa_btag_2_" #IIITTM
	stringend = ".MultiDimFit.mH120.root"
	scenlist = ["I", "II","III"]
	for i in scenlist :
		fileList.append(stringstart+i+"MM"+stringend)
		titles.append("Combined, scen. "+i+", M WP")
	print fileList
	print titles
	#titles = [,"Combined, scen. II, M WP","Combined, scen. III, M WP"]

def plotSetupOne(fileList, titles) :
	#sc = "II"
	#bwp = "M"
	#pwp = "M"
	#lwp = "M"
	stringstart = "higgsCombine1.00_comb_2_" #IIITTM
	stringend = ".MultiDimFit.mH120.root"
	scenlist = ["I", "II","III"]
	for i in scenlist :
		fileList.append(stringstart+i+"MMM"+stringend)
		titles.append("Combined, scen. "+i+", M WP")
	print fileList
	print titles
	#titles = [,"Combined, scen. II, M WP","Combined, scen. III, M WP"]


parseOptions()
global opt, args

#colors =   [kBlue,kRed+1,kPink,kGreen-2,kBlack,kBlack,kYellow+2,kCyan]
#titles = ["bbgg1","bbtt1","c3","c2","c1"]


#fileErrList = ["higgsCombinebbcomb_scankl_syst3_bkTimes1.MultiDimFit.mH120.root","higgsCombineTest0.MultiDimFit.mH120.root","higgsCombineTest2.MultiDimFit.mH120.root","higgsCombinebbcomb_scankl_syst1noSyst_bkTimes1.MultiDimFit.mH120.root","higgsCombinebbcomb_scankl_syst1noSyst_bkTimes1.MultiDimFit.mH120.root"]
#fileErrListLow = ["higgsCombinebbcomb_scankl_syst3_bkTimes1.MultiDimFit.mH120.root","higgsCombineTest0.MultiDimFit.mH120.root","higgsCombineTest2.MultiDimFit.mH120.root","higgsCombinebbcomb_scankl_syst1noSyst_bkTimes1.MultiDimFit.mH120.root","higgsCombinebbcomb_scankl_syst1noSyst_bkTimes1.MultiDimFit.mH120.root"]
#fileList = ["higgsCombinebbtt_scankl_all_sel0_syst1Syst_bkTimes1_forComb.MultiDimFit.mH120.root","higgsCombinebbaa_1_nosyst.MultiDimFit.mH120.root","higgsCombinebbaa_1.MultiDimFit.mH120.root"]
colors =   [kBlue,kRed+1,kGreen,kBlack,kBlack,kYellow+2,kCyan]
fileList = []
titles = []
graphs = []
grapherrs = []
grapherrslow = []
if opt.setup == 1 : plotSetupOne(fileList,titles)
elif opt.setup == 2 : plotSetupbbaa(fileList,titles)
else : print "OTHER SCENARIOS not defined yet"

print fileList
print titles

for ifile in range(len(fileList)):
	graphs.append(TGraph())
	inF = TFile.Open(fileList[ifile],"READ")
	tree = inF.Get("limit")

	#ipoint = 0
	for entry in tree :
		graphs[ifile].SetPoint(graphs[ifile].GetN(),entry.kl,2.0*entry.deltaNLL)
			

c=TCanvas()#"","",600,600)
c.SetTicks(1,1)
c.SetLeftMargin(0.14)
c.SetRightMargin(0.08)
c.cd()
gStyle.SetOptTitle(0)

print graphs
print colors
graphs[0].SetLineColor(colors[0])
graphs[0].SetLineWidth(3)
#graphs[3].SetLineStyle(3)
graphs[0].Sort()
graphs[0].SetTitle(titles[0])
graphs[0].SetFillColor(colors[0])
graphs[0].SetFillStyle(3001)
graphs[0].SetMarkerColor(colors[0])
graphs[0].SetMarkerStyle(0)
#graphs[0].SetFillStyle(0)
#graphs[0].SetFillColor(0)


mini = 0.8 #graphs[3].GetXaxis().GetXmin()
maxi = 1.2 #graphs[3].GetXaxis().GetXmax()
maxY = 6
#if plotMu :
#	mini = 0.9
#	maxi = 1.1

y168 = 0.135
y195 = 0.34
#if plotAll == 4: y168 = 0.15
#if plotAll == 0 or plotAll ==1 or plotAll == 6 or plotAll == 2 or plotAll == 5:
#	y168 = 0.22
#	y195 = 0.595
#	#if plotMu:
#	if not plotMu : 
#		mini =0.7
#		maxi = 1.3
#		if plotAll == 1 : y168 = 0.5



graphs[0].Draw("AL3")
graphs[0].GetXaxis().SetTitle("k_{#lambda}")
#if plotMu : graphs[0].GetXaxis().SetTitle("#mu=#sigma/#sigma_{obs}")
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

#if plotAll >= 0 : graphs[3].SetLineStyle(2)

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
	if ig == len(fileList) : #or plotAll >= 0 :
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
#if not ( not plotMu and plotAll == 1): 
linetwo.Draw("SAME")

leg = TLegend(0.4,0.8,0.63,0.63)
leg.SetLineColor(0)
leg.SetLineStyle(0)
leg.SetLineWidth(0)
leg.SetFillStyle(0)
leg.SetShadowColor(10)
leg.SetTextSize(0.030)
leg.SetTextFont(42)
 
for i in range(len(graphs)) :
	leg.AddEntry(graphs[len(graphs)-1-i])
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
#if not ( not plotMu and plotAll == 1): 
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


raw_input()

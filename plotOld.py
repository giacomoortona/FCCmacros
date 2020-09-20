from ROOT import *
import optparse

#define function for parsing options
def parseOptions():

    usage = ('usage: %prog [options] datasetList\n'+ '%prog -h for help')
    parser = optparse.OptionParser(usage)
    parser.add_option('-v', '--var', dest='var', type='string', default="kl", help='variable (kl, r)')
    parser.add_option('-w', '--which', dest='what', type='int', default=3, help='which plot 1D/2D and vars')
    parser.add_option('-s', '--stop', dest='stop', type='int', default=1, help='stop to see the plot')
    parser.add_option('-n', '--nuis', dest='nuis', type='int', default=1, help='use nuisances')
    parser.add_option('-p', '--suffixoptions', dest='options', type='string', default="_", help='options used to run (p,k)')
    global opt, args
    (opt, args) = parser.parse_args()

parseOptions()
global opt, args
if "kl" in opt.var : variable = "kl"
else : variable="r"
#0 = 1D(maa)
#1 = 1D(mhh)
#2 = 2D(aa,bb)
#3 = 2D(aa,hh)
whichplot = opt.what 

#folders = [
#	"w_cards_v6_morphed1D_maa",
#	"w_cards_v6_morphed1D_mhh",
#	"w_cards_v6_morphed2D_aabb",
#	"w_cards_v6_morphed2D_aahh",
#	"w_cards_v6_morphed1D_mhh_boosted"
#]
varNames = [
	"haa_m",
	"hh_m",
	"hmaa_mbb",
	"hmaa_mhh",
	"boosted"
]

folders = [
	".",
	".",
	".",
	".",
	"."
]

#folders = [
#	folder1Dmaa,
#	folder1Dmhh,
#	folder2Dhaabb,
#	folder2Dhaahh
#]

titles = ["1dscan_maa","1dscan_mhh","2dscan_maa_mbb","2dscan_maa_mhh","1dscan_mhh_boosted"]
inf =  TFile.Open(folders[whichplot]+"/higgsCombinescan"+variable+"_"+varNames[whichplot]+opt.options+".MultiDimFit.mH120.root")
tree = inf.Get("limit")
infS =  TFile.Open(folders[whichplot]+"/higgsCombinescan"+variable+"_syst_"+varNames[whichplot]+opt.options+".MultiDimFit.mH120.root")
infSS =  TFile.Open(folders[whichplot]+"/higgsCombinescan"+variable+"_systSig_"+varNames[whichplot]+opt.options+".MultiDimFit.mH120.root")
infB2 =  TFile.Open(folders[whichplot]+"/higgsCombinescan"+variable+"_2bkg_"+varNames[whichplot]+opt.options+".MultiDimFit.mH120.root")
infB05 =  TFile.Open(folders[whichplot]+"/higgsCombinescan"+variable+"_05bkg_"+varNames[whichplot]+opt.options+".MultiDimFit.mH120.root")

if opt.nuis > 0 :
	treeSyst = infS.Get("limit")
	treeSystS = infSS.Get("limit")
	trees = [tree,treeSyst,treeSystS]
	if opt.nuis > 5 :
		trees.append(infB2.Get("limit"))
		trees.append(infB05.Get("limit"))
else : trees = [tree]

graphs = []
for i in range(len(trees)) : graphs.append(TGraph(0))
graphs[0].SetLineColor(kBlue)
graphs[0].SetName("Stat. only")
for i in range(len(trees)) : graphs[i].SetFillStyle(0)

for i in range(len(trees)) : 
	ipoint =0
	for event in trees[i] :
		if variable == "kl" :
			if whichplot is not 4 and ( event.kl<0.9 or event.kl>1.1 ): continue
			if whichplot == 4 :
				if event.kl<0.95 and event.kl>0.9 : continue
				if event.kl<1.15 and event.kl>1.02 : continue
			graphs[i].SetPoint(ipoint,event.kl, 2*event.deltaNLL)
		else :
			if event.r<0.9 or event.r>1.1 : continue
			graphs[i].SetPoint(ipoint,event.r, 2*event.deltaNLL)
		ipoint+=1
	graphs[i].Sort()
	graphs[i].SetTitle("")
	if variable == "r" : graphs[i].GetXaxis().SetTitle("r = #sigma_{obs}/#sigma_{SM}")
	else : graphs[i].GetXaxis().SetTitle("k_{#lambda} = #lambda_{obs}/#lambda_{SM}")
	graphs[i].GetYaxis().SetTitle("-2#Delta NLL")
	graphs[i].SetLineWidth(3)

c = TCanvas("c","c")

if opt.nuis > 0 and opt.nuis < 5 and whichplot < 4 :
	graphs[1].SetLineColor(kRed+2)
	graphs[2].SetLineColor(kGreen+3)
	graphs[1].SetName("#delta S/S = 1%")
	graphs[2].SetName("#delta S/S = #delta ttH/ttH = 1%")
	graphs[1].Draw("AL")
	graphs[2].Draw("LSAME")
elif opt.nuis > 5 :
	graphs[3].SetLineColor(kRed+2)
	graphs[3].SetName("All bkg x 2")
	graphs[4].SetLineColor(kGreen+2)
	#graphs[4].SetLineStyle(3)
	graphs[4].SetName("All bkg x 0.5")
	graphs[4].Draw("AL")
	graphs[3].Draw("LSAME")
graphs[0].Draw("LSAME")
leg = c.BuildLegend()
leg.SetLineColor(0)
leg.SetFillColor(0)

xmin = 0.9
xmax = 1.1
if whichplot == 4 and variable == "kl":
	xmin = 0.5
	xmax = 1.5
line = TLine(xmin,1,xmax,1)
line.SetLineColor(kBlack)
line.SetLineStyle(3)
line.SetLineWidth(3)
line.Draw("SAME")

appString = "_v6_"
if whichplot == 4 : appString = "_v6_sel_10_"
if opt.nuis > 5 :
	appString += "2bkg_"

c.SaveAs(titles[whichplot]+appString+variable+opt.options+".pdf")
c.SaveAs(titles[whichplot]+appString+variable+opt.options+".root")

if opt.stop > 0 :raw_input()

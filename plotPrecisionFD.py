from ROOT import *
import os,re, optparse

fileLoader = ["/eos/user/g/gortona/FCC/Results_v49/higgsCombinelumiScan_III_lumiXXX_forPrec.FitDiagnostics.mH120.root",
"/eos/user/g/gortona/FCC/Results_v49/higgsCombinelumiScan_II_lumiXXX_forPrec.FitDiagnostics.mH120.root",
"/eos/user/g/gortona/FCC/Results_v49/higgsCombinelumiScan_I_lumiXXX_forPrec.FitDiagnostics.mH120.root",
"/eos/user/g/gortona/FCC/Results_v49/higgsCombinelumiScan_I_lumiXXX_noSyst_forPrec.FitDiagnostics.mH120.root"]

lumis = [0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
graphs = [TGraph(),TGraph(),TGraph(),TGraph()]
colors = [kBlue,kRed+1,kGreen+1,kBlack]
titles = ["Combined - scenario III ","Combined - scenario II ","Combined - scenario I","Combined - no syst. unc."]
for ig in range(len(graphs)):
	graphs[ig].SetLineColor(colors[ig])
	graphs[ig].SetFillColor(0)
	graphs[ig].SetTitle(titles[ig])
	graphs[ig].SetName(titles[ig])
	graphs[ig].SetLineWidth(3)

graphs[3].SetLineStyle(2)
for l in lumis :
	print l 
	for ifile in range(len(fileLoader)):
		fname = fileLoader[ifile].replace("XXX","{0}".format(l))
		#print fname
		infile = TFile.Open(fname)
		tree = infile.Get("limit")
		low = -1
		high = -1
		center = -1
		obs = -1
		for entry in tree :
			if entry.quantileExpected < 0 : obs = entry.limit
			elif entry.quantileExpected < 0.17 : low = entry.limit
			elif entry.quantileExpected < 0.7 : center = entry.limit
			else : high = entry.limit
		#if high >= 1.3 :
		#	if low <=0.7 :graphs[ifile].SetPoint(graphs[ig].GetN(),l*30.,(obs)*100.0)
		#	else : graphs[ifile].SetPoint(graphs[ig].GetN(),l*30.,(center-low)*100.0)
		#else : 
		graphs[ifile].SetPoint(graphs[ig].GetN(),l*30.,(high-center)*100.0)

c = TCanvas()
c.SetTicks(1,1)
c.SetLeftMargin(0.14)
c.SetRightMargin(0.08)
c.cd()
gStyle.SetOptTitle(0)

graphs[0].Draw("AL")
graphs[0].GetXaxis().SetTitle("Collected luminosity (ab^{-1})")
graphs[0].GetYaxis().SetTitle("#delta k_{#lambda}/k_{#lambda}, #mu=1")

graphs[1].Draw("LSAME")
graphs[2].Draw("LSAME")
graphs[3].Draw("LSAME")


leg = c.BuildLegend()
leg.SetHeader("Assuming SM couplings.")
leg.SetLineColor(0)
leg.SetLineStyle(0)
leg.SetLineWidth(0)
leg.SetFillStyle(0)
leg.SetShadowColor(10)
leg.SetTextSize(0.030)
leg.SetTextFont(42)
leg.SetX1(0.52)
leg.SetX2(0.75)
leg.SetY1(0.63)
leg.SetY2(0.88)
leg.SetFillColor(0)

Text = TPaveText(0.73, 0.88,0.93,0.95,'brNDC')
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

Text2 = TPaveText(0.35, 0.71,0.5,0.85,'brNDC')
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
graphs[0].GetXaxis().SetRangeUser(0.008*30,1.1*30)
graphs[0].GetYaxis().SetRangeUser(0,50)
c.Modified()
graphs[0].GetXaxis().SetLimits(0.008*30,1.1*30)
graphs[0].GetYaxis().SetLimits(0,50)
c.Modified()
c.Update()

c.SetLogx()
c.Modified()
c.Update()

c.SaveAs("precisionVSlumi.pdf")
c.SaveAs("precisionVSlumi.png")
#raw_input()
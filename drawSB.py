from ROOT import *

nscen = 1 #

fileI = TFile.Open("/eos/user/s/selvaggi/Analysis/hh_comb/hhbbbb_v58/hhbbbb_I_M/sel_HH_kappa_lambda_1.00/root_HH_kappa_lambda_1.00/shapes.root")
fileII = TFile.Open("/eos/user/s/selvaggi/Analysis/hh_comb/hhbbbb_v58/hhbbbb_II_M/sel_HH_kappa_lambda_1.00/root_HH_kappa_lambda_1.00/shapes.root")
fileIII = TFile.Open("/eos/user/s/selvaggi/Analysis/hh_comb/hhbbbb_v58/hhbbbb_III_M/sel_HH_kappa_lambda_1.00/root_HH_kappa_lambda_1.00/shapes.root")

files = [fileI, fileII, fileIII]
hSigs = [fileI.Get("HH_sel0_tmva_bdt_I_M"),fileII.Get("HH_sel0_tmva_bdt_II_M"),fileIII.Get("HH_sel0_tmva_bdt_III_M")]
httba = [fileI.Get("ttbar_sel0_tmva_bdt_I_M"),fileII.Get("ttbar_sel0_tmva_bdt_II_M"),fileIII.Get("ttbar_sel0_tmva_bdt_III_M")]
hqcd  = [fileI.Get("QCD_sel0_tmva_bdt_I_M"),fileII.Get("QCD_sel0_tmva_bdt_II_M"),fileIII.Get("QCD_sel0_tmva_bdt_III_M")]
hsing = [fileI.Get("singleH_sel0_tmva_bdt_I_M"),fileII.Get("singleH_sel0_tmva_bdt_II_M"),fileIII.Get("singleH_sel0_tmva_bdt_III_M")]
hzz   = [fileI.Get("ZZ_sel0_tmva_bdt_I_M"),fileII.Get("ZZ_sel0_tmva_bdt_II_M"),fileIII.Get("ZZ_sel0_tmva_bdt_III_M")]
hzbb  = [fileI.Get("Zbb_sel0_tmva_bdt_I_M"),fileII.Get("Zbb_sel0_tmva_bdt_II_M"),fileIII.Get("Zbb_sel0_tmva_bdt_III_M")]


hBkg = []
for i in range(nscen) : #
	for xbin in range(1,hqcd[i].GetNbinsX()+1) :
			if hqcd[i].GetBinContent(xbin)<=0 : 
				print "empty bin, scenario",i,"bin",xbin,"filling with",hqcd[i].GetBinContent(xbin-1)
				hqcd[i].SetBinContent(xbin,hqcd[i].GetBinContent(xbin-1)) #1.7*30000000)
				
	htmps = httba[i]+hqcd[i]+hsing[i]+hzz[i]+hzbb[i]
	hBkg.append(htmps)


c = TCanvas("c","c")
c.Divide(1,nscen)
for i in range(nscen) :
	c.cd(1+i)
	hBkg[i].Draw()
	hSigs[i].Scale(100)
	hSigs[i].SetLineColor(kRed+1)
	hSigs[i].SetMarkerColor(kRed+1)
	hSigs[i].Draw("SAME")
	c.cd(1+i).SetLogy()
	hSigs[i].GetYaxis().SetRangeUser(0.1,1000)
	print "SCENARIO ",i
	for xbin in range(16,hSigs[i].GetNbinsX()+1):
		print xbin,hSigs[i].GetXaxis().GetBinCenter(xbin),") Sx100:",hSigs[i].GetBinContent(xbin),"B:",hBkg[i].GetBinContent(xbin),"=>",hSigs[i].GetBinContent(xbin)/hBkg[i].GetBinContent(xbin),"Zbb)=",hzbb[i].GetBinContent(xbin),"ttbar)=",httba[i].GetBinContent(xbin),"zbb/ttbar=",hzbb[i].GetBinContent(xbin)/httba[i].GetBinContent(xbin)
c.Modified()
c.Update()
raw_input()
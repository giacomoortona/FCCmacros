from ROOT import *
import os,re, optparse


files = ["FCCworkshop3/hhbbaa_II_MM/sel_HH_kappa_lambda_1.00/root_HH_kappa_lambda_1.00/shapes.root","FCCworkshop3/hhbbaa_II_MM_beffUp/sel_HH_kappa_lambda_1.00/root_HH_kappa_lambda_1.00/shapes.root","FCCworkshop3/hhbbaa_II_MM_beffDown/sel_HH_kappa_lambda_1.00/root_HH_kappa_lambda_1.00/shapes.root"]

fN = TFile.Open(files[0])
fU = TFile.Open(files[1])
fD = TFile.Open(files[2])

print "open files"

print "jgjj"
a =  fN.Get("jgjj_sel0_bdth_bdtqcd_100_II_MM").Integral()
b =  fU.Get("jgjj_sel0_bdth_bdtqcd_100_II_MM").Integral()
c =  fD.Get("jgjj_sel0_bdth_bdtqcd_100_II_MM").Integral()
print b/a , "/",  c/a
print "ggjj"
a =  fN.Get("ggjj_sel0_bdth_bdtqcd_100_II_MM").Integral()
b =  fU.Get("ggjj_sel0_bdth_bdtqcd_100_II_MM").Integral()
c =  fD.Get("ggjj_sel0_bdth_bdtqcd_100_II_MM").Integral()
print b/a , "/",  c/a
print "singleH"
a =  fN.Get("singleH_sel0_bdth_bdtqcd_100_II_MM").Integral()
b =  fU.Get("singleH_sel0_bdth_bdtqcd_100_II_MM").Integral()
c =  fD.Get("singleH_sel0_bdth_bdtqcd_100_II_MM").Integral()
print b/a , "/",  c/a
print "HH"
a =  fN.Get("HH_sel0_bdth_bdtqcd_100_II_MM").Integral()
b =  fU.Get("HH_sel0_bdth_bdtqcd_100_II_MM").Integral()
c =  fD.Get("HH_sel0_bdth_bdtqcd_100_II_MM").Integral()
print b/a , "/",  c/a

hN =  fN.Get("HH_sel0_bdth_bdtqcd_100_II_MM")
hU =  fU.Get("HH_sel0_bdth_bdtqcd_100_II_MM")
hD =  fD.Get("HH_sel0_bdth_bdtqcd_100_II_MM")

print "integrals",hN.Integral(),hU.Integral(),hD.Integral()
print "loaded h2"

hxN = hN.ProjectionX("xU")
hxU = hU.ProjectionX("xN")
hxD = hD.ProjectionX("xD")

hyN = hN.ProjectionY("yU")
hyU = hU.ProjectionY("yN")
hyD = hD.ProjectionY("yD")

print "done projections"

hxU.SetLineColor(kRed)
hyU.SetLineColor(kRed)
hxD.SetLineColor(kGreen+2)
hyD.SetLineColor(kGreen+2)

cx = TCanvas("cx")
hxU.Draw()
hxN.Draw("SAME")
hxD.Draw("SAME")

cy = TCanvas("cy")
hyU.Draw()
hyN.Draw("SAME")
hyD.Draw("SAME")

raw_input()
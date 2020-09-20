from ROOT import *
from outRatesbbaa import getRatebbaa
from outRatesbbbb import getRatebbbb
from outRatesbbtahtah import getRatebbtahtah
from outRatesbbtahtal import getRatebbtahtal

xvar = RooRealVar("x","x",-1.,2.0)
plot = xvar.frame()
for bwp in ["L","M","T"] :
	for pwp in [""] :
		for scenario in ["I","II","III"] :
			formula = RooFormulaVar("HHnorm"+bwp+pwp,getRatebbbb(scenario,bwp,pwp),RooArgList(xvar))
			formula.plotOn(plot)

plot.Draw()
raw_input()
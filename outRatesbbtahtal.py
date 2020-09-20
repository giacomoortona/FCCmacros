def getRatebbtahtal(scenario,bwp,pwp):
    outString = "CIAO"
    if scenario is "I" and bwp is "M" and pwp is "M":
        outString = "0.15420*@0*@0 + (-0.51752-2.0*0.15420)*@0 +0.15420 + 1.0 - -0.51752"
    if scenario is "I" and bwp is "M" and pwp is "T":
        outString = "0.15631*@0*@0 + (-0.52150-2.0*0.15631)*@0 +0.15631 + 1.0 - -0.52150"
    if scenario is "I" and bwp is "T" and pwp is "M":
        outString = "0.15422*@0*@0 + (-0.50727-2.0*0.15422)*@0 +0.15422 + 1.0 - -0.50727"
    if scenario is "I" and bwp is "T" and pwp is "T":
        outString = "0.15318*@0*@0 + (-0.50075-2.0*0.15318)*@0 +0.15318 + 1.0 - -0.50075"
    if scenario is "II" and bwp is "M" and pwp is "M":
        outString = "0.15324*@0*@0 + (-0.50277-2.0*0.15324)*@0 +0.15324 + 1.0 - -0.50277"
    if scenario is "II" and bwp is "M" and pwp is "T":
        outString = "0.15341*@0*@0 + (-0.50487-2.0*0.15341)*@0 +0.15341 + 1.0 - -0.50487"
    if scenario is "II" and bwp is "T" and pwp is "M":
        outString = "0.15282*@0*@0 + (-0.49996-2.0*0.15282)*@0 +0.15282 + 1.0 - -0.49996"
    if scenario is "II" and bwp is "T" and pwp is "T":
        outString = "0.15244*@0*@0 + (-0.49665-2.0*0.15244)*@0 +0.15244 + 1.0 - -0.49665"
    if scenario is "III" and bwp is "M" and pwp is "M":
        outString = "0.15251*@0*@0 + (-0.49699-2.0*0.15251)*@0 +0.15251 + 1.0 - -0.49699"
    if scenario is "III" and bwp is "M" and pwp is "T":
        outString = "0.15257*@0*@0 + (-0.49780-2.0*0.15257)*@0 +0.15257 + 1.0 - -0.49780"
    if scenario is "III" and bwp is "T" and pwp is "M":
        outString = "0.15202*@0*@0 + (-0.49355-2.0*0.15202)*@0 +0.15202 + 1.0 - -0.49355"
    if scenario is "III" and bwp is "T" and pwp is "T":
        outString = "0.15172*@0*@0 + (-0.49055-2.0*0.15172)*@0 +0.15172 + 1.0 - -0.49055"
    return outString
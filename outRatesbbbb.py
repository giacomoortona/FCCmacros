def getRatebbbb(scenario,bwp,pwp):
    outString = "CIAO"
    if scenario is "I" and bwp is "M" and pwp is "":
        outString = "0.16032*@0*@0 + (-0.47016-2.0*0.16032)*@0 +0.16032 + 1.0 - -0.47016"
    if scenario is "I" and bwp is "T" and pwp is "":
        outString = "0.15587*@0*@0 + (-0.45584-2.0*0.15587)*@0 +0.15587 + 1.0 - -0.45584"
    if scenario is "II" and bwp is "M" and pwp is "":
        outString = "0.15703*@0*@0 + (-0.45794-2.0*0.15703)*@0 +0.15703 + 1.0 - -0.45794"
    if scenario is "II" and bwp is "T" and pwp is "":
        outString = "0.15522*@0*@0 + (-0.45154-2.0*0.15522)*@0 +0.15522 + 1.0 - -0.45154"
    if scenario is "III" and bwp is "M" and pwp is "":
        outString = "0.15608*@0*@0 + (-0.45170-2.0*0.15608)*@0 +0.15608 + 1.0 - -0.45170"
    if scenario is "III" and bwp is "T" and pwp is "":
        outString = "0.15511*@0*@0 + (-0.44633-2.0*0.15511)*@0 +0.15511 + 1.0 - -0.44633"
    return outString
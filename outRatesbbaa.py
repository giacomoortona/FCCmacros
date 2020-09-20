def getRatebbaa(scenario,bwp,pwp):
    outString = "CIAO"
    if scenario is "I" and bwp is "M" and pwp is "M":
        outString = "0.21822*@0*@0 + (-0.75169-2.0*0.21822)*@0 +0.21822 + 1.0 - -0.75169"
    if scenario is "I" and bwp is "M" and pwp is "T":
        outString = "0.21728*@0*@0 + (-0.75088-2.0*0.21728)*@0 +0.21728 + 1.0 - -0.75088"
    if scenario is "I" and bwp is "T" and pwp is "M":
        outString = "0.21906*@0*@0 + (-0.75420-2.0*0.21906)*@0 +0.21906 + 1.0 - -0.75420"
    if scenario is "I" and bwp is "T" and pwp is "T":
        outString = "0.21916*@0*@0 + (-0.75517-2.0*0.21916)*@0 +0.21916 + 1.0 - -0.75517"
    if scenario is "II" and bwp is "M" and pwp is "M":
        outString = "0.21775*@0*@0 + (-0.75290-2.0*0.21775)*@0 +0.21775 + 1.0 - -0.75290"
    if scenario is "II" and bwp is "M" and pwp is "T":
        outString = "0.21687*@0*@0 + (-0.75146-2.0*0.21687)*@0 +0.21687 + 1.0 - -0.75146"
    if scenario is "II" and bwp is "T" and pwp is "M":
        outString = "0.21672*@0*@0 + (-0.75166-2.0*0.21672)*@0 +0.21672 + 1.0 - -0.75166"
    if scenario is "II" and bwp is "T" and pwp is "T":
        outString = "0.21647*@0*@0 + (-0.75155-2.0*0.21647)*@0 +0.21647 + 1.0 - -0.75155"
    if scenario is "III" and bwp is "M" and pwp is "M":
        outString = "0.21533*@0*@0 + (-0.74970-2.0*0.21533)*@0 +0.21533 + 1.0 - -0.74970"
    if scenario is "III" and bwp is "M" and pwp is "T":
        outString = "0.21469*@0*@0 + (-0.74851-2.0*0.21469)*@0 +0.21469 + 1.0 - -0.74851"
    if scenario is "III" and bwp is "T" and pwp is "M":
        outString = "0.21451*@0*@0 + (-0.74831-2.0*0.21451)*@0 +0.21451 + 1.0 - -0.74831"
    if scenario is "III" and bwp is "T" and pwp is "T":
        outString = "0.21436*@0*@0 + (-0.74814-2.0*0.21436)*@0 +0.21436 + 1.0 - -0.74814"
    return outString
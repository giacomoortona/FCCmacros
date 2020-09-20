def getRatebbtahtah(scenario,bwp,pwp):
    outString = "CIAO"
    if scenario is "I" and bwp is "M" and pwp is "M":
        outString = "0.30975*@0*@0 + (-0.68143-2.0*0.30975)*@0 +0.30975 + 1.0 - -0.68143"
    if scenario is "I" and bwp is "M" and pwp is "T":
        outString = "0.31155*@0*@0 + (-0.69037-2.0*0.31155)*@0 +0.31155 + 1.0 - -0.69037"
    if scenario is "I" and bwp is "T" and pwp is "M":
        outString = "0.30829*@0*@0 + (-0.67571-2.0*0.30829)*@0 +0.30829 + 1.0 - -0.67571"
    if scenario is "I" and bwp is "T" and pwp is "T":
        outString = "0.30714*@0*@0 + (-0.67300-2.0*0.30714)*@0 +0.30714 + 1.0 - -0.67300"
    if scenario is "II" and bwp is "M" and pwp is "M":
        outString = "0.30670*@0*@0 + (-0.67250-2.0*0.30670)*@0 +0.30670 + 1.0 - -0.67250"
    if scenario is "II" and bwp is "M" and pwp is "T":
        outString = "0.30667*@0*@0 + (-0.67494-2.0*0.30667)*@0 +0.30667 + 1.0 - -0.67494"
    if scenario is "II" and bwp is "T" and pwp is "M":
        outString = "0.30407*@0*@0 + (-0.66758-2.0*0.30407)*@0 +0.30407 + 1.0 - -0.66758"
    if scenario is "II" and bwp is "T" and pwp is "T":
        outString = "0.30311*@0*@0 + (-0.66515-2.0*0.30311)*@0 +0.30311 + 1.0 - -0.66515"
    if scenario is "III" and bwp is "M" and pwp is "M":
        outString = "0.30285*@0*@0 + (-0.66460-2.0*0.30285)*@0 +0.30285 + 1.0 - -0.66460"
    if scenario is "III" and bwp is "M" and pwp is "T":
        outString = "0.30260*@0*@0 + (-0.66539-2.0*0.30260)*@0 +0.30260 + 1.0 - -0.66539"
    if scenario is "III" and bwp is "T" and pwp is "M":
        outString = "0.30058*@0*@0 + (-0.65922-2.0*0.30058)*@0 +0.30058 + 1.0 - -0.65922"
    if scenario is "III" and bwp is "T" and pwp is "T":
        outString = "0.29957*@0*@0 + (-0.65639-2.0*0.29957)*@0 +0.29957 + 1.0 - -0.65639"
    return outString
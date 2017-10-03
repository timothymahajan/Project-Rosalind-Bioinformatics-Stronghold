#Problem 11: Calculating Protein Mass
#Given: A protein string PP of length at most 1000 aa.
#Return: The total weight of PP.

def weight(p):
    wgt = 0
    for i in range(0, len(p)):
        if (p[i] == "A"):
            wgt = wgt + 71.03711
        elif (p[i] == "C"):
            wgt = wgt + 103.00919
        elif (p[i] == "D"):
            wgt = wgt + 115.02694
        elif (p[i] == "E"):
            wgt = wgt + 129.04259
        elif (p[i] == "F"):
            wgt = wgt + 147.06841
        elif (p[i] == "G"):
            wgt = wgt + 57.02146
        elif (p[i] == "H"):
            wgt = wgt + 137.05891
        elif (p[i] == "I"):
            wgt = wgt + 113.08406
        elif (p[i] == "K"):
            wgt = wgt + 128.09496
        elif (p[i] == "L"):
            wgt = wgt + 113.08406
        elif (p[i] == "M"):
            wgt = wgt + 131.04049
        elif (p[i] == "N"):
            wgt = wgt + 114.04293
        elif (p[i] == "P"):
            wgt = wgt + 97.05276
        elif (p[i] == "Q"):
            wgt = wgt + 128.05858
        elif (p[i] == "R"):
            wgt = wgt + 156.10111
        elif (p[i] == "S"):
            wgt = wgt + 87.03203
        elif (p[i] == "T"):
            wgt = wgt + 101.04768
        elif (p[i] == "V"):
            wgt = wgt + 99.06841
        elif (p[i] == "W"):
            wgt = wgt + 186.07931
        elif (p[i] == "Y"):
            wgt = wgt + 163.06333
    return wgt

print(weight("SKADYEK"))
#Problem 1: Counting DNA Nucleotides
#Given: A DNA string ss of length at most 1000 nt.
#Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in ss.

def countSymbol (str):
    aCount = 0
    cCount = 0
    gCount = 0
    tCount = 0
    for i in str:
        if (i == 'A'):
            aCount = aCount + 1
        elif (i == 'C'):
            cCount = cCount + 1
        elif (i == 'G'):
            gCount = gCount + 1
        else:
            tCount = tCount + 1
    return [aCount, cCount, gCount, tCount]

print(countSymbol("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"))

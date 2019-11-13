#Problem 1: Counting DNA Nucleotides
#Given: A DNA string ss of length at most 1000 nt.
#Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in ss.


def countSymbol (string):
    return str(string.count("A")) + " " + str(string.count("G")) + " " + str(string.count("C")) + " " + str(string.count("T"))

print(countSymbol("TAGGAGTAGTCCTAGGAGGGACTTCAAGAGGAGTGGTCGGGCGAGCACTCACCGTCGTCTGAAGTTAACCTGA"))

#Problem 43: Matching Random Motifs
#Given: A positive integer N≤100000N≤100000, a number x between 0 and 1, and a DNA string ss of length at most 10 bp.
#Return: The probability that if N random DNA strings having the same length as s are constructed with GC-content x (see “Introduction to Random Strings”), then at least one of the strings equals s. We allow for the same random string to be created more than once.

def probability (n, x, s):
    p = 1
    at = 0
    gc = 0
    for i in s:
        if i == 'A' or i == 'T':
            at = at + 1
        elif i == 'G' or i == 'C':
            gc = gc + 1

    q = ((0.5*x) ** gc) * ((0.5 - 0.5*x) ** at) 
    p = 1 - (1 - q) ** n
    return p


print(probability(80504, 0.534302, 'GGTCCAAG'))
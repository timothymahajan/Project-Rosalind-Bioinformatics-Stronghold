#Problem 26: Perfect Matchings and RNA Secondary Structures
#Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.
#Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.

from math import factorial

seq = 'AUGCCCACCCGACGGUUGGGUUGACUUUGUGAUGCGCCGCACGAAAACCUACGCGGAGUUCCAAUUCGACACGCGGGCGU'

match = factorial(seq.count('U')) * factorial(seq.count('G'))
print(match)

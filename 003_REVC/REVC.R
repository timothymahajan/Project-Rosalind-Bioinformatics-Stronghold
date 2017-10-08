#Problem 3: Complementing a Strand of DNA
#Given: A DNA string s of length at most 1000 bp.
#Return: The reverse complement sc of s.

require(Biostrings)
dna = DNAString("AAAACCCGGT")
comp = as.character(reverseComplement(dna))

#Problem 2: Transcribing DNA into RNA
#Given: A DNA string t having length at most 1000 nt.
#Return: The transcribed RNA string of t.
require(Biostrings)
dna = DNAString("GATGGAACTTGACTACGTAAATT")
rna = RNAString(dna)

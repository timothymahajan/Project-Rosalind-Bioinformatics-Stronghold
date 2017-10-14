#Problem 36: k-Mer Composition
#Given: A DNA string s in FASTA format (having length at most 100 kbp).
#Return: The 4-mer composition of s.

from itertools import product

f = open("Example36.txt", "r")
mat = []
str1 = f.read()
str1 = str1.replace("Rosalind_", "")
str1 = str1.replace("\n", "")
str1 = ''.join([i for i in str1 if not i.isdigit()])
mat = str1.split(">")
mat.remove("")

lst =  [''.join(kmer) for kmer in list(product('ACGT', repeat = 4))]
count = [0]*(256)

for i in range(0, len(mat[0])-3):
	count[lst.index(mat[0][i:i+4])] = count[lst.index(mat[0][i:i+4])] + 1

f = open('KMER.txt', 'w')
f.write(' '.join(map(str,count)))
f.close()

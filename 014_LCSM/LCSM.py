#Problem 14: Finding a Shared Motif
#Given: A collection of kk (k≤100k≤100) DNA strings of length at most 1 kbp each in FASTA format.
#Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

f = open("FindingASharedMotifExample.txt", "r")
mat = []
str1 = f.read()
str1 = str1.replace("Rosalind_", "")
str1 = str1.replace("\n", "")
str1 = ''.join([i for i in str1 if not i.isdigit()])
mat = str1.split(">")
mat.remove("")

min = mat[0]
for i in mat:
    if len(i) < len(min):
        min = i

submat = []
for i in range (0, len(min)):
    for j in range (i, len(min)+1):
        submat.append(min[i:j])
submat.remove('')

works = []
for i in submat:
    sub = [x for x in mat if i in x]
    if (sub == mat):
        works.append(i)
print(works)

max = works[0]
for i in works:
    if len(i) >= len(max):
        max = i

print(max)


#Result: GACAATAGGAGGGCATTTGTATTAATGAAGCCCAACGCGGCCAGTATCTAAGATTTTACGAGCGGGTTCTATGTATGCATGTATCACTCTACAAACTGCCAATGGGTCCACTTAATGTAATCGCGAACCCTTCTAGCAGACGCTGCAGCTTGTAGCGCTGCGAGTATCTCCCTAACACTTCAGATTGCCCAGTTTGGAACTACCGT

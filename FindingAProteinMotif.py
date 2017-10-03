#Problem 16: Finding A Protein Motif
#Given: At most 15 UniProt Protein Database access IDs.
#Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.

import fnmatch

f = open("FindingAProteinMotifExample.txt", "r")
mat = []
str1 = " "
while (str1 != ''):
    str1 = f.readline().strip()
    mat.append(str1)
for i in range(0, len(mat)-1):
    if (mat[i][0] == ">"):
        mat[i+1] = "*{0}".format(mat[i+1])

filtered = fnmatch.filter(mat, '>*')
filt = [x for x in mat if x not in filtered]
a = ""
lst = a.join(filt)
lst = lst.split("*")
lst.remove("")

g = open("FindingAProteinMotifExample2.txt", "r")
mat2 = []
str2 = " "
while (str2 != ''):
    str2 = g.readline().strip()
    mat2.append(str2)
mat2.remove("")

mat3 = []
for i in range(0, len(lst)):
    mat3.append(mat2[i])
    for j in range(0, len(lst[i])-3):
        if (lst[i][j] == "N" and lst[i][j+1] != "P" and (lst[i][j+2] == "S" or lst[i][j+2] == "T") and lst[i][j+3] != "P"):
            mat3.append(j+1)

for i in range(0, len(mat3)):
    if (mat3[i] in mat2):
        print("\n")
        print(mat3[i])
    else:
        print(mat3[i], end = ' ')

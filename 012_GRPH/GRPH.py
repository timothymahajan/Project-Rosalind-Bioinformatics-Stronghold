#Problem 12: Overlap Graphs
#Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
#Return: The adjacency list corresponding to O. You may return edges in any order.

f = open("OverlapGraphsExample.txt", "r")
mat = []
str1 = f.read()
str1 = str1.replace("Rosalind_", "")
str1 = str1.replace("\n", "")
str1 = ''.join([i for i in str1 if not i.isdigit()])
mat = str1.split(">")
mat.remove("")

f = open("OverlapGraphsExample.txt", "r")
matx = []
str2 = " "
while (str2 != ''):
    str2 = f.readline().strip()
    matx.append(str2)
matx.remove("")

mati = []
for i in range(0, len(matx)):
    if (matx[i][0] == ">"):
        mati.append(matx[i])

maty = []
for i in mati:
    maty.append(i[1:])

q = []
mat1 = []
temp = []
counter = 0
for i in range(0, len(mat)):
    p = []
    p = mat[:i] + mat[i+1:]
    for j in range(0, len(p)):
        if (mat[i][0] == p[j][-1]):
            temp = [mat[i], p[j]]
            mat1.append(temp)

matz = []
for i in mat1:
    for j in range(0,2):
        a = mat.index(i[j])
        matz.append(maty[a])

a = list(zip(*(iter(matz),)*2))

c = []
for i in a:
    c.append(i[::-1])

for i in c:
    print(i[0], i[1])

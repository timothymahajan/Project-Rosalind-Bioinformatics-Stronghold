#Problem 47: Expected Number of Restriction Sites
#Given: A positive integer n (n≤1,000,000), a DNA string s of even length at most 10, and an array A of length at most 20, containing numbers between 0 and 1.
#Return: An array having the same length as A in which B[i] represents the expected number of times that s will appear as a substring of a random DNA string t of length n, where t is formed with GC-content A[i] (see “Introduction to Random Strings”).

mat = []
f = open('Example47.txt', 'r')
str1 = ' '
while (str1 != ''):
    str1 = f.readline().strip()
    mat.append(str1)

n = int(mat[0])
s = mat[1]
a = [float(i) for i in mat[2].split()]

at = 0
gc = 0
for i in s:
    if i == 'A' or i == 'T':
        at = at + 1
    elif i == 'G' or i == 'C':
        gc = gc + 1

mat1 = []

for i, j in enumerate(a):
    prob = ((0.5 * j) ** gc) * (n - len(s) + 1) * ((0.5 - 0.5 * j) ** at)
    mat1.append(prob)

f = open('EVAL.txt', 'w')
for i in mat1:
    f.write(str(i))
    f.write('\n')
f.close()
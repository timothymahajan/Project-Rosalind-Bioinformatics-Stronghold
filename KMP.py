#Problem 37: Speeding Up Motif Finding
#Given: A DNA string s (of length at most 100 kbp) in FASTA format.
#Return: The failure array of s.

f = open("Example37.txt", "r")
mat = []
str1 = f.read()
str1 = str1.replace("Rosalind_", "")
str1 = str1.replace("\n", "")
str1 = ''.join([i for i in str1 if not i.isdigit()])
mat = str1.split(">")
mat.remove("")

seq = mat[0]

P = [0] * len(seq)
j = 0

for i in range(2, len(seq)):
    while (j > 0 and seq[j] != seq[i-1]):
        j = P[j-1]
    if (seq[j] == seq[i-1]):
        j = j + 1
    P[i-1] = j


f = open('KMPa.txt', 'w')
f.write((' '.join(map(str, P))))
f.close()
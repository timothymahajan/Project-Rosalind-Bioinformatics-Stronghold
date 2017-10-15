#Problem 40: Maximum Matchings and RNA Secondary Structures
#Given: An RNA string s of length at most 100.
#Return: The total possible number of maximum matchings of basepair edges in the bonding graph of s.

f = open("Example40.txt", "r")
mat = []
str1 = f.read()
str1 = str1.replace("Rosalind_", "")
str1 = str1.replace("\n", "")
str1 = ''.join([i for i in str1 if not i.isdigit()])
mat = str1.split(">")
mat.remove("")

bases = ['A', 'U', 'G', 'C']
cnt = [mat[0].count(i) for i in bases]
minAu = min(cnt[:2])
maxAu = max(cnt[:2])
minGc = min(cnt[2:])
maxGc = max(cnt[2:])

def f(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*f(n-1)

a = f(maxAu) // (f(maxAu - minAu))
b = f(maxGc) // (f(maxGc - minGc))

print (a * b)
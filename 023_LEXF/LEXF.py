#Problem 23: Enumerating k-mers Lexicographically
#Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10n≤10).
#Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).

import itertools

f = open("LEXF_Example.txt", "r")
str1 = ' '
mat = []
while (str1 != ''):
    str1 = f.readline().strip()
    mat.append(str1)
mat.remove("")

a = mat[0]
b = int(mat[1])

c = list(map(str, a.split())) 
x = list(itertools.product(c, repeat = b))


print(*[''.join(i) for i in x], sep='\n')

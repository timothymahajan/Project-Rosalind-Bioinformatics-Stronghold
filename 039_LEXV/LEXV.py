#Problem 39: Ordering Strings of Varying Length Lexicographically
#Given: A permutation of at most 12 symbols defining an ordered alphabet A and a positive integer nn (n≤4n≤4).
#Return: All strings of length at most nn formed from A, ordered lexicographically. (Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on the order in which the symbols are given.)

from itertools import product

f = open("LEXV_Example.txt", "r")
str1 = ' '
mat = []
while (str1 != ''):
    str1 = f.readline().strip()
    mat.append(str1)
mat.remove("")

a = mat[0]
b = int(mat[1])


a = ['>'] + a.split()
c = []

for i in product(c, repeat = b):
	if '>' not in i:
		c.append(''.join(x))
	else:
		for j in range(1, b):
			if (''.join(i[j:b]) == '>'*(b-i) and '>' not in i[:j]):
				c.append(''.join(i).replace('>',''))

with open('ros.txt','w') as g:
	g.write('\n'.join(c))
	g.close()


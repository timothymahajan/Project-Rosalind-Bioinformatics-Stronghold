#Problem 19: Enumerating Gene Orders
#Given: A positive integer n≤7n≤7.
#Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

import itertools
n = 5
perm = list(itertools.permutations(range(1, n + 1)))

f = open('PERM.txt', 'w')
f.write(str(len(perm)))
f.write("\n")
for i in perm:
    f.write(' '.join(str(j) for j in i))
    f.write("\n")
f.close() 

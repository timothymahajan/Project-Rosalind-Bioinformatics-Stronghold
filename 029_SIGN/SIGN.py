#Problem 29: Enumerating Oriented Gene Orderings
#Given: A positive integer n≤6.
#Return: The total number of signed permutations of length n, followed by a list of all such permutations (you may list the signed permutations in any order).

import itertools 

n = 3                                                                      
permutation = []                                                           
total = 0 
c = itertools.permutations(list(range(1, n + 1)))

for i in c:
    d = itertools.product([-1, 1], repeat = len(list(range(1, n + 1))))
    for j in d:
        e = [i * sign for i, sign in zip(i, j)]                         
        permutation.append(e)                                           
        total = total + 1                                                            

print(total)                                                                  

for i in range(0, len(permutation)):                                          
    print(permutation[i], sep=' ')

#Problem 27: Partial Permutations
#Given: Positive integers n and k such that 100≥n>0100≥n>0 and 10≥k>010≥k>0.
#Return: The total number of partial permutations P(n,k)P(n,k), modulo 1,000,000.

from math import factorial

def numPartialPerms(n,k):
    perm = (factorial(n)/factorial(n-k)) % 1000000
    return perm

print(numPartialPerms(84,9))

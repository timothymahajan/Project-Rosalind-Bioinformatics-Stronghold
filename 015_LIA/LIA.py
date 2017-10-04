#Problem 15: Independent Alleles
#Given: Two positive integers k (k≤7k≤7) and N (N≤2kN≤2k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.
#Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.

import math

def prob(k,n):
    p = []
    q = 2**k
    for i in range(n,(q+1)):
        p.append(choose(q,i)* 0.25**i * 0.75**(q-i))
    return sum(p)

def choose(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


print (prob(6,19))

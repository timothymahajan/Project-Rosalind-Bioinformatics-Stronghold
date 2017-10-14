#Problem 60: Independent Segregation of Chromosomes
#Given: A positive integer n≤50.
#Return: An array A of length 2n2n in which A[k] represents the common logarithm of the probability that two diploid siblings share at least k of their 2n chromosomes (we do not consider recombination for now).

import math

def binomial(n, k, p):
    return (math.factorial(n) / math.factorial(k) / math.factorial(n-k)) * (p**k * (1-p)**(n-k))

n = 5

prob = []
for k in range(2*n, -1, -1):
    prob = prob + [binomial(n*2, k, 0.5)]

prob = [math.log10(sum(prob[:i])) for i in range(2*n, 0, -1)]

print(' '.join([str(i) for i in prob]))

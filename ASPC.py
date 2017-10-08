#Problem 45: Introduction to Alternative Splicing
#Given: Positive integers n and m with 0≤m≤n≤2000.
#Return: The sum of combinations C(n,k) for all k satisfying m≤k≤n, modulo 1,000,000.

from math import factorial

def comb (a, b):
        return factorial(a) // (factorial(b) * factorial(a - b))

m = 1911
n = 1260
sum = 0
    
for i in range(n, m + 1):
    sum = sum + comb(m, i)

print (sum % 1000000)
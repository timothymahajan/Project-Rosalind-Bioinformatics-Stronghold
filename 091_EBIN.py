#Problem 91: Wright-Fisher's Expected Behavior
#Given: A positive integer n (n≤1000000) followed by an array PP of length m (m≤20) containing numbers between 0 and 1. Each element of P can be seen as representing a probability corresponding to an allele frequency.
#Return: An array B of length m for which B[k] is the expected value of B in (n,P[k]); in terms of Wright-Fisher, it represents the expected allele frequency of the next generation.

with open('ebin.txt', 'r') as f:
    n = int(f.readline())
    p = [float(i) for i in f.readline().split(' ')]
        
for k in p:
    print (n*k)

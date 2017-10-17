#Problem 87: The Wright-Fisher Model of Genetic Drift
#Given: Positive integers N (N≤7), m (m≤2N), g (g≤6) and k (k≤2N).
#Return: The probability that in a population of N diploid individuals initially possessing m copies of a dominant allele, we will observe after g generations at least k copies of a recessive allele. Assume the Wright-Fisher model.

import math

def binomial(n, i, j):
    return (math.factorial(n) / math.factorial(i) / math.factorial(n-i)) * ((j/n)**i * (1-(j/n))**(n-i))

def probability(n, m, g, k):
    
    n = n * 2

    current = [0 for i in range(n+1)]
    current[m] = 1
    
    for z in range (g):

        next = [0 for i in range(n+1)]
        
        for i in range(n+1):
            for j in range(n+1):
                next[i] = next[i] + binomial(n, i, j) * current[j]
                
        current = next

    return sum(current[:-k])
       
print(probability(6, 8, 4, 6))

#Problem 85: Sex-Linked Inheritance
#Given: An array A of length n for which A[k] represents the proportion of males in a population exhibiting the k-th of nn total recessive X-linked genes. Assume that the population is in genetic equilibrium for all n genes.
#Return: An array B of length n in which B[k] equals the probability that a randomly selected female will be a carrier for the k-th gene.

with open('Example85.txt') as f:
    sex = map(float, f.readline().strip().split())
    
prob = [i * (1-i) / 0.5 for i in sex]
    
print(' '.join([str(i) for i in prob]))
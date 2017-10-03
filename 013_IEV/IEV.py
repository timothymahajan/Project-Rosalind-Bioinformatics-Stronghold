#Problem 13: Calculating Expected Offspring
'''
Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa
Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.
'''

f = open("Example14.txt", "r")
f = f.readline()
b = f.split(" ")
bint = []
for i in range (0, len(b)):
    bint.append(int(b[i]))

def expected (a):
    sum = (a[0] * 1 + a[1] * 1 + a[2] * 1 + a[3] *0.75 + a[4] *0.5 + a[5] * 0) * 2
    return sum

print(expected(bint))

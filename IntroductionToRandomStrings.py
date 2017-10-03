#Problem 28: Introduction to Random Strings
#Given: A DNA string ss of length at most 100 bp and an array AA containing at most 20 numbers between 0 and 1.
#Return: An array BB having the same length as AA in which B[k]B[k] represents the common logarithm of the probability that a random string constructed with the GC-content found in A[k]A[k] will match ss exactly.

import math

def RandomString(strRandomString, stringArray):
    strRandomString = strRandomString.upper()
    cg = len(strRandomString.replace('A', '').replace('T', ''))
    at = len(strRandomString.replace('C', '').replace('G', ''))
    inputArray = stringArray.split()
    outputArray = []
    for i in range(0, len(inputArray)):
        prob = cg * math.log10(float(inputArray[i]) / 2) + at * math.log10((1 - float(inputArray[i])) / 2)
        outputArray.append(round(prob, 3))
    return outputArray




result = ' '.join(map(str, RandomString('TGCTTGTTGTGTACTCGGCGGAATGACTTGTACGCCCCGCGAGTCGGCTGGATGATACGGCTGTAACGACTAAACGCTAA', '0.095 0.125 0.203 0.267 0.336 0.389 0.453 0.516 0.587 0.588 0.675 0.743 0.782 0.863 0.930')))

f = open('PROB.txt', 'w')
f.write(result)  
f.close() 


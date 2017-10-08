#Problem 44: Counting Subsets
#Given: A positive integer n (n≤1000n≤1000).
#Return: The total number of subsets of {1,2,…,n}{1,2,…,n} modulo 1,000,000.

num  = 820

def numberOfSets(num):
   return (2**num) % 1000000

print(numberOfSets(num))

#Problem 4: Rabbits and Recurrence Relations
#Given: Positive integers n≤40n≤40 and k≤5k≤5.
#Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

def fibonacci(n,k):
    seq = []
    num = 0
    for i in range (0, n):
        if (i == 0 or i == 1):
            seq.append(1)
        else:
            num = seq[i-1] + seq[i-2]*k
            seq.append(num)
    return seq

print(fibonacci(5,5))

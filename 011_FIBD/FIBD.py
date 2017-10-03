#Problem 11: MortalFibonacciRabbits
#Given: Positive integers n≤100n≤100 and m≤20m≤20.
#Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

mat = [1, 1]
def mortal (months, live):
    count = 2
    for i in range(2, months):
        if (i < live):
            mat.append(mat[len(mat)-2] + mat[len(mat)-1]) 
        elif (i == live or i == live+1):
            mat.append((mat[len(mat)-2] + mat[len(mat)-1]) - 1)
        else:
            mat.append((mat[len(mat)-2] + mat[len(mat)-1]) - (mat[len(mat)-(live+1)]))
    return (mat[len(mat)-1])

print (mortal(81, 17))
#37577591247583251

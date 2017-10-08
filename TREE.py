#Problem 32: Completing a Tree
#Given: A positive integer n (n≤1000n≤1000) and an adjacency list corresponding to a graph on n nodes that contains no cycles.
#Return: The minimum number of edges that can be added to the graph to produce a tree.

f = open('Example32.txt', 'r')
str1 = ' '
mat = []
while (str1 != ''):
    str1 = f.readline().strip()
    mat.append(str1)
mat.remove('')

n = int(mat[0])
#Takes the number of nodes n minus the total number of edges the adjaceny list minus one
#len(mat) = number of edges in the adjaceny list - 1
edge = n - len(mat)

print(edge)
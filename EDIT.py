#Problem 46: Edit Distance
#Given: Two protein strings s and t in FASTA format (each of length at most 1000 aa).
#Return: The edit distance dE(s,t).

f = open("Example46.txt", "r")
mat = []
str1 = f.read()
str1 = str1.replace("Rosalind_", "")
str1 = str1.replace("\n", "")
str1 = ''.join([i for i in str1 if not i.isdigit()])
mat = str1.split(">")
mat.remove("")

one = mat[0]
two = mat[1]

def edit(one, two):

    gp = list(range(len(one) + 1))

    for i, s in enumerate(two):
        last = gp
        gp = [i+1] 

        for j, t in enumerate(one):
            if (s == t):
                gp.append(last[j])

            else:
                gp.append(min([last[j+1], last[j], gp[-1]]) + 1)

    return gp[-1]

print(edit(one,two))
#Problem 25: Genome Assembly as Shortest Superstring
#Given: At most 50 DNA strings of equal length, not exceeding 1 kbp, in FASTA format (which represent reads deriving from the same strand of a single linear chromosome).
#The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.
#Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).

f = open("Example25.txt", "r")
mat = []
str1 = f.read()
str1 = str1.replace("Rosalind_", "")
str1 = str1.replace("\n", "")
str1 = ''.join([i for i in str1 if not i.isdigit()])
mat = str1.split(">")
mat.remove("")

def long(mat, bbb=''):
    if (len(mat) == 0):
        return bbb

    elif (len(bbb) == 0):
        bbb = mat.pop(0)
        return long(mat, bbb)

    else:
        for i in range(len(mat)):
            a = mat[i]
            for j in range(len(a) // 2):
                c = len(a) - j
                if bbb.startswith(a[j:]):
                    mat.pop(i)
                    return long(mat, a[:j] + bbb)
                if bbb.endswith(a[:c]):
                    mat.pop(i)
                    return long(mat, bbb + a[c:])
print(long(mat))

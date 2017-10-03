#Problem 5: Computing GC Content
#Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
#Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

n = ["CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG", "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT", "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"]
m = []
def gcContent(n):
    for i in n:
        count = 0
        for j in range(0, len(i)):
            if (i[j] == 'C' or i[j] == 'G'):
                count = count + 1
        l = count/len(i)
        m.append(l)
    large = 0
    for k in m:
        if (k > large):
            large = k
    return large*100

print(gcContent(n))

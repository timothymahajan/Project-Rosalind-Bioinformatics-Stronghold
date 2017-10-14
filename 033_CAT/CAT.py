#Problem 33: Catalan Numbers and RNA Secondary Structures
#Given: An RNA string s having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'. The length of the string is at most 300 bp.
#Return: The total number of noncrossing perfect matchings of basepair edges in the bonding graph of s, modulo 1,000,000.


f = open("Example33.txt", "r")
mat = []
str1 = f.read()
str1 = str1.replace("Rosalind_", "")
str1 = str1.replace("\n", "")
str1 = ''.join([i for i in str1 if not i.isdigit()])
mat = str1.split(">")
mat.remove("")

c = {'':1, 'A':0, 'C':0, 'G':0, 'U':0, 'AA':0, 'AC':0, 'AG':0, 'AU':1, 'CA':0, 'CC':0, 'CG':1, 'CU':0, 'GA':0, 'GC':1, 'GG':0, 'GU':0, 'UA':1, 'UC':0, 'UG':0, 'UU':0}

def catalan(mat):
    if (mat not in c):
        if mat.count('C') != mat.count('G') or mat.count('A') != mat.count('U'):
            c[mat] = 0
        else:
            c[mat] = sum([catalan(mat[1:i]) * c[mat[0]+mat[i]] * catalan(mat[i+1:]) for i in range(1, len(mat), 2)])
    return c[mat]
print(catalan(mat[0]) % 1000000)

f = open("Example12.txt", "r")
mat = []
str1 = f.read()
str1 = str1.replace("Rosalind_", "")
str1 = str1.replace("\n", "")
str1 = ''.join([i for i in str1 if not i.isdigit()])
mat = str1.split(">")
mat.remove("")


def consensus (m):
    a = []
    c = []
    g = []
    t = []
    for i in range(0, len(mat[0])):
        countA = 0
        countC = 0
        countG = 0
        countT = 0
        for j in mat:
            if (j[i] == "A"):
                countA = countA + 1
            elif (j[i] == "C"):
                countC = countC + 1
            elif (j[i] == "G"):
                countG = countG + 1
            elif (j[i] == "T"):
                countT = countT + 1
        a.append(countA)
        c.append(countC)
        g.append(countG)
        t.append(countT)
    profile = []
    for i in range(0, len(mat[0])):
        if (a[i] >= c[i] and a[i] >= g[i] and a[i] >= t[i]):
            profile.append("A")
        elif (c[i] >= a[i] and c[i] >= g[i] and c[i] >= t[i]):
            profile.append("C")
        elif (g[i] >= a[i] and g[i] >= c[i] and g[i] >= t[i]):
            profile.append("G")
        else:
            profile.append("T")
    strProfile = ''.join(profile)
    strA = 'A: ' + ' '.join(map(str,a))
    strC = 'C: ' + ' '.join(map(str,c))
    strG = 'G: ' + ' '.join(map(str,g))
    strT = 'T: ' + ' '.join(map(str,t))

    file = open("result12.txt","w")
    file.write(strProfile)
    file.write("\n")
    file.write(strA)
    file.write("\n")
    file.write(strC)
    file.write("\n")
    file.write(strG)
    file.write("\n")
    file.write(strT)
    file.write("\n")
    file.close()
    return strProfile, strA, strC, strG, strT
print(consensus(mat))



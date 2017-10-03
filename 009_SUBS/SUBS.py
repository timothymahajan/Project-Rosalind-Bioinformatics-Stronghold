#Problem 9: Finding a Motif in DNA
#Given: Two DNA strings s and t (each of length at most 1 kbp).
#Return: All locations of t as a substring of s.

def substring (str, sub):
    list = []
    for i in range (0, len(str) - len(sub)):
        a = str[i:i+len(sub)]
        if (a == sub):
            list.append(i+1)
    return list

print(substring("GATATATGCATATACTT", "ATAT"))

#Problem 6: Counting Point Mutations
#Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
#Return: The Hamming distance dH(s,t).

str1 = "GAGCCTACTAACGGGAT"
str2 = "CATCGTAATGACGGCCT"
def hammingDistance(str1, str2):
    count = 0
    for i in range(0, len(str1)):
        if (str1[i] != str2[i]):
            count = count + 1
    return count

print(hammingDistance(str1, str2))

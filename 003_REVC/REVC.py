#Problem 3: Complementing a Strand of DNA
#Given: A DNA string s of length at most 1000 bp.
#Return: The reverse complement sc of s.

def reverse (str):
    reverse = []
    for i in range(len(str)-1, -1, -1):
        reverse.append(str[i])
    for i in range(0, len(reverse)):
        if (reverse[i] == "A"):
            reverse[i] = "T"
        elif (reverse[i] == "T"):
            reverse[i] = "A"
        elif (reverse[i] == "C"):
            reverse[i] = "G"
        else:
            reverse[i] = "C"
    return reverse

print(reverse("AAAACCCGGT"))

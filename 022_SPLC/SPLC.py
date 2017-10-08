#Problem 22: RNA Splicing
#Given: A DNA string ss (of length at most 1 kbp) and a collection of substrings of ss acting as introns. All strings are given in FASTA format.
#Return: A protein string resulting from transcribing and translating the exons of ss. (Note: Only one solution will exist for the dataset provided.)

f = open("Example22.txt", "r")
str1 = f.read()
str1 = str1.replace("Rosalind_", "")
str1 = str1.replace("\n", "")
str1 = ''.join([i for i in str1 if not i.isdigit()])
intron = str1.split(">")
intron.remove("")
str = intron[0]
del intron[0]

for i in intron:
    str = str.replace(i, '')

cod = {
    'TTT': 'F',         'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
    'TTC': 'F',         'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
    'TTA': 'L',         'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
    'TTG': 'L',         'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
    'TCT': 'S',         'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
    'TCC': 'S',         'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'TCA': 'S',         'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'TCG': 'S',         'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'TAT': 'Y',         'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
    'TAC': 'Y',         'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'TAA': 'Stop',      'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'TAG': 'Stop',      'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'TGT': 'C',         'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
    'TGC': 'C',         'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'TGA': 'Stop',      'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'TGG': 'W',         'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}

b = []
for i in range(0, len(str), 3):
    f = str[i:i+3]
    b.append(f)


c = ''.join(cod[i] for i in b)
print(c)

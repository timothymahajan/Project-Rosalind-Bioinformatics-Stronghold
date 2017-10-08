#Problem 18: Open Reading Frames
#Given: A DNA string ss of length at most 1 kbp in FASTA format.
#Return: Every distinct candidate protein string that can be translated from ORFs of ss. Strings can be returned in any order.

rev = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

a1 = 'GCCTGAATAAAGGTCGCTAAAAGTAGCTAAACAGACAGCACGACCGTTAGCGCGTGGCGCGTTGTCGTCAGTTGTCCTATCCAAACCAATGCTGTCTTTGAGATGAGGATTCATAATCCTGTATGCATTAGGCAGAATGAATGATTATCGACAGGAAATGATATGTGGGCTAAACGTACCCCCACTGGCGGTCTTTGTTGCAACCCGATCAGTAAGGGTACGGGCACCGGCTAGAGAAGGGAACCAGATGTACGTGTTTTCTCCTCGCTGAGAAGGCGTGCTCAAAGAACAGTGGCCCTTAGGTGAAAAGATTCCTAGTTTCGGTGTGGTGTATTGCCCCAGCTAGCAGACTAATGCGTTCGTCCCGCTCTGTCTATTAGTACGTGCCGATGACTATCCTCTATGAATTCCCCTCGGGACGCCAATTAGCTAATTGGCGTCCCGAGGGGAATTCATTCGACGTGAGTATCTGTGTGTTTGAAAAGCCAAGTGGGAAGCGCGGCTGTTCGAGAAAAGCAACCTGAATTCAGAGAGTGTCTCACTGCGCACCTGCGGATAGGTCGACCGACGAGTTTAGGAGGTGGCGGCAAGAAATCGTACACGTGCCATGGGGTCCTAACTCTGTGAAGAGGAGCTTCGACATGTCTGTCAACACTGGCGTTCCCGTCGAGCCAGTGAGGCATACCATCCTAAAAGCAGTGTAGTGAACATTATCCCAAACACATCGCGATATCGACCCTAGTAGGTCACACCGGATAGACCGTAGCGTGATGTCCACATCGCTTTCAACTGGATAAAGTGCGGTGGCCACTAATTGACTGCCTAAGCTGGAACCGGCCGAACGCCTATTAATTTCTG'
a2 = a1[1:len(a1)] + a1[0]
a3 = a1[2:len(a1)] + a1[0:2]

aRev1 = ''.join([i for i in reversed(a1)])
aRev2 = aRev1[1:len(aRev1)] + aRev1[0]
aRev2 = ''.join(rev[i] for i in aRev2)
aRev3 = aRev1[2:len(aRev1)] + aRev1[0:2]
aRev3 = ''.join(rev[i] for i in aRev3)



a1m = []
a2m = []
a3m = []
aRev1m = []
aRev2m = []
aRev3m = []

def cod (lst, mat):
    if (len(lst) % 3 == 1):
        lst = lst[0:len(lst)-1]
    if (len(lst) % 3 == 2):
        lst = lst[0:len(lst)-2]
    #In this case, the stop codon is identified by the letter 'Z'
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
    'TAA': 'Z',         'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'TAG': 'Z',         'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'TGT': 'C',         'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
    'TGC': 'C',         'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'TGA': 'Z',         'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'TGG': 'W',         'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
    }
    for i in range(0, len(lst), 3):
        f = lst[i:i+3]
        mat.append(f)
    c = ''.join(cod[i] for i in mat)
    return c

a1m = cod(a1, a1m)
a2m = cod(a2, a2m)
a3m = cod(a3, a3m)

aRev1m = cod(aRev1, aRev1m)
aRev2m = cod(aRev2, aRev2m)
aRev3m = cod(aRev3, aRev3m)

fin = []

def protein (prt):
    for i in range(0, len(prt)):
        if (prt[i] == 'M'):
            for j in range(i, len(prt)):
                if (prt[j] == 'Z'):
                    fin.append(prt[i:j])
                    break
    return fin

protein(a1m)
protein(a2m)
protein(a3m)
protein(aRev1m)
protein(aRev2m)
a = protein(aRev3m)
proteins = list(set(a))

for i in proteins:
    print(i)
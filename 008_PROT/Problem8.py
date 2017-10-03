def protein (rna):
    codon = ""
    protein = []
    for i in range(0, len(rna) - 3, 3):
        codon = rna[i:i+3]
        if (codon == "UUU" or codon == "UUC"):
            protein.append("F")
        elif (codon == "UUA" or codon == "UUG"):
            protein.append("L")
        elif (codon == "UCU" or codon == "UCC" or codon == "UCA" or codon == "UCG"):
            protein.append("S")
        elif (codon == "UAU" or codon == "UAC"):
            protein.append("Y")
        elif (codon == "UAA" or codon == "UAG" or codon == "UGA"):
            break
        elif (codon == "UGU" or codon == "UGC"):
            protein.append("C")
        elif (codon == "UGG"):
            protein.append("W")
        elif (codon == "CUU" or codon == "CUC" or codon == "CUA" or codon == "CUG"):
            protein.append("L")
        elif (codon == "CCU" or codon == "CCC" or codon == "CCA" or codon == "CCG"):
            protein.append("P")
        elif (codon == "CAU" or codon == "CAC"):
            protein.append("H")
        elif (codon == "CAA" or codon == "CAG"):
            protein.append("Q")
        elif (codon == "CGU" or codon == "CGC" or codon == "CGA" or codon == "CGG" or codon == "AGA" or codon == "AGG"):
            protein.append("R")
        elif (codon == "AUU" or codon == "AUC" or codon == "AUA"):
            protein.append("I")
        elif (codon == "AUG"):
            protein.append("M")
        elif (codon == "ACU" or codon == "ACC" or codon == "ACA" or codon == "ACG"):
            protein.append("T")
        elif (codon == "AAU" or codon == "AAC"):
            protein.append("N")
        elif (codon == "AAA" or codon == "AAG"):
            protein.append("K")
        elif (codon == "AGU" or codon == "AGC"):
            protein.append("S")
        elif (codon == "GUU" or codon == "GUC" or codon == "GUA" or codon == "GUG"):
            protein.append("V")
        elif (codon == "GCU" or codon == "GCC" or codon == "GCA" or codon == "GCG"):
            protein.append("A")
        elif (codon == "GAU" or codon == "GAC"):
            protein.append("D")
        elif (codon == "GAA" or codon == "GAG"):
            protein.append("E")
        elif (codon == "GGU" or codon == "GGC" or codon == "GGA" or codon == "GGG"):
            protein.append("G")
    return protein

print(protein("AUGUAAGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"))


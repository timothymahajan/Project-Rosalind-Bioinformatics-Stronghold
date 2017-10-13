#Problem 34: Error Correction in Reads	
#Given: A collection of up to 1000 reads of equal length (at most 50 bp) in FASTA format. Some of these reads were generated with a single-nucleotide error. For each read s in the dataset, one of the following applies:
#    s was correctly sequenced and appears in the dataset at least twice (possibly as a reverse complement);
#    s is incorrect, it appears in the dataset exactly once, and its Hamming distance is 1 with respect to exactly one correct read in the dataset (or its reverse complement).
#Return: A list of all corrections in the form "[old read]->[new read]". (Each correction must be a single symbol substitution, and you may return the corrections in any order.)

def HammingDistance(string1, string2):
    result = 0
    for i in range(0, len(string1)):
        if(string1[i] != string2[i]):
            result += 1
    return result

def FastaReaderStringsOnly(strFileName):
    resultList = []
    resultString = ''
    with open(strFileName) as f:
        for line in f:
            if ('>' in line):
                if (resultString != ''):
                    resultList.append(resultString)
                    resultString = ''
            else:
                resultString = resultString + line.strip()
        if (resultString != ''):
            resultList.append(resultString)
    return resultList

def ReverseComplement (strDNA):
    result = ""
    for i in range(len(strDNA)-1, -1, -1):
        if (strDNA[i] == "A"):
            result += "T"
        elif (strDNA[i] == "T"):
            result += "A"
        elif (strDNA[i] == "C"):
            result += "G"
        else:

            result += "C" 
    return result

strings = list(FastaReaderStringsOnly("Example34.txt"))
stringsReverseComplement = list(map(ReverseComplement, strings))
stringsReverseComplement.extend(strings)

result = []
for oldRead in strings:
    if stringsReverseComplement.count(oldRead) == 1:
        for newRead in stringsReverseComplement:
            if(HammingDistance(oldRead, newRead) == 1):
                if(stringsReverseComplement.count(newRead) > 1):
                    result.append(oldRead + '->' + newRead)

result = list(set(result))
f = open('ErrorCorrections.txt', 'w')
for string in result:
     f.write(string)
     f.write('\n')
f.close() 






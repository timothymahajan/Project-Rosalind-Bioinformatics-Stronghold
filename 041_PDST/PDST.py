#Problem 41: Creating a Distance Matrix
#Given: A collection of n (n≤10) DNA strings s1,…,sn of equal length (at most 1 kbp). Strings are given in FASTA format.
#Return: The matrix D corresponding to the p-distance dpdp on the given strings. As always, note that your answer is allowed an absolute error of 0.001.

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

strings = FastaReaderStringsOnly("Example41.txt")
ln = len(strings)
st = strings[0]
ln_string = len(st)

matrix = [[0 for x in range(ln)] for y in range(ln)] 

for i in range(0, ln):
    for j in range(0, i):
        matrix[i][j] = HammingDistance(strings[i], strings[j])/ln_string 
        matrix[j][i] = matrix[i][j]

f = open('DistanceMatrix.txt', 'w')
line = ""
for i in range(0, ln):
    for j in range(0, ln):
        line = line + str(matrix[i][j]) + '\t'
    f.write(line)
    f.write('\n')
    line = ""
f.close() 


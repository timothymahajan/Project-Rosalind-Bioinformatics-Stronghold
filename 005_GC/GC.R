#Problem 5: Computing GC Content
#Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
#Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

seq <- read.fasta("Example5.txt")
gc <- apply(matrix(names(seq)), 1, function(x){GC(seq[[x]])})
max <- which(gc==max(gc))
rbind(names(seq)[max], paste(signif(gc[max], 4) * 100, "%", sep=""))

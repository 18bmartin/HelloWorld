#finding and opening the initial file
DNAfile = open('/users/18bmartin/downloads/genomic_dna.txt', 'r')
DNAsequence = DNAfile.read()

#splitting the file data into exons and an intron
exon1 = DNAsequence[0:63]
intron = DNAsequence[63:90]
exon2 = DNAsequence[90:]

#creating a file for the exons
exonFile = open('exonFile.txt', 'w')
exonFile.write(exon1 + exon2)

#creating a file for the intron
intronFile = open('intronFile.txt', 'w')
intronFile.write(intron)

#close all the files
DNAfile.close()
exonFile.close()
intronFile.close()
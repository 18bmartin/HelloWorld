inFile = open('/users/18bmartin/downloads/ex3-1_input.txt', 'r')
outFile = open('trim.txt.', 'w')

for line in inFile:
    line = line[14:]
    outfile = outFile.write(line)

outFile.close()
inFile.close()
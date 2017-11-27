#open the files
inFile = open('/users/18bmartin/downloads/ex3-1_input.txt', 'r')
outFile = open('trim.txt.', 'w')

#trim, add the new line to the file, print the line and the length of the line
for line in inFile:
    line = line[14:]
    outfile = outFile.write(line)
    print("line is", len(line), "chratcers long.")
    print(line)

#close the files
outFile.close()
inFile.close()
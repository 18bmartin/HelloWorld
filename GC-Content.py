dnaSequence = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'

#find the variables from the DNA  sequence
numGs = int(dnaSequence.count('G'))
numCs = int(dnaSequence.count('C'))
total = int(len(dnaSequence))

#equate the percentage of GC units
percentageGC = ((numCs + numGs)/total)*100

#printing all the variables used in the equation
print(str(numGs))
print(str(numCs))
print(str(total))

#3 ways to round up the deicmal points
print(str(round(percentageGC, 2)))

percentageGC2 = ("%.1f" % percentageGC)
print(str(percentageGC2))

print('GC content is {0:.1f}%'.format(percentageGC))

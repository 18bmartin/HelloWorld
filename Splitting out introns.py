#the initial DNA sequence
dnaSequence = '''ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT'''

#cutting the intron out of the DNA code
segment1 = dnaSequence[0:63]
segment2 = dnaSequence[90:]

#printing the sequence with and without an intron
print("the total DNA sequence is", dnaSequence)
print("the sequence without an intron is", segment1 + segment2)

#a) finding the length of all the variables in order to do calculations with them
segment1len = len(segment1)
segment2len = len(segment2)
dnaSequenceLen =len(dnaSequence)

#calculating the percent
percent = ((segment1len + segment2len)/dnaSequenceLen)*100

#printing the percent
print("the code is {0:.1f}% exon".format(percent))

#b) finding the intron within the code
intron = dnaSequence[63:90]

#making the intron a lowercase
intron = intron.lower()

#printing the total sequence with lowercase intron
print(segment1 + intron + segment2)

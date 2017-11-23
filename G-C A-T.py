#the initial DNA sequence
dnaSequence = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT'

#changing all the corresponding letters
AtoT = dnaSequence.replace("A", "t")
TtoA = AtoT.replace("T", "a")
CtoG = TtoA.replace("C", "g")
GtoC = CtoG.replace("G", "c")

#making the replacement into uppercase
newDNA = GtoC.upper()

#printing the original DNA sequence and its compliment
print(dnaSequence)
print(newDNA)
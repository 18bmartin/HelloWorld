#the initial DNA sequence
dnaSequence = 'ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT'

#seperating the DNA sequence at the specified location
firstFragment = 'ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT' [0:22]
secondFragment = 'ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT' [23:100]

#finsing the length of the 2 fragments
firstFragmentLen = len(firstFragment)
secondFragmentLen = len(secondFragment)

#printing the original and the split DNA sequence
print("the original DNA sequence is", dnaSequence)
print("the first fragment is", firstFragment, "and is", firstFragmentLen ,"letters long")
print("the second fragment is", secondFragment, "and is", secondFragmentLen,"letters long")

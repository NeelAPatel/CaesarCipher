import sys

def getDictionary(dictName):
	dictFile = open(dictName, "r")
	dictFileArr = dictFile.readlines()
	dictFile.close()
	
	#remove trailing \n
	for index in range(len(dictFileArr)):
		dictFileArr[index] = dictFileArr[index].lower().strip()
		
	return dictFileArr
	
# Recieve files from input
ciphFile = sys.argv[1]
dictFile = getDictionary(sys.argv[2])

# Get first line from cipher
with open(ciphFile, "r") as file:
	ciphLine = file.readline().strip()

alphabet = "abcdefghijklmnopqrstuvwxyz"

wordsMatched = []  # should be about 26
for shiftIndex in range(26):
	decryptLine = ""
	wordMatchCount = 0
	for ltr in ciphLine:
		# gets each letter
		ltr = ltr.lower()
		
		# check if letter is in alphabet because spaces
		if ltr in alphabet:
			ciphLtrIndex = alphabet.index(ltr)
			
			# Shift and grab letter
			shiftVal = (ciphLtrIndex + shiftIndex) % 26  # move to next value
			shiftLtr = alphabet[shiftVal]
			
			# add letter to line
			decryptLine += shiftLtr
		else:
			# Must be a space or punctuation
			decryptLine += ltr
	
	# Now check how many words have matched
	decrypted = decryptLine.split(" ")
	for dWrd in decrypted:
		if dWrd in dictFile:
			wordMatchCount += 1
	
	wordsMatched.append(wordMatchCount)

# print(wordsMatched)
# print(max(wordsMatched))
decryptionShift = wordsMatched.index(max(wordsMatched))

decryptFile = []
# decrypt all lines now
with open(ciphFile, "r") as file:
	for ciphLine in file:
		ciphLine = ciphLine.lower()
		decryptLine = ""
		for ltr in ciphLine:
			ltr = ltr.lower()
			if ltr in alphabet:
				ciphLtrIndex = alphabet.index(ltr)
				
				# Shift and grab letter
				shiftVal = (ciphLtrIndex + decryptionShift) % 26  # move to next value
				shiftLtr = alphabet[shiftVal]
				
				# add letter to line
				decryptLine += shiftLtr
			else:
				# Must be a space or punctuation
				decryptLine += ltr
		decryptFile.append(decryptLine)

#output
print(decryptionShift)
for l in decryptFile:
	print(l)
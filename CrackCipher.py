import sys

def getFreq(fileName, alphabet):
	
	freq = [0] * 27
	with open(fileName, "r") as file:
		for fLine in file:
			fLine = fLine.lower().strip()
			for ltr in fLine:
				ltr = ltr.lower()
				if ltr in alphabet:
					freq[alphabet.find(ltr)] += 1
	
	return freq

# Recieve files from input
ciphFile = sys.argv[1]
knownFile = sys.argv[2]

#alphabet set
alphabet = " abcdefghijklmnopqrstuvwxyz" #space included this time

#Get frequency arrays
ciphFreq = getFreq(ciphFile, alphabet)
knownFreq = getFreq(knownFile, alphabet)

# use dictionaries to make a:### pairs
ciphDict = dict(zip(alphabet, ciphFreq))
knownDict = dict(zip(alphabet, knownFreq))
ciphFreq.sort(reverse=True)
knownFreq.sort(reverse=True)

ciphMap = []
knownMap = []

for i in range(27):
	for ltr, count in ciphDict.items():
		if count == ciphFreq[i]:
			ciphMap.append(ltr)
	
	for ltr, count in knownDict.items():
		if count == knownFreq[i]:
			knownMap.append(ltr)

decryptMap = dict(zip(ciphMap, knownMap))

with open(ciphFile, "r") as file:
	for ciphLine in file:
		ciphLine = ciphLine.lower()
		decryptedLine = ""
		# print("====")
		for ltr in ciphLine:
			ltr = ltr.lower()
			if ltr in alphabet:
				decryptedLine += decryptMap.get(ltr)
			else:
				decryptedLine += ltr
		print(decryptedLine)
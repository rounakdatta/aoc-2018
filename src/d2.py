def p1():

	# get input
	f = open('./input/d2.txt')
	inp = f.readlines()
	inp = [foo.strip() for foo in inp]

	# code
	twos = 0
	threes = 0

	for code in inp:

		charDict = {}
		for i in range(len(code)):
			try:
				charDict[code[i]] += 1
			except:
				charDict[code[i]] = 1

		twoDone = False
		threeDone = False
		for i in range(len(code)):
			if twoDone and threeDone:
				break

			if charDict[code[i]] == 2:
				twoDone = True
			if charDict[code[i]] == 3:
				threeDone = True

		if twoDone:
			twos += 1
		if threeDone:
			threes += 1

	return twos * threes

def findCommonPart(astring, bstring):
	commonPart = ''

	for i in range(len(astring)):
		if astring[i] == bstring[i]:
			commonPart += astring[i]

	return commonPart

def p2():

	# get input
	f = open('./input/d2.txt')
	inp = f.readlines()
	inp = [foo.strip() for foo in inp]	

	# code
	correctBoxes = []

	for icode1 in range(len(inp) - 1):

		for icode2 in range(icode1 + 1, len(inp)):

			differCount = 0
			for i in range(len(inp[icode1])):
				if inp[icode1][i] != inp[icode2][i]:
					differCount += 1

			if differCount == 1:
				correctBoxes.append(inp[icode1])
				correctBoxes.append(inp[icode2])
				return findCommonPart(correctBoxes[0], correctBoxes[1])

	return ''

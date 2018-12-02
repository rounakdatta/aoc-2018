def p1():

	# get input
	f = open('./input/d1.txt')
	inp = f.readlines()
	inp = [foo.strip() for foo in inp]

	# code
	resultFreq = 0
	for eachFreq in inp:
		resultFreq += int(eachFreq)

	return resultFreq

def p2():

	# get input
	f = open('./input/d1.txt')
	inp = f.readlines()
	inp = [foo.strip() for foo in inp]	

	# code
	repeatFreqFound = False
	resultFreq = 0
	counter = 0
	allStatesTillNow = []
	while not repeatFreqFound:
		resultFreq += int( inp[counter % len(inp)] )

		if resultFreq in allStatesTillNow:
			repeatFreqFound = True

		allStatesTillNow.append(resultFreq)
		counter += 1

	return resultFreq
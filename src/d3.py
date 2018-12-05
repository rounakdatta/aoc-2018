def p1():

	# get input
	f = open('./input/d3.txt')
	inp = f.readlines()
	inp = [foo.strip() for foo in inp]

	max_width = 1000
	max_height = 1000

	import numpy as np
	matrix = np.zeros([max_height, max_width], dtype=int)

	# code
	for icode in range(len(inp)):
		currCode = inp[icode].split()

		shifted = currCode[2][:-1].split(',')
		shifted = [int(shifted[0]), int(shifted[1])]

		dim = currCode[3].split('x')
		dim = [int(dim[0]), int(dim[1])]
		
		for i in range(dim[0]):
			for j in range(dim[1]):
				matrix[(shifted[0] - 1) + i][(shifted[1] - 1) + j] += 1

	count = 0
	for i in range(max_height):
		for j in range(max_width):
			if matrix[i][j] > 1:
				count += 1

	return count


def p2():

	# get input
	f = open('./input/d3.txt')
	inp = f.readlines()
	inp = [foo.strip() for foo in inp]	

	# code
	max_width = 1000
	max_height = 1000

	import numpy as np
	matrix = np.zeros([max_height, max_width], dtype=int)

	# code
	notOverlapping = 0

	for icode in range(len(inp)):
		currCode = inp[icode].split()

		shifted = currCode[2][:-1].split(',')
		shifted = [int(shifted[0]), int(shifted[1])]

		dim = currCode[3].split('x')
		dim = [int(dim[0]), int(dim[1])]
		
		for i in range(dim[0]):
			for j in range(dim[1]):
				matrix[(shifted[0] - 1) + i][(shifted[1] - 1) + j] += 1	

	for icode in range(len(inp)):
		currCode = inp[icode].split()

		shifted = currCode[2][:-1].split(',')
		shifted = [int(shifted[0]), int(shifted[1])]

		dim = currCode[3].split('x')
		dim = [int(dim[0]), int(dim[1])]
		
		doesOverlap = False
		for i in range(dim[0]):
			for j in range(dim[1]):
				if matrix[(shifted[0] - 1) + i][(shifted[1] - 1) + j] != 1:
					doesOverlap = True

		if not doesOverlap:
			notOverlapping = currCode[0][1:]

	return notOverlapping
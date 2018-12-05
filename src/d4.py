def p1():

	# get input
	f = open('./input/d4.txt')
	inp = f.readlines()
	inp = [foo.strip() for foo in inp]

	# code
	dataset = []
	for obsv in inp:
		obsv = obsv.split(' ')
		obsv = [ obsv[0][1:], obsv[1][:-1] ] + obsv[2:]
		obsv = obsv[0].split('-') + obsv[1].split(':') + obsv[2:]

		dataset += [obsv]

	dataset = sorted(dataset, key=lambda foo: (foo[1], foo[2], foo[3], foo[4]))
	
	sleepDict = {}
	listOfGuards = []

	sleepMeter = [0, 0, 0]
	start = 0
	end = 0
	i = 0
	currGuard = ''
	while i < len(dataset):
		if dataset[i][5] == 'Guard':

			try:
				if dataset[i - 1][5] == 'Guard':
					currGuard = dataset[i][6][1:]
					i += 1
					sleepMeter = [0, 0, 0]
					continue

			except:
				continue

			try:	
				lastPerson = currGuard
				try:
					sleepDict[lastPerson][0] = max(sleepDict[lastPerson][0], sleepMeter[0])
					sleepDict[lastPerson].append(sleepMeter)
				except:
					sleepDict[lastPerson] = [sleepMeter[0], sleepMeter]
					listOfGuards.append(lastPerson)
			except Exception as e:
				True

			currGuard = dataset[i][6][1:]
			i += 1
			sleepMeter = [0, 0, 0]
			continue
		else:
			if dataset[i][5] == 'falls':
				start = dataset[i][4]
			if dataset[i][5] == 'wakes':
				end = dataset[i][4]
				sleepTime = (int(end) - int(start))
				sleepMeter = [sleepMeter[0] + sleepTime, start, end]
			i += 1

	listOfGuards = listOfGuards[1:]
	timeSlept = sorted([(int(foo), sleepDict[foo][0]) for foo in listOfGuards], key=lambda x: x[1])
	mostSleepyGuard = timeSlept[-1][0]
	maxTimeSlept = timeSlept[-1][1]

	sleepyData = sleepDict[str(mostSleepyGuard)]

	import numpy as np
	timespan = np.zeros(60)
	
	for i in range(1, len(sleepyData)):
		for j in range(int(sleepyData[i][1]), int(sleepyData[i][2])):
			timespan[j] += 1

	mostSleptMinute = timespan.argmax()

	return mostSleepyGuard * mostSleptMinute


def p2():

	# get input
	f = open('./input/d4.txt')
	inp = f.readlines()
	inp = [foo.strip() for foo in inp]	

	# code
	

import requests

def getQuestionInput(day):

	getURL = 'https://adventofcode.com/2018/day/' + str(day) + '/input'

	headers = {
	    'authority': 'adventofcode.com',
	    'cache-control': 'max-age=0',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	    'referer': 'https://adventofcode.com/2018/day/' + str(day),
	    'accept-encoding': 'gzip, deflate, br',
	    'accept-language': 'en-US,en;q=0.9',
	    'cookie': 'session=53616c7465645f5f67a1ded0fd4122438efe619ff177de6ff2f45c373f9a43056d7ca2b0ff1ca521f93aaba96f1b0cec',
	}

	responseObj = requests.get(getURL, headers=headers)
	f = open('./input/d' + str(day) + '.txt', 'w+')
	inputContent = responseObj.content.decode("utf-8") 
	f.write(inputContent)
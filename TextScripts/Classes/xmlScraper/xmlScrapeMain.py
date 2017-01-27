from xmlScraper import *

def initialize():
	url = 'https://api.sportradar.us/nba-t3/league/hierarchy.xml?api_key=n62whvrs4yg3qrp55vayfew5'
	queryDict = {}
	queryList = list(queryDict.items())
	if len(queryList != 1):
		for i in range(len(queryList)):
			url  = url + queryList[i][0] + '=' + queryList[i][1] + '&'
		url = url[:len(url) - 1]
	args = [url,'',[],None,[],None]
	a = scraper(args)
	data = a.scrape()
	a.getNodeTags('team')
	a.parse()
	#a.removeRecords(['keyword1','keyword2'])
	a.writeFile('filename.txt')
initialize()
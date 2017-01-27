from xmlScraperSportAPI import *

def getData(rootNode, argString):
	url = 'https://api.sportradar.us/nba-t3/'+argString+'.xml?api_key=n62whvrs4yg3qrp55vayfew5'
	args = [url,'',[],None,[],None]
	a = scraper(args)
	a.scrape()
	data = a.parseText(rootNode)
	return data


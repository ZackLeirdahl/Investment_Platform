from xmlScraperSportAPI import *

def getData(rootNode, argString):
	url = 'https://api.sportradar.us/nba-t3/'+argString+'.xml?api_key=n62whvrs4yg3qrp55vayfew5'
	args = [url,'',[],None,[],None]
	a = scraper(args)
	a.scrape()
	data = a.parseText(rootNode)
	return data
	
def initialize():
	teamID = ''
	playerID = ''
	teamIDs = []
	teamDict = dict()
	rootNodes = ['{http://feed.elasticstats.com/schema/basketball/nba/hierarchy-v2.0.xsd}team','{http://feed.elasticstats.com/schema/basketball/team-v2.0.xsd}player','{http://feed.elasticstats.com/schema/basketball/nba/hierarchy-v2.0.xsd}statistics']
	for i in range(len(rootNodes)):
		argStrings = ['league/hierarchy','teams/'+teamID+'/profile','players/'+playerID+'/profile']
		if i == 0:
			leagueData = getData(rootNodes[i],argStrings[i])
			for j in range(len(leagueData)):
				team = leagueData[j]
				teamDict[team['alias']]= team['id']
		if i == 1:
			for k in teamDict:
				teamID = teamDict[k]
				playerData = getData(rootNodes[i], argStrings[i])
			for j in range(len(playerData)):
				player = playerData[j]
				print(player)

initialize()
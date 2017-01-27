from xmlScraper import *

url = 'http://service.dice.com/api/rest/jobsearch/v1/simple.xml?text=Analytics&sort=2&age=14&direct=1&areacode=55414&skill=Mining'
args = [url,'',[],None,[],None]
a = scraper(args)
data = a.scrape()
a.getNodeTags('resultItem')
a.parse()
a.removeRecords(['Senior'])
a.writeFile('testfille.txt')

#def initialize():
#	url = 'http://service.dice.com/api/rest/jobsearch/v1/simple.xml?'
#	queryDict = {'arg1':'acutalsearch'}
#	queryList = list(queryDict.items())
#	for i in range(len(queryList)):
#		url  = url + queryList[i][0] + '=' + queryList[i][1] + '&'
#	url = url[:len(url) - 1]
#	print(url)
#	
#initialize()
from Scraper import *
#url = 'http://www.xignite.com/xAnalysts.asmx/GetResearchReport?Identifier=MSFT&IdentifierType=Symbol&AnalystsResearchReportType=CurrentSalesConsensus&_Token=BAB72711CD9847A4964B778333727670'
url = 'http://www.basketball-reference.com/players/t/townska01/splits/'
a = scraper(url)
c = htmlScraper()
data = a.scrape()
print(data)
#d = c.feed(data)
#print(d)

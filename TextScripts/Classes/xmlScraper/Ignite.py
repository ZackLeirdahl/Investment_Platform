from Scraper import *
url = 'http://www.xignite.com/xAnalysts.asmx/GetResearchReport?Identifier=MSFT&IdentifierType=Symbol&AnalystsResearchReportType=CurrentSalesConsensus&_Token=BAB72711CD9847A4964B778333727670'
args = [url,'',[],None,[],None]
a = scraper(args)
a.scrape()
data = a.parseText('{http://www.xignite.com/services/}Values')
print(data)

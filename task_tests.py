from realtime import Realtime
from refresh import RefreshStats
from news import News
from price import CurrentPrice
from company import Company

def realtime_test(companies):
	t = Realtime(companies, output_root = r'C:\Users\zleirdahl\Desktop\PythonScripts\iex\Data\RealTime\\', header_fields = ['Minute','High','Low','Average','Change','Trades','Volume'], file_suffix = 'realtime')
	t.run()

def refreshstats_test(companies):
	t = RefreshStats(companies, output_root = r'C:\Users\zleirdahl\Desktop\PythonScripts\iex\Data\Stats\\', file_suffix = 'stats')
	t.run()

def news_test(companies):
	t = News(companies, output_root = r'C:\Users\zleirdahl\Desktop\PythonScripts\iex\Data\News\\', header_fields = ['Date','Headline','Source','URL','Summary'], file_suffix = 'news')
	t.run()

def price_test(companies):
	t = CurrentPrice(companies, output_root = r'C:\Users\zleirdahl\Desktop\PythonScripts\iex\Data\Price\\', file_suffix = 'price')
	t.run()

def company_test(companies):
	t = Company(companies, output_root = r'C:\Users\zleirdahl\Desktop\PythonScripts\iex\Data\Companies\\', file_suffix = 'company')
	t.run()
	
if __name__ == '__main__':
	
	test_name = 'company'
	
	companies = ['aapl','nflx']
	test_dict = {
		'realtime': realtime_test,
		'refreshstats': refreshstats_test,
		'news': news_test,
		'price': price_test,
		'company': company_test}
	test_dict[test_name.lower()](companies)
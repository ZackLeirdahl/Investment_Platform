import statistics
from request import RequestHub

def format_results(results):
	formatted = []
	for i in range(len(results['minute'])):
		try:
			minute = str(results['minute'][i])
			high = str(round(results['high'][i],2))	
			low = str(round(results['low'][i],2))
			average = str(round(results['average'][i],2))
			trades = str(results['marketNumberOfTrades'][i])
			change = str(round(results['changeOverTime'][i],3))
			volume = str(results['volume'][i])
			formatted.append(','.join([minute,high,low,average,change,trades,volume]))
		except:
			continue
	return formatted
	
def write_data(result, file_name, output_root = r'C:\Users\zleirdahl\Desktop\PythonScripts\iex\Data\RealTime\\'):
	with open(output_root + file_name, 'w') as wf:
		wf.write('Minute,High,Low,Average,Change,Trades,Volume\n')
		for line in result:
			wf.write(line + '\n')


if __name__  == '__main__':
	hub = RequestHub()
	companies = ['aapl']
	actions = ['chart//1d']
	action_keys = {'chart//1d': ['minute','volume','changeOverTime','high','low','average','marketNumberOfTrades']}
	requests = hub.get_requests(companies,actions)
	results = dict.fromkeys(companies,dict.fromkeys(actions))
	for company in results.keys():
		for i in range(len(actions)):
			result = hub.get_result(actions[i], action_keys[actions[i]],requests[company][actions[i]])
			results[company][actions[i]] = format_results(result)
	for company in companies:
		write_data(results[company]['chart//1d'], company + '_RealTime.csv')

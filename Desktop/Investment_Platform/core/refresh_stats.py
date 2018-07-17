from request import RequestHub


class Refresh:
	def __init__(self):
		self.Name = 'RefreshNew'
	
	def compute_chart(self, result):
		formatted = {}
		daily = {}
		periods = [5,10,20]
		average_keys = ['close','change','spread','volume']
		for i in range(len(result['date'])):
			daily[i] = {
				'date': result['date'][i],
				'open': round(result['open'][i],2),
				'close': round(result['close'][i],2),
				'change': round(result['changePercent'][i],2),
				'high': round(result['high'][i],2),
				'low': round(result['low'][i],2),
				'spread': round((round(result['high'][i],2)-round(result['low'][i],2)),2),
				'volume': result['volume'][i]
			}
		daily = sorted(daily.items())
		averages = dict.fromkeys(periods)
		for i in range(len(periods)):
			averages[periods[i]] = self.compute_avg(len(result['date']), periods[i], daily)
		for period in averages.keys():
			for i in range(len(average_keys)):
				formatted[str(period)+ 'Day' +average_keys[i]] = averages[period][average_keys[i]]
		return formatted
		
	def compute_avg(self, num_days, days, daily, average_keys = ['close','change','spread','volume']):
		vals = dict.fromkeys(average_keys,0)
		temp = {}
		i = num_days - days
		while i <= (num_days - 1):
			temp[i] = daily[i]
			i+=1
		for k in temp.keys():
			for j in range(len(average_keys)):
				vals[average_keys[j]] += temp[k][1][average_keys[j]]
		for k in vals.keys():
			vals[k] = round((vals[k]/days),2)
		return vals

	def format_results(self, results,	lines = []):
		for key in sorted(results):
			value = results[key]
			if type(value) == float:
				value = round(value,2)
			lines.append(str(key) + ',' + str(value))
		return lines

if __name__ == '__main__':
	hub = RequestHub()
	r = Refresh()
	companies = ['aapl','nflx']
	actions = ['chart','stats']
	action_keys = {
				'chart': ['date','high','low','volume','changePercent','open','close'],
				'stats': ['marketcap','beta','week52high','week52low','week52change','shortInterest','shortDate','float','consensusEPS','day200MovingAvg','day50MovingAvg','institutionPercent','insiderPercent','shortRatio','month6ChangePercent','month3ChangePercent','month1ChangePercent','day5ChangePercent']}
	requests = hub.get_requests(companies,actions)
	results = dict.fromkeys(companies,dict.fromkeys(actions))
	for company in results.keys():
		for i in range(len(actions)):
			result = hub.get_result(actions[i], action_keys[actions[i]],requests[company][actions[i]])
			if actions[i] == 'chart':
				result = r.compute_chart(result)
			results[company][actions[i]] = result
		results[company]['stats'].update(results[company]['chart'])
		formatted = r.format_results(results[company]['stats'])
		hub.write_results(formatted, r'C:\Users\zleirdahl\Desktop\PythonScripts\iex\Data\Stats\\' + company + '_stats.csv')

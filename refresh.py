from task import BaseTask

class RefreshStats(BaseTask):
	def __init__(self, companies, **kwargs):
		BaseTask.__init__(self, companies, **kwargs)
		self.actions = ['chart','stats']
		self.action_keys = {'chart': ['date','high','low','volume','changePercent','open','close'],'stats': ['marketcap','beta','week52high','week52low','week52change','shortInterest','shortDate','float','consensusEPS','day200MovingAvg','day50MovingAvg','institutionPercent','insiderPercent','shortRatio','month6ChangePercent','month3ChangePercent','month1ChangePercent','day5ChangePercent']}	
		self.average_keys = ['close','change','spread','volume']
		self.periods = [5,10,20]
	
	def process_action(self, result, company, action, daily = {}):
		if action == 'chart':
			num_days = len(result['date'])
			for i in range(num_days):
				daily[i] = {'date': result['date'][i], 'open': round(result['open'][i],2), 'close': round(result['close'][i],2), 'change': round(result['changePercent'][i],2), 'high': round(result['high'][i],2), 'low': round(result['low'][i],2), 'spread': round((round(result['high'][i],2)-round(result['low'][i],2)),2), 'volume': result['volume'][i]}
			daily = sorted(daily.items())
			for period in self.periods:
				temp = {}
				vals = dict.fromkeys(self.average_keys,0)
				i = num_days - period
				while i <= (num_days - 1):
					temp[i] = daily[i]
					i+=1
				for k in temp.keys():
					for j in range(len(self.average_keys)):
						vals[self.average_keys[j]] += temp[k][1][self.average_keys[j]]
				for key in vals.keys():
					vals[key] = round((vals[key]/period),2)
				for key in self.average_keys:
					self.data[company][action].append(str(period) + 'Day' + key + ',' + str(vals[key]))
		else:
			for key in sorted(result):
				value = result[key]
				if type(value) == float:
					value = round(value,2)	
				self.data[company][action].append(str(key) + ',' + str(value))


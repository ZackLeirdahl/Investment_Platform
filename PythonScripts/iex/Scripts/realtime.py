from task import BaseTask

class Realtime(BaseTask):
	def __init__(self, companies, **kwargs):
		BaseTask.__init__(self, companies, **kwargs)
		self.actions = ['chart//1d']
		self.action_keys = {'chart//1d': ['minute','volume','changeOverTime','high','low','average','marketNumberOfTrades']}
			
	def process_action(self, result, company, action):
		for i in range(len(result['minute'])):
			try:
				minute = str(result['minute'][i])
				high = str(round(result['high'][i],2))	
				low = str(round(result['low'][i],2))
				average = str(round(result['average'][i],2))
				trades = str(result['marketNumberOfTrades'][i])
				change = str(round(result['changeOverTime'][i],3))
				volume = str(result['volume'][i])
				self.data[company][action].append(','.join([minute,high,low,average,change,trades,volume]))
			except:
				continue
		

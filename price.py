import json
from task import BaseTask
from urllib import request

class CurrentPrice(BaseTask):
	def __init__(self, companies, **kwargs):
		BaseTask.__init__(self, companies, **kwargs)
		self.actions = ['price']
	
	def process_company(self, company):
		self.data[company] = dict.fromkeys(self.actions,[])
		for action in self.actions:
			raw = request.urlopen(self.requests[company][action]).read().decode('utf-8')
			self.data[company][action].append(str(json.loads(raw)))
		
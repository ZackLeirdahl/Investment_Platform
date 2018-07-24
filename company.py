from task import BaseTask

class Company(BaseTask):
	def __init__(self, companies, **kwargs):
		BaseTask.__init__(self, companies, **kwargs)
		self.actions = ['company']
		self.action_keys = {'company': ['symbol','companyName','exchange','industry','description','sector']}
	
	def process_action(self, result, company, action):
		for key in sorted(result):
			value = result[key].replace(',','|').strip()
			self.data[company][action].append(str(key) + ',' + str(value))
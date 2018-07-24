import os
from request import RequestHub

class BaseTask:
	def __init__(self, companies, **kwargs):
		self.hub = RequestHub()
		self.data = {}
		self.companies = companies
		self.actions = None
		self.action_keys = None
		self.requests = None
		try:
			self.output_root = kwargs['output_root']
		except:
			self.output_root = ''
		try:
			self.header_line = ','.join(kwargs['header_fields'])
		except:
			self.header_line = None
		try:
			self.suffix = '_' + kwargs['file_suffix'] + '.csv'
		except:
			self.suffix = '_default.csv'
		
	def run(self):
		self.requests = self.hub.get_requests(self.companies,self.actions)
		for company in self.companies:
			self.process_company(company)
		self.write_data()
	
	def process_company(self, company):
		self.data[company] = dict.fromkeys(self.actions,[])
		for action in self.actions:
			self.process_action(self.hub.get_result(action, self.action_keys[action], self.requests[company][action]), company, action)
	
	def process_action(self):
		raise NotImplementedError('This method must be implemented in a child class.')
	
	def write_data(self):	
		for company in self.companies:
			for action in self.actions:
				self.hub.write_results(self.data[company][action], os.path.join(self.output_root, company + self.suffix), self.header_line)
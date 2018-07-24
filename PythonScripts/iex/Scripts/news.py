from task import BaseTask

class News(BaseTask):
	def __init__(self, companies, **kwargs):
		BaseTask.__init__(self, companies, **kwargs)
		self.actions = ['news//last//5']
		self.action_keys = {'news//last//5': ['datetime','headline','source','url','summary']}
			
	def process_action(self, result, company, action):
		for i in range(len(result['datetime'])):
			date = str(result['datetime'][i])[:10]
			headline = str(result['headline'][i]).replace(',','|').replace('  ',' ').strip()
			source = str(result['source'][i])
			url = str(result['url'][i])
			summary = str(result['summary'][i]).replace(',','|').replace('  ',' ').strip()
			self.data[company][action].append(','.join([date,headline,source,url,summary]))
		

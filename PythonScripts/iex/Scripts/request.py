import json
from urllib import request

class RequestHub:
	def __init__(self):
		self.url = 'https://api.iextrading.com/1.0/stock'
		
	def get_requests(self, symbols, actions):
		requests = dict.fromkeys(symbols)
		for sym in symbols:
			company = dict.fromkeys(actions)
			for action in actions:
				company[action] = '/'.join([self.url,sym,action])
			requests[sym] = company
		return requests
	
	def get_result(self, action, action_keys, url):
		raw = request.urlopen(url).read().decode('utf-8')
		data = json.loads(raw)
		result = dict.fromkeys(action_keys)
		if type(data) != list:
			for key in action_keys:
				if key in data.keys():
					result[key] = data[key]
		else:
			for record in data:
				for key in action_keys:
					if key in record.keys():
						if result[key] == None:
							result[key] = [record[key]]
						else:
							result[key].append(record[key])
		return result
	
	def write_results(self, results, output_file, header = None):
		with open(output_file, 'w') as wf:
			if header != None:
				wf.write(header + '\n')
			for line in results:
				wf.write(line + '\n')
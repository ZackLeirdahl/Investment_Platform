from urllib import request
import re
import xml.etree.ElementTree as ET
class scraper:
	def __init__(self, args):
		self.url = args[0]
		self.data = args[1]
		self.master = args[2]
		self.root = args[3]
		self.tags = args[4]
		self.rootNode = args[5]
		
	def scrape(self):
		page = request.urlopen(self.url)
		valid = False
		data = ''
		while not valid:
			htmltext = page.readline()
			line = htmltext.decode()
			if line == '':
				valid = True
			data = data + line
		self.data = data
		self.root = ET.fromstring(self.data)
		
	def parseText(self, rootNode):
		master = []
		for r in self.root.iter(rootNode):
			master.append(r.attrib)
		return master

				

		

	
from urllib import request
import re
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

class scraper:
	def __init__(self, url):
		self.url = url
		
	def scrape(self):
		page = request.urlopen(self.url)
		valid = False
		data = ''
		while not valid:
			text = page.readline()
			line = text.decode()
			if line == '':
				valid = True
			data = data + line
		self.data = data
		return data

class xmlScraper:
	def __init__(self, data, tags, rootNode):
		self.data = data
		self.root = ET.fromstring(self.data)
		self.master = []
		self.tags = tags
		self.rootNode = rootNode
		
	def getNodeTags(self):
		root = self.root.findall('.//'+self.rootNode+'//')
		for r in root:
			self.tags.append(r.tag)
		self.tags = list(set(self.tags))
		return self.tags

	def parseText(self):
		for r in self.root.iter(self.rootNode):
			record = []
			for t in r.itertext():
				record.append(t)
			self.master.append(record)
		return self.master
	
	def parseAttrib(self, rootNode):
		for r in self.root.iter(rootNode):
			self.master.append(r.attrib)
		return self.master
	
	def removeRecords(self, searchList):
		tempMaster = []
		for i in range(len(self.master)):
			flag = False
			record = str(self.master[i])
			for j in range(len(searchList)):
				if re.search(searchList[j],record) != None:
					flag = True
			if not flag:
				tempMaster.append(record)
		self.master = tempMaster
		return self.master

	def writeFile(self, fName):
		ofile = open(fName,'w')
		for i in range(len(self.master)):
			line = ''.join(str(self.master[i])).replace('[','').replace(']','').replace("'",'')
			ofile.write(line + '\n')
		ofile.close()

class htmlScraper(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print('This is a start tag and attributes',tag, attrs)
	def handle_endtag(self, tag):
		print('This is an end tag',tag)
  	
	def handle_data(self, data):
		print('This is the data',data)
	
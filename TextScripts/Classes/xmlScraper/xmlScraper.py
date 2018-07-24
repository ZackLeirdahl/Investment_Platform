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
		return data
		
	def getAllTags(self):
		tags = []
		for elem in self.root.iter():
			 tags.append(elem.tag)
		self.tags = list(set(tags))
	
	def getNodeTags(self, rootNode):
		self.rootNode = rootNode
		root = self.root.findall('.//'+rootNode+'//')
		print(root)
		tags = []
		for r in root:
			tags.append(r.tag)
		self.tags = list(set(tags))
		
	def parseText(self):
		master = []
		for r in self.root.iter():
			record = []
			for t in r.itertext():
				record.append(t)
			master.append(record)
		self.master = master
		
	def parseAttrib(self, rootNode):
		master = []
		for r in self.root.iter(rootNode):
			master.append(r.attrib)
		self.master = master
	
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
	
	def writeFile(self, fName):
		ofile = open(fName,'w')
		for i in range(len(self.master)):
			line = ''.join(str(self.master[i])).replace('[','').replace(']','').replace("'",'')
			ofile.write(line + '\n')
		ofile.close()
				

		

	
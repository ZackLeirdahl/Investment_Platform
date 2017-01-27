from urllib import request
import re
import time
import xml.etree.ElementTree as ET

def scrape(args):
	page = request.urlopen('http://service.dice.com/api/rest/jobsearch/v1/simple.xml?text='+args[0]+'&sort=2&age=14&direct=1&areacode='+args[1]+'&skill='+args[2]+'&pgcnt='+args[3]+'&page=1')
	valid = False
	data = ''
	while not valid:
		htmltext = page.readline()
		line = htmltext.decode()
		if line == '':
			valid = True
		data = data + line
	return data

def parse(data):
	root = ET.fromstring(data)
	i = 1
	master = []
	for result in root.iter('resultItem'):
		 a = result.find('detailUrl').text
		 b = result.find('jobTitle').text
		 c = result.find('company').text
		 d = result.find('location').text
		 e = result.find('date').text
		 entry = [str(i),a,b,c,d,e]
		 master.append(entry)
		 i +=1
	return master

def initialize():
	areaCode = '55414'
	skill = ['T-SQL','python','C#']
	text = ['intelligence','analyst','analytics']
	pgcnt = '100'
	args = [text[1],areaCode,skill[1],pgcnt]
	data = scrape(args)
	result = parse(data)
	print(result)
initialize()

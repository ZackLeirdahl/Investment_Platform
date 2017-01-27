from urllib import request
import re
import time
partnerID = '118182'
key = 'embO2VNgeLo'
page = request.urlopen('http://api.glassdoor.com/api/api.htm?v=1&format=xml&t.p='+partnerID+'&t.k='+key+'&userip=&useragent=&action=jobs-stats')
valid = False
data = ''
while not valid:
	htmltext = page.readline()
	line = htmltext.decode()
	if line == '':
		valid = True
	data = data + line
print(data)
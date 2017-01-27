from urllib import request
import re
import time

def scrape(a,b,d,e):
	symbols = ['AAPL','MTCH','CELG','XOM','GD','CAKE','BAC','LRCX','PANW','FB','IBM','NVDA','MSFT','MBLY','GE','UNH','FIT','TSLA','F']
	master= []
	for i in range(len(symbols)):
		s = symbols[i]
		page = request.urlopen('https://ichart.finance.yahoo.com/table.csv?d='+d+'&e='+e+'&f=2017&a='+a+'&b='+b+'&c=2017&ignore=.csv&s='+s)
		valid = False
		data = ''
		while not valid:
			htmltext = page.readline()
			line = htmltext.decode()
			if line == '':
				valid = True
			data = data + line
		data = data.replace('Date,Open,High,Low,Close,Volume,Adj Close\n','')
		master.append(s + ',' + data)
	return master

def writeFile(data):
	date = time.strftime('%d:%m')
	fname = 'stockdata.txt'
	ofile = open(fname,'w')
	ofile.write('Symbol,Date,Open,High,Low,Close,Volume,Adj Close')
	ofile.write('\n')
	for i in range(len(data)):
		ofile.write(str(data[i]))
	ofile.close()
	
def initialize():
	d = str(int(time.strftime('%m'))-1)
	e = str(int(time.strftime('%d')))
	if (e =='30' and d in ('5','7','10','12')) or (e == '28' and d == '3') or e == '31':
		a = d - 1
		if d in ('5', '7','10','12'):
			b = '30'
		elif d == '3':
			b = '28'
		else:
			b == '31'
	else:
		a = d
		b = str(int(e)- 1)
	data = scrape(a,b,d,e)
	writeFile(data)
	
initialize()

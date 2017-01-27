from urllib import request

page = request.urlopen('https://api.sportradar.us/nba-t3/league/hierarchy.xml?api_key=n62whvrs4yg3qrp55vayfew5')

valid = False
data = ''
while not valid:
	htmltext = page.readline()
	line = htmltext.decode()
	if line == '':
		valid = True
	print(line)
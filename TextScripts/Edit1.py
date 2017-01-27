from urllib import request
from html import parser
url = 'http://www.databasebasketball.com/teams/teamyear.htm?tm=MIN&lg=n&yr=2010'
page = request.urlopen(url)
valid = False
data = ''
parsed = parser.HTMLParser()
while not valid:
	htmltext = page.readline()
	line = htmltext.decode()
	line = parsed.handle_starttag('p',[''])
	if line == '':
		valid = True
	data = data + line
print(data)



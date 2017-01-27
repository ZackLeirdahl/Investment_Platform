from urllib import request
page = request.urlopen('https://api.login.yahoo.com/oauth/v2/get_request_token')
htmltext = page.readline()
line = htmltext.decode()
print(line)

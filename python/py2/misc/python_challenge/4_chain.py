# import urllib.request
# url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
# data = urllib.request.urlopen(url + '37278').read().decode('utf-8')
# while data.startswith('and'):
#     print(data)
#     data = urllib.request.urlopen(url + data.split(' ')[-1]).read().decode('utf-8')
# print(data)
# peak.html


import requests
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
num = '63579'
while True:
	text = requests.get(url + num).text
	print(text)
	if text.startswith('and'):		# and the next nothing is 53548
		num = text.split()[-1]
	else:
		break

# initail num = 12345
# hint1: <font color=red>Your hands are getting tired </font>and the next nothing is 94485
# hint2: and the next nothing is 16044
#		 Yes. Divide by two and keep going.
# hint3: There maybe misleading numbers in the
#		 text. One example is 82683. Look only for the next nothing and the next nothing is 63579
# hint4: peak.html
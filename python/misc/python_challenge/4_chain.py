import urllib.request
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
data = urllib.request.urlopen(url + '37278').read().decode('utf-8')
while data.startswith('and'):
    print(data)
    data = urllib.request.urlopen(url + data.split(' ')[-1]).read().decode('utf-8')
print(data)
# peak.html

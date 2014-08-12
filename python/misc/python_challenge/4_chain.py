import urllib.request
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
data = urllib.request.urlopen(url + '12345').read().decode('utf-8')
while data.isdigit():
    print(data)
    data = urllib.request.urlopen(url + str(data)).read().decode('utf-8')
print(data) 

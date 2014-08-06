import urllib.request
url = 'http://fun.coolshell.cn/n/'
data = urllib.request.urlopen(url + '2014').read().decode('utf-8')
while data.isdigit():
    print(data)
    data = urllib.request.urlopen(url + str(data)).read().decode('utf-8')
print(data)     # Cool! the next level is "tree"

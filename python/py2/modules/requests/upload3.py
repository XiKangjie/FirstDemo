import requests

with open('test.cfg', 'rb') as f:
    r = requests.post('http://localhost:9000/upload', data=f)
print r.text

#encoding:utf-8
import json

data = {'name': '中文'}

with open("chinese.json", mode="w") as f:
    json.dump(data, f)

with open("chinese.json") as f:
    data = json.load(f)
print data['name']


import json

data = {'a': 'A', 'c': 3.0, 'b': (2, 4), 'd': [1, 2.0, "3", True]}

with open("data.json", mode="w") as f:
    json.dump(data, f)

with open("data.json") as f:
    data = json.load(f)
print data['b']
print data['d']

"""

[2, 4]
[1, 2.0, u'3', True]

"""


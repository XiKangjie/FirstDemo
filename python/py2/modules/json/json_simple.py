import json

data = {'a': 'A', 'c': 3.0, 'b': (2, 4, 'a', True)}
print "data: ", data

# dump string
data_string = json.dumps(data)
print "encoded: ", data_string
# load string
print "decoded: ", json.loads(data_string)

print "sort: ", json.dumps(data, sort_keys=True)
print "indent: ", json.dumps(data, sort_keys=True, indent = 4)


"""
data:  {'a': 'A', 'c': 3.0, 'b': (2, 4, 'a', True)}
encoded:  {"a": "A", "c": 3.0, "b": [2, 4, "a", true]}
decoded:  {u'a': u'A', u'c': 3.0, u'b': [2, 4, u'a', True]}
sort:  {"a": "A", "b": [2, 4, "a", true], "c": 3.0}
indent:  {
    "a": "A", 
    "b": [
        2, 
        4, 
        "a", 
        true
    ], 
    "c": 3.0
}

"""

import shelve

s = shelve.open('test_shelf')
try:
    existing = s['key1']
finally:
    s.close()

print(existing)

# {'int': 10, 'float': 3.4, 'string': 'sample data'}

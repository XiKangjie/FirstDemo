import shelve

s = shelve.open('test_shelf')
try:
    s['key1'] = {'int':10, 'float':3.4, 'string':'sample data'}
finally:
    s.close()

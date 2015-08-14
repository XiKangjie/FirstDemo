# All section and option names are treated as strings, but option values can be
# strings, integers, floating point numbers, or booleans. There are a range of
# possible boolean values that are converted true or false.

# get() always returns a string. Use getint() for integers, getfloat() for
# floating point numbers, and getboolean() for boolean values.


from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('types.ini')

print 'Integers:'
for name in parser.options('ints'):
    string_value = parser.get('ints', name)
    value = parser.getint('ints', name)
    print '  %-12s : %-7r -> %d' % (name, string_value, value)

print '\nFloats:'
for name in parser.options('floats'):
    string_value = parser.get('floats', name)
    value = parser.getfloat('floats', name)
    print '  %-12s : %-7r -> %0.2f' % (name, string_value, value)

print '\nBooleans:'
for name in parser.options('booleans'):
    string_value = parser.get('booleans', name)
    value = parser.getboolean('booleans', name)
    print '  %-12s : %-7r -> %s' % (name, string_value, value)

"""
Integers:
  negative     : '-5'    -> -5
  positive     : '1'     -> 1

Floats:
  negative     : '-3.14' -> -3.14
  positive     : '0.2'   -> 0.20

Booleans:
  tf_true      : 'true'  -> True
  yn_true      : 'yes'   -> True
  number_false : '0'     -> False
  yn_false     : 'no'    -> False
  onoff_true   : 'on'    -> True
  number_true  : '1'     -> True
  onoff_false  : 'off'   -> False
  tf_false     : 'false' -> False
"""

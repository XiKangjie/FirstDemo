from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('simple.ini')
for name, value in parser.items('UPPERCASE'):
    print '%s=%s' % (name, value)

parser2 = SafeConfigParser()
parser2.optionxform = str
parser2.read('simple.ini')
for name, value in parser2.items('UPPERCASE'):
    print '%s=%s' % (name, value)

with open('simple_write.ini', 'w') as f:
    parser2.write(f)

from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('simple.ini')

for section_name in parser.sections():
    print 'Section:', section_name
    print '  Options:', parser.options(section_name)
    for name, value in parser.items(section_name):
        print '  %s = %s' % (name, value)

"""
Section: bug_tracker
  Options: ['url', 'username', 'password']
  url = http://localhost:8080/bugs/
  username = dhellmann
  password = SECRET
Section: wiki
  Options: ['url', 'username', 'password']
  url = http://localhost:8080/wiki/
  username = dhellmann
  password = SECRET
"""

print parser.has_section('bug_tracker')
# True

print parser.has_option('wiki', 'username')
# True

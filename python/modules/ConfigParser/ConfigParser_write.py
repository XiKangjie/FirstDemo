import ConfigParser
import sys

parser = ConfigParser.SafeConfigParser()

# add_section() create a new section
parser.add_section('bug_tracker')
# set() add or change an option
parser.set('bug_tracker', 'url', 'http://localhost:8080/bugs')
parser.set('bug_tracker', 'username', 'dhellmann')
parser.set('bug_tracker', 'password', 'secret')

parser.write(sys.stdout)

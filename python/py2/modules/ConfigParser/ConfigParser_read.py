# Configuration file consists of one or more named sections, each of which can
#contain individual options with names and values.

# Config file sections are identified by looking for lines starting with
# [ and ending with ]. The value between the square brackets is the section
# name, and can contain any characters except square brackets.

# Options are listed one per line within a section. The line starts with
# the name of the option, which is separated from the value by a colon (:)
# or equal sign (=). Whitespace around the separator is ignored when the file is parsed.

from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('simple.ini')
print parser.get('bug_tracker', 'url')

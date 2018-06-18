#!/usr/bin/env python

import optparse

parser = optparse.OptionParser(usage='%prog [optoins] <arg1> <arg2> [<arg3>...]',
                               prog='my_program_name', version='1.0')

# The default processing action for options is to store the value using the
# name given in the dest argument to add_option()
parser.add_option('-a', action='store_true', default=False, help='help a')
# optparse will convert option values from strings to type int.
parser.add_option('-b', action='store', dest='b', type='int', help='help b')
parser.add_option('--ccc', action='store', dest='c', help='help ccc')
parser.add_option('-d', type='choice', choices=['x', 'y'], help='help d')

# The return value from parse_args() is a two-part tuple containing an Valures instance
# and the list of arguments to the command that were not interpreted as options.
options, remainder = parser.parse_args()

print 'options:', options
print 'remainder:', remainder


"""
consen@dev:~/.../library/optparse$ python example.py -h
Usage: my_program_name [optoins] <arg1> <arg2> [<arg3>...]

Options:
  --version   show program's version number and exit
  -h, --help  show this help message and exit
  -a          help a
  -b B        help b
  --ccc=C     help ccc
  -d D        help d



consen@dev:~/.../library/optparse$ python example.py -a -b1 --ccc what other -d x
options: {'a': True, 'c': 'what', 'b': 1, 'd': 'x'}
remainder: ['other']

"""

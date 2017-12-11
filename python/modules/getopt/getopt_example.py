import getopt
import sys

version = '1.0'
verbose = False
output_filename = 'default.out'

print('ARGV     :', sys.argv[1:])

options, remainder = getopt.getopt(
        sys.argv[1:],
        'o:v',
        ['output=', 'verbose', 'version=']
)

print('OPTIONS  :', options)

for opt, arg in options:
    if opt in ('-o', '--output'):
        output_filename = arg
    elif opt in ('-v', '--verbose'):
        verbose = True
    elif opt == '--version':
        version = arg

print('VERSION  :', version)
print('VERBOSE  :', verbose)
print('OUTPUT   :', output_filename)
print('REMAINING:', remainder)

'''
python getopt_example.py -o foo
python getopt_example.py -ofoo
python getopt_example.py --output foo
python getopt_example.py --output=foo

ARGV      : ['--output=foo']
OPTIONS   : [('--output', 'foo')]
VERSION   : 1.0
VERBOSE   : False
OUTPUT    : foo
REMAINING : []
'''

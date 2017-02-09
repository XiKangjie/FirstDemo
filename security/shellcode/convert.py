import sys

if len(sys.argv) < 2:
    print 'Usage: python %s filename' % sys.argv[0]
    sys.exit(0)

with open(sys.argv[1], 'rb') as f:
    shellcode = ''
    for line in f:
        for c in line:
            shellcode += '\\x' + c.encode('hex')
    print shellcode

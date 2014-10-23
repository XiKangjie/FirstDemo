import sys

''' Interpreter Settings '''

# build-time version information
print sys.version
print sys.version_info
# 2.7.6 (default, Mar 22 2014, 23:03:14)
# [GCC 4.8.2]
# sys.version_info(major=2, minor=7, micro=6, releaselevel='final', serial=0)

# install location
print sys.executable
print sys.prefix
# /usr/bin/python
# /usr

# command line options
print sys.flags.tabcheck
# 0

''' Runtime Environment '''

# command line arguments
print sys.argv
# ['sys_example.py']

# input and output streams
print sys.stdout
# <open file '<stdout>', mode 'w' at 0xb748b078>

''' Memory Management and Limits '''

# reference counts
one = []
print sys.getrefcount(one)          # 2

# object size
print sys.getsizeof(one)            # 32

# recursion
print sys.getrecursionlimit()       # 1000

# maximum values
print sys.maxint                    # 2147483647
print sys.maxsize                   # 2147483647
print sys.maxunicode                # 1114111

# floating point values
print sys.float_info.epsilon        # 2.22044604925e
print sys.float_info.dig            # 15
print sys.float_info.mant_dig       # 53

# byte ordering
print sys.byteorder                 # little

#!/usr/bin/env python
'''
https://blog.holbertonschool.com/hack-the-virtual-memory-python-bytes/

Prints:
- the address of the bytes object
- a b"string" (bytes object)
- information about the bytes object
And then:
- reads a char from stdin
- prints the same (or not :)) information again
'''

import sys
import ctypes

lib = ctypes.CDLL('./libbytes.so')
lib.print_python_bytes.argtypes = [ctypes.py_object]

s = b"Holberton"
print(hex(id(s)))
print(s)
lib.print_python_bytes(s)

sys.stdin.read(1)

print(hex(id(s)))
print(s)
lib.print_python_bytes(s)

from ctypes import *

libadd = cdll.LoadLibrary("./libadd.so")

print libadd.add(1, 1)

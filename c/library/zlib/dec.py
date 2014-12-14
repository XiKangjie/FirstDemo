import zlib
import struct

with open("zlib_simple.z") as f:
    data = f.read()
    dedata = zlib.decompress(data)
    print len(dedata)
    print dedata 
    s = struct.Struct('I4sI8s')
    print s.unpack(dedata)

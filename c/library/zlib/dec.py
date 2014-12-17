import zlib
import struct

with open("zlib_simple.z") as f:
    print f.read(4)
    #size = int(f.read(4))
    #print size
    #data = f.read(size)
    #dedata = zlib.decompress(data)
    #print len(dedata)
    #s = struct.Struct('I4sI8s')
    #print s.unpack(dedata)

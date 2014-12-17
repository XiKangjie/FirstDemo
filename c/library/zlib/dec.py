import zlib
import struct

with open("zlib_simple.z", "rb") as f:
    bsize = f.read(4)
    size, = struct.unpack('I', bsize)
    print size
    data = f.read(size)
    dedata = zlib.decompress(data)
    print struct.unpack('I4sI8s', dedata)

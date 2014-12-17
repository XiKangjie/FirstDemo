# The in-memory approach has obvious drawbacks that make it impractical for
# real-world use cases. The alternative is to use Compress and Decompress objects
# to manipulate streams of data, so that the entire data set does not have to
# fit into memory.

import zlib
try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO


BLOCK_SIZE = 4


compressor = zlib.compressobj()
with open('data.txt', 'rb') as reader, open('compressed.z', 'w') as writer:
    while True:
        block = reader.read(BLOCK_SIZE)
        if block:
            print 'block:', block
        else:
            break
        compressed = compressor.compress(block)
        if compressed:
            writer.write(compressed)
    # write and data being buffered by the compressor
    remaining = compressor.flush()
    writer.write(remaining)

    writer.write(zlib.compress("blabla"))


decompressor = zlib.decompressobj()
buffer = StringIO()
with open('compressed.z') as f:
    while True:
        block = f.read(BLOCK_SIZE)
        if block:
            decompressed = decompressor.decompress(block)
            buffer.write(decompressed)
            print "decompressed:", decompressed
            if decompressor.unused_data:
                print "unused_data:", decompressor.unused_data
                break
        else:
            break
    # deal with data remaining inside the decompressor buffer
    remaining = decompressor.flush()
    buffer.write(remaining)
    print "remaining:", remaining
    
    print 'buffer:', buffer.getvalue()


"""
block: hell
block: o zl
block: ib

decompressed: h
decompressed: ello
decompressed:  zli
decompressed: b

decompressed:
unused_data: x
remaining:
buffer: hello zlib

"""

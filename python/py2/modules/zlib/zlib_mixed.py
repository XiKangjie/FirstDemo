# The Decompress class returned by decompressobj() can also be used in situations
# where compressed and uncompressed data is mixed together.
import zlib

data = "hello" * 5
compressed = zlib.compress(data)
combined = compressed + "world"

decompressor = zlib.decompressobj()
decompressed = decompressor.decompress(combined)

print 'Decompressed: ', decompressed
print 'Unused data: ', decompressor.unused_data

"""
Decompressed:  hellohellohellohellohello
Unused data:  world
"""

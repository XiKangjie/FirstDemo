# The simplest way to work with zlib requires holding all of the data to be compressed
# or decompressed in memory.

import zlib

original_data = 'This is the original text.'
print 'Original: ', len(original_data), original_data

compressed = zlib.compress(original_data)
print 'Compressed: ', len(compressed), compressed

decompressed = zlib.decompress(compressed)
print 'Decompressed: ', len(decompressed), decompressed

#!/usr/bin/env python

import umsgpack

packed = umsgpack.packb({u'compact': True, u'schema': 0})
unpacked = umsgpack.unpackb(packed)
print packed
print unpacked


with open('test.bin', 'w') as f:
    umsgpack.pack({u'compact': True, u'schema': 0}, f)
    umsgpack.pack([1, 2, 3], f)

with open('test.bin') as f:
    print umsgpack.unpack(f)
    print umsgpack.unpack(f)

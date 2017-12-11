#!/usr/bin/env python

import hashlib

data = 'hi'

h = hashlib.md5()
h.update(data)
print h.hexdigest()

print hashlib.md5(data).hexdigest()


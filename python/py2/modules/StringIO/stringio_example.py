# StringIO provides a conveninet means of working with text in memory using the
# file API (read, write, ext.).


# Find the best implementation available on this platform
try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO

# Writing to a buffer
output = StringIO()
output.write('This goes into the buffer.')
print >>output, 'And so does this.'

# Retrive the value written
#output.seek(0)
#print output.read(4)
print output.getvalue()

# discard buffer memory
output.close()

# Initialize a read buffer
input = StringIO('Initial value for read buffer')
# Read from the buffer
print input.read(5)
print input.read()


"""
This goes into the buffer.And so does this.

Initi
al value for read buffer
"""

from humanfriendly import format_size, parse_size

print format_size(100)
print format_size(1024)
print format_size(1024 * 1024)
print format_size(1024 * 1024 * 1024)
print format_size(10241892347)

"""
100 bytes
1 KB
1 MB
1 GB
9.54 GB
"""

print parse_size('100 bytes')
print parse_size('1 KB')
print parse_size('1kb')
print parse_size('1 MB')

"""
100
1024
1024
1048576
"""

from humanfriendly import format_timespan, parse_timespan

print format_timespan(12)
print format_timespan(1209)
print format_timespan(234451)

"""
12 seconds
20 minutes and 9 seconds
2 days, 17 hours and 7 minutes
"""

print parse_timespan('1s')
print parse_timespan('1m')
print parse_timespan('1h')
print parse_timespan('1d')
print parse_timespan('1y')

"""
1.0
60.0
3600.0
86400.0
31449600.0
"""

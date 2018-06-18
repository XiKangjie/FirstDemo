import profile
import pstats
from profile_fibonacci_memoized import fib, fib_seq

# Read all 5 stats files into a single object
stats = pstats.Stats('profile_stats_0.stats')
for i in range(1, 5):
    stats.add('profile_stats_%d.stats' % i)
stats.strip_dirs()
stats.sort_stats('cumulative')

print 'INCOMING CALLERS:'
stats.print_callers('\(fib')

print 'OUTGOING CALLEES:'
stats.print_callees('\(fib')

"""
INCOMING CALLERS:
   Ordered by: cumulative time
   List reduced from 13 to 2 due to restriction <'\\(fib'>

Function                                   was called by...
profile_fibonacci_memoized.py:26(fib_seq)  <- <string>:1(<module>)(5)    0.006
                                              profile_fibonacci_memoized.py:26(fib_seq)(100)    0.006
profile_fibonacci_memoized.py:16(fib)      <- profile_fibonacci_memoized.py:9(__call__)(21)    0.003


OUTGOING CALLEES:
   Ordered by: cumulative time
   List reduced from 13 to 2 due to restriction <'\\(fib'>

Function                                   called...
profile_fibonacci_memoized.py:26(fib_seq)  -> :0(append)(105)    0.001
                                              :0(extend)(100)    0.000
                                              profile_fibonacci_memoized.py:9(__call__)(105)    0.003
                                              profile_fibonacci_memoized.py:26(fib_seq)(100)    0.006
profile_fibonacci_memoized.py:16(fib)      -> profile_fibonacci_memoized.py:9(__call__)(38)    0.003

"""

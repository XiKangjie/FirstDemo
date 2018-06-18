import profile

def fib(n):
    # from http://en.literateprograms.org/Fibonacci_numbers_(Python)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_seq(n):
    seq = [ ]
    if n > 0:
        seq.extend(fib_seq(n-1))
    seq.append(fib(n))
    return seq

print 'RAW'
print '=' * 80
# run() takes a string statement as argument, and creates a report of
# the time spent executing different lines of code while running the statement.
profile.run('print fib_seq(20); print')

#  Since there are only 66 primitive calls, we know that the vast majority of those 57k calls were recursive. 
"""
RAW
================================================================================
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

         57356 function calls (66 primitive calls) in 0.438 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       21    0.000    0.000    0.000    0.000 :0(append)
       20    0.000    0.000    0.000    0.000 :0(extend)
        1    0.001    0.001    0.001    0.001 :0(setprofile)
        1    0.000    0.000    0.437    0.437 <string>:1(<module>)
        1    0.000    0.000    0.438    0.438 profile:0(print fib_seq(20); print)
        0    0.000             0.000          profile:0(profiler)
     21/1    0.002    0.000    0.437    0.437 profile_fibonacci_raw.py:12(fib_seq)
 57291/21    0.435    0.000    0.435    0.021 profile_fibonacci_raw.py:3(fib)

"""


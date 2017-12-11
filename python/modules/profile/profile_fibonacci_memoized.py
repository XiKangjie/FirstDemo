import profile

class memoize:
    # from http://avinashv.net/2008/04/python-decorators-syntactic-sugar/
    def __init__(self, function):
        self.function = function
        self.memoized = {}

    def __call__(self, *args):
        try:
            return self.memoized[args]
        except KeyError:
            self.memoized[args] = self.function(*args)
            return self.memoized[args]

@memoize
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

if __name__ == '__main__':
    print 'MEMOIZED'
    print '=' * 80
    profile.run('print fib_seq(20); print')

"""
MEMOIZED
================================================================================
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

         145 function calls (87 primitive calls) in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       21    0.000    0.000    0.000    0.000 :0(append)
       20    0.001    0.000    0.001    0.000 :0(extend)
        1    0.000    0.000    0.000    0.000 :0(setprofile)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.001    0.001 profile:0(print fib_seq(20); print)
        0    0.000             0.000          profile:0(profiler)
       21    0.000    0.000    0.000    0.000 profile_fibonacci_memoized.py:16(fib)
     21/1    0.000    0.000    0.001    0.001 profile_fibonacci_memoized.py:26(fib_seq)
    59/21    0.000    0.000    0.000    0.000 profile_fibonacci_memoized.py:9(__call__)

"""

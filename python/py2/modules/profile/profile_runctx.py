import profile
from profile_fibonacci_memoized import fib, fib_seq

# Sometimes, instead of constructing a complex expression for run(),
# it is easier to build a simple expression and pass it parameters
# through a context, using runctx()

if __name__ == '__main__':
    profile.runctx('print fib_seq(n); print', globals(), {'n':20})

# Decorators provide a very powerful way to alter the behavior of a function
# without redifining it.

from functools import wraps


# let the logging decorator to log the calls made to the function it decorateds
def logging(fun):
    # wraps decorator does some magic to ensure that aux behaves as closely as
    # possible to fun.
    @wraps(fun)
    def aux(*args, **kwargs):
        print "Calling", fun.__name__
        return fun(*args, **kwargs)
    return aux


# f has been decorated with logging, logging must be a function taking another
# function as an argument.
@logging
def f(x):
    return x + 1

print f(3)          # 4
print f.__name__    # f

# A common example which is often used to illustrate decorators in Python is
# memoization: when a function is computation-heavy but often called using the
# same arguments, you can save a lot of time by caching past results returned by
# the function


def memoize(fun):
    cache = {}

    @wraps(fun)
    def aux(x):
        if x in cache:
            return cache[x]
        else:
            a = fun(x)
            cache[x] = a
            return a
    return aux


@memoize
def f(x):
    return x + 1

print f(1)  # 2
print f(1)  # 2

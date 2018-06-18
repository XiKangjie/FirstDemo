# Generators provide an easy way to create iterator objects (objects over which
# you can iterate)

# Generators expressions

l = [1, 2, 3]
# the elements in m are generated on the go when needed:
# only when trying to iterate over the variable m are the elements generated.
# one at a time, save memory.
m = (i * i for i in l)
print sum(m)

# A second way to define a generator is by writing a function using the special
# keyword yield. on each iteration step, the function is executed until a yield
# instruction is hit, the value following the yield keyword is returned and can
# be used during the iteration step.


def min_max(filename):
    with open(filename) as f:
        for line in f:
            l = map(int, line.split())
            yield min(l), max(l)

for (inf, sup) in min_max("./num.txt"):
    print (inf + sup) / 2

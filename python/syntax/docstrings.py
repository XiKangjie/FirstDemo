'''
Module documentation
Words Go Here

python -m pydoc -b
python -m pydoc docstrings
python -m pydoc -w docstrings
'''

spam = 40

def square(x):
    '''
    function documentation
    can we have you liver then?
    '''
    return x ** 2   # square

class Employee:
    'class documentation'
    pass

print(square(4))
print(square.__doc__)

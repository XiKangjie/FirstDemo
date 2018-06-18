class Student(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # read only
    @property
    def full_name(self):
        return self.first_name + self.last_name

s = Student('he', 'he')
print s.full_name
s.full_name = 'heihei'      # AttributeError: can't set attribute
print s.full_name

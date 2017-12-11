# -*- coding: utf-8 -*-
import os.path

# Parsing Paths
for path in ['/one/two/three',
             '/one/two/three/',
             '/',
             '.',
             '']:
    print path, ' : ', os.path.split(path)

'''
/one/two/three  :  ('/one/two', 'three')
/one/two/three/  :  ('/one/two/three', '')
/  :  ('/', '')
.  :  ('', '.')
  :  ('', '')
''' 
# basename() returns a value equivalent to the second part of the split() value.
# dirname() returns the first part of the split path.
for path in ['/one/two/three',
             '/one/two/three/',
             '/',
             '.',
             '']:
    print path, ' : ', os.path.basename(path)
'''
/one/two/three  :  three
/one/two/three/  :  
/  :  
.  :  .
  :  
'''
for path in ['/one/two/three',
             '/one/two/three/',
             '/',
             '.',
             '']:
    print path, ' : ', os.path.dirname(path)
'''
/one/two/three  :  /one/two
/one/two/three/  :  /one/two/three
/  :  /
.  :  
  :  
'''

# Building Paths

# if a component is an absolute path, all previous components are thrown away and
# joining continues from the absolute path
for parts in [('one', 'two', 'three'),
              ('/', 'one', 'two', 'three'),
              ('/one', '/two', '/three')]:
    print parts, ' : ', os.path.join(*parts)
'''
('one', 'two', 'three')  :  one/two/three
('/', 'one', 'two', 'three')  :  /one/two/three
('/one', '/two', '/three')  :  /three
'''

# Testing Files
f = os.path.abspath(__file__)
print 'File         :', f
print 'Absolute     :', os.path.isabs(f)
print 'Is File      :', os.path.isfile(f)
print 'Is Dir       :', os.path.isdir(f)
print 'Is Link      :', os.path.islink(f)
print 'Mountpoint?  :', os.path.ismount(f)
print 'Exists       :', os.path.exists(f)
print 'Link Exists? :', os.path.lexists(f)
'''
Absolute     : True
Is File      : True
Is Dir       : False
Is Link      : False
Mountpoint?  : False
Exists       : True
Link Exists? : True
'''

# Traversing a Directory Tree
def visit(arg, dirname, names):
    print dirname, arg
    for name in names:
        subname = os.path.join(dirname, name)
        if os.path.isdir(subname):
            print '     %s/' % name
        else:
            print '     %s' % name
os.path.walk('.', visit, '(start)')

'''
.
├── ospath.py
├── test1
│   ├── test11
│   └── test.txt
└── test2


. (start)
     ospath.py
     test1/
     test2/
./test1 (start)
     test11/
     test.txt
./test1/test11 (start)
./test2 (start)

'''

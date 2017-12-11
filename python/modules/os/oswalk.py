import os

for dir_name, sub_dirs, files in os.walk('.'):
    print dir_name
    print '\t', sub_dirs
    print '\t', files

'''

spath.py
├── oswalk.py
├── test1
│   ├── test11
│   └── test.txt
└── test2

.
        ['test2', 'test1']
        ['oswalk.py', 'ospath.py']
./test2
        []
        []
./test1
        ['test11']
        ['test.txt']
./test1/test11
        []
        []

'''

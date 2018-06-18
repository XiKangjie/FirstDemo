import tempfile

# It creates a file, and on platforms where it is possible, unlinks it immediately.
# This makes it impossible for another program to find or open the file, 
# since there is no reference to it in the filesystem table.

# The file created by TemporaryFile() or NamedTemporaryFile() is removed automatically when it is closed.

temp = tempfile.NamedTemporaryFile(suffix='_suffix',
                                   prefix='prefix_',
                                   dir='/tmp')
try:
    print 'temp:', temp
    print 'temp.name', temp.name
finally:
    temp.close()

"""
$ python tempfile_NamedTemporaryFile_args.py 
temp: <open file '<fdopen>', mode 'w+b' at 0x7fa86944af60>
temp.name /tmp/prefix_Th_z3Y_suffix
$ ls -l /tmp/prefix_Th_z3Y_suffix
ls: cannot access /tmp/prefix_Th_z3Y_suffix: No such file or directory
"""

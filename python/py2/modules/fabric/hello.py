# fab hello -f hello.py
# fab hello:name=Consen -f hello.py

def hello(name="world"):
    print 'Hello %s!' % name


"""
$ fab hello -f hello.py 
Hello world!

Done.
$ fab hello:name=Consen -f hello.py                              
Hello Consen!

Done.
"""

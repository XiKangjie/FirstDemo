import platform

print 'uname:', platform.uname()

print
print 'system   :', platform.system()
print 'node     :', platform.node()
print 'release  :', platform.release()
print 'version  :', platform.version()
print 'machine  :', platform.machine()
print 'processor:', platform.processor()

"""
uname: ('Linux', 'skyeye.360.cn', '3.10.20-11.el6.centos.alt.x86_64', '#1 SMP Sat Nov 23 23:08:56 UTC 2013', 'x86_64', 'x86_64')

system   : Linux
node     : thinkpad
release  : 3.10.20-11.el6.centos.alt.x86_64
version  : #1 SMP Sat Nov 23 23:08:56 UTC 2013
machine  : x86_64
processor: x86_64
"""

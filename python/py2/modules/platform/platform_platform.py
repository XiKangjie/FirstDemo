import platform

print 'Normal :', platform.platform()
print 'Aliased:', platform.platform(aliased=True)
print 'Terse  :', platform.platform(terse=True)

"""
Normal : Linux-3.10.20-11.el6.centos.alt.x86_64-x86_64-with-centos-6.6-Final
Aliased: Linux-3.10.20-11.el6.centos.alt.x86_64-x86_64-with-centos-6.6-Final
Terse  : Linux-3.10.20-11.el6.centos.alt.x86_64-x86_64-with-glibc2.2.5
"""

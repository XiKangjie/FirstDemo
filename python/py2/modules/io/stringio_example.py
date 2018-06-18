# -*- coding: utf-8 -*-

from io import StringIO

# write to StringIO:
f = StringIO()
f.write(u'hello')
f.write(u' ')
f.write(u'world!')
print(f.getvalue())

# read from StringIO:
f = StringIO(u'水面细风生，\n菱歌慢慢声。\n客亭临小市，\n灯火夜妆明。')
while True:
    s = f.readline()
    if s == u'':
        break
    print(s.strip())

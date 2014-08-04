# http://fun.coolshell.cn/81648.html
# Dvorak Simplified Keyboard to QWERTY Keyboard

D2Q = dict(zip(r'''`1234567890[]',.pyfgcrl/=\aoeuidhtns-;qjkxbmwvz~!@#$%^&*(){}"<>PYFGCRL?+|AOEUIDHTNS_:QJKXBMWVZ ''',
               r'''`1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>? '''))
#print(D2Q)

for c in r'macb() ? lpcbyu(&gbcq/_\021%ocq\012\0_=w(gbcq)/_dak._=}_ugb_[0q60)s+':
    print(D2Q[c], end = '')
# main() { printf(&unix["\021%six\012\0"],(unix)["have"]+"fun"-0x60);}

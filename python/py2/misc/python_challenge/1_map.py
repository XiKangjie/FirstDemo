text = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. 
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. 
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''

trans_map = dict(zip('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab'))
def make_trans(s):
    ret = ''
    for c in s:
        if 'a' <= c <= 'z':
            ret += trans_map[c]
        else:
            ret += c
    return ret

print(make_trans(text))
'''
i hope you didnt translate it by hand. thats what computers are for. 
doing it in by hand is inefficient and that's why this text is so long. 
using string.maketrans() is recommended. now apply on the url.
'''
print(make_trans('map'))    # ocr

import string
trans_from = string.ascii_lowercase
trans_to = string.ascii_lowercase[2:] + string.ascii_lowercase[:2]
table = str.maketrans(trans_from, trans_to)
print(str.translate(text, table))
print(str.translate('map', table))

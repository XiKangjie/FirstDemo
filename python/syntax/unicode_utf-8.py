print(hex(ord('学')))
# 0x5b66 --> unicode code point

print('学'.encode('utf-8'))
# b'\xe5\xad\xa6'

print(b'\xe7\x8b\xbc'.decode('utf-8'))
# 狼
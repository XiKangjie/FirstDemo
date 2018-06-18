import binascii

hexstr = '7F18EB0233FF85FF75A65F5E'
data = binascii.unhexlify(hexstr)
print data
print binascii.hexlify(data)


hexstr = binascii.hexlify('hello')
print hexstr
print binascii.unhexlify(hexstr)


"""
3���u�_^
7f18eb0233ff85ff75a65f5e
68656c6c6f
hello
"""

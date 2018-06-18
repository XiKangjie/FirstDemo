import struct

values = (1, b'ab', 3.4)
print('Original values:', values)

endianness = [
    ('@', 'native, native'),
    ('=', 'native, standard'),
    ('<', 'little-endian'),
    ('>', 'big-endian'),
    ('!', 'network')
]

for code, name in endianness:
    s = struct.Struct(code + 'I 2s f')
    packed_data = s.pack(*values)
    print()
    print('Format string    :', s.format, 'for', name)
    print('Uses             :', s.size, 'bytes')
    print('Packed value     :', packed_data)
    print('Unpacked value   :', s.unpack(packed_data))

import struct
import socket
import zlib

stream_header = 'h B h'

with open('7357.bak', 'rb') as f:
    header = f.read(2 + 1 + 2 + 16 + 2 + 16)
    ip_proto, is_ipv6 = struct.unpack('<HB', header[0:3])
    print 'ipproto:', ip_proto, 'is_ipv6:', is_ipv6
    if is_ipv6 == 1:
        pass
    else:
        server_port, server_ip = struct.unpack('<HI', header[3:9])
        client_port, client_ip = struct.unpack('<HI', header[21:27])
    print 'sport:', server_port, 'sip:', server_ip
    print 'cport:', client_port, 'cip:', client_ip
    print 'sip:', socket.inet_ntoa(header[5:9])
    print 'cip:', socket.inet_ntoa(header[23:27])

    dolog = f.read(4)
    dologid_count, = struct.unpack('<I', dolog)
    print 'dologid_count:', dologid_count
    dolog = f.read(dologid_count * 4)
    dologid = []
    for i in range(dologid_count):
        id, = struct.unpack('<I', dolog[i*4 : (i+1)*4])
        dologid.append(id)
    print 'dologid:', dologid

    data = f.read(4)
    total_out, = struct.unpack('<I', data)
    print 'total_out:', total_out
    data = f.read(total_out)
    dedata = zlib.decompress(data)
    size, = struct.unpack('<I', dedata[0:4])
    direction, = struct.unpack('<B', dedata[4:5])
    s2c_count, = struct.unpack('<I', dedata[5:9])
    c2s_count, = struct.unpack('<I', dedata[9:13])
    print 'size:', size, 'direction:', direction, \
            's2c_count:', s2c_count, 'c2s_count:', c2s_count
    print dedata[13:(13+size)]


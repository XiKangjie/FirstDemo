"""
Sockets can be configured to act as a server and listen for incoming messages,
or connect to other applications as a client.
"""
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
# Calling listen() puts the socket into server mode, and accept() waits for an
# incoming connection.
# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'connection from', client_address
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                print >>sys.stderr, 'sending data back to the client'
                connection.sendall(data)
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
    finally:
        # Clean up the connection
        connection.close()

"""
starting up on localhost port 10000
waiting for a connection
connection from ('127.0.0.1', 52030)
received "This is the mess"
sending data back to the client
received "age. It will be "
sending data back to the client
received "repeated."
sending data back to the client
received ""
no more data from ('127.0.0.1', 52030)
waiting for a connection
"""

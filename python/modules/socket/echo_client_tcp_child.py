"""
The client program sets up its socket differently form the way a server does.
Instead of binding to a port and listening, it uses connect() to attach the 
socket directly to the remote address.
"""
import socket
import sys
import time
import subprocess

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cmd = ["cat"]
proc = subprocess.Popen(cmd)
print proc.pid

# For netstat and lsof
time.sleep(20)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stdout, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    # Send data
    message = 'This is the message. It will be repeated.'
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print >>sys.stderr, 'received "%s"' % data
finally:
    print >>sys.stderr, 'closing socket'
    time.sleep(20) # For netstat
    sock.close()

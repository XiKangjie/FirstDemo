"""
A socket is one endpoint of a communication channel used by programs to pass data
back and forth locally or across the Internet. Sockets have two primary properties
controlling the way they send data: the *address family* controls the OSI network
layer protocol used and the *socket type* controls the transport layer protocol.

Python supports three families. The most common, *AF_INET* is used for IPv4 Internet
addressing. *AF_INET6* is used for IPv6 Internet addressing. *AF_UNIX* is the
address family for Unix Domain Sockets(UDS), an interprocess communication protocol
available on POSIX-compliant systems.

The socket type is usually either SOCK_DGRAM for user datagram protocol(UDP) or
SOCK_STREAM for transmission control protocol(TCP).
"""

import socket

# Looking up Hosts on the Network
print socket.gethostname()              # ThinkPad


for host in ['www', 'www.baidu.com', 'ThinkPad']:
    try:
        print '%15s : %s' % (host, socket.gethostbyname(host))
    except socket.error, msg:
        print '%15s : ERROR: %s' % (host, msg)

"""
            www : ERROR: [Errno -2] Name or service not known
  www.baidu.com : 180.97.33.108
       ThinkPad : 127.0.1.1
"""


for host in ['www', 'www.baidu.com', 'ThinkPad']:
    print host
    try:
        hostname, aliases, addresses = socket.gethostbyname_ex(host)
        print '  Hostname:', hostname
        print '  Aliases :', aliases
        print ' Addresses:', addresses
    except socket.error, msg:
        print '%15s : ERROR: %s' % (host, msg)
    print

"""
www
            www : ERROR: [Errno -2] Name or service not known

www.baidu.com
  Hostname: www.a.shifen.com
  Aliases : ['www.baidu.com']
 Addresses: ['220.181.112.244', '220.181.111.188']

ThinkPad
  Hostname: ThinkPad
  Aliases : []
 Addresses: ['127.0.1.1']
"""


hostname, aliases, addresses = socket.gethostbyaddr('127.0.1.1')
print 'Hostname :', hostname
print 'Aliases  :', aliases
print 'Addresses:', addresses

"""
Hostname : ThinkPad
Aliases  : []
Addresses: ['127.0.1.1']
"""


# Finding Service Information
import urlparse
for url in [ 'http://www.python.org',
             'https://www.mybank.com',
             'ftp://prep.ai.mit.edu',
             'gopher://gopher.micro.umn.edu',
             'smtp://mail.example.com',
             'imap://mail.example.com',
             'imaps://mail.example.com',
             'pop3://pop.example.com',
             'pop3s://pop.example.com',
             ]:
    parsed_url = urlparse.urlparse(url)
    port = socket.getservbyname(parsed_url.scheme)
    print '%6s : %s' % (parsed_url.scheme, port)

for port in [ 80, 443, 21, 70, 25, 143, 993, 110, 995 ]:
    print urlparse.urlunparse(
        (socket.getservbyport(port), 'example.com', '/', '', '', '')
        )

"""
  http : 80
 https : 443
   ftp : 21
gopher : 70
  smtp : 25
  imap : 143
 imaps : 993
  pop3 : 110
 pop3s : 995
http://example.com/
https://example.com/
ftp://example.com/
gopher://example.com/
smtp://example.com/
imap2://example.com/
imaps://example.com/
pop3://example.com/
pop3s://example.com/
"""

# The number assigned to a transport protocol can be retrieved with getprotobyname()
for name in ['icmp', 'tcp', 'udp']:
    print name, socket.getprotobyname(name)

"""
icmp 1
tcp 6
udp 17
"""

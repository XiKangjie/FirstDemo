from netaddr import *

iprange = IPRange('172.16.1.100', '172.16.1.105')

for ip in iprange:
    print ip, ip in iprange, type(ip)

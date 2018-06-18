# The urllib2 module has been split across several modules in Python 3.0
# names urllib.request, urllib.parse and urllib.error.
#import urllib2
from urllib.request import urlopen
import time

hosts = ["http://www.yahoo.com", "http://www.google.com", "http://www.amazon.com",
		"http://www.ibm.com", "http://www.apple.com"]

start = time.time()
# grabs urls of hosts and print first 1024 bytes of page
for host in hosts:
	response = urlopen(host)
	print(response.read(1024))

print("Elapsed Time: {0}".format(time.time() - start))
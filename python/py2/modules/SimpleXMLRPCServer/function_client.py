import xmlrpclib

proxy = xmlrpclib.ServerProxy('http://localhost:9090')
print proxy.list_contents('./')
print proxy.list_contents('./')
print proxy.list_contents('./')

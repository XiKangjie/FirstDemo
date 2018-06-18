import xmlrpclib

proxy = xmlrpclib.ServerProxy('http://localhost:9090')
print proxy.list_contents2('./')
print proxy.list_contents2('./')
print proxy.list_contents2('./')

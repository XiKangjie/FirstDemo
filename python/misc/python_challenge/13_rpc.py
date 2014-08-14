import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print(proxy.system.listMethods())				# ['phone', 'system.listMethods', 'system.methodHelp',
												# 'system.methodSignature', 'system.multicall',
												# 'system.getCapabilities']
print(proxy.system.methodHelp('phone'))			# Returns the phone of a person
print(proxy.system.methodSignature('phone'))	# [['string', 'string']]

print(proxy.phone('Bert'))						# 555-ITALY

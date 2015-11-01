class MetaOne(type):
	def __new__(meta, classname, supers, classdict): # Redefine type method
		print('In MetaOne.new:', classname)
		return type.__new__(meta, classname, supers, classdict)

	def __init__(cls, classname, supers, classdict):
		print('In MetaOne.init:', cls, classname)

	def toast(self):
		print('toast')

class Super(metaclass=MetaOne): # Metaclass inherited by subs too
	def spam(self): # MetaOne run twice for two classes
		print('spam')

class Sub(Super): # Superclass: inheritance versus instance
	def eggs(self): # Classes inherit from superclasses
		print('eggs')# But not from metaclasses

print(dir(Super))
print(dir(Sub))
X = Sub()
X.eggs()
X.spam()

Sub.eggs(X)
Sub.spam(X)
Sub.toast()
MetaOne.toast(Sub)
MetaOne.toast(Super)
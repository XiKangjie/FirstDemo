# Context Managers are a fancy way to say -- before that code do something,
# and after that code do something.

filename = "my_file.txt"
mode = "w"

# uh, what happens if we never reach the 'close' call ?
# writer = open(filename, mode)
# writer.write("Hello ")
# writer.write("World")
# writer.close()

# ok
# but when we do more than writing "Hello World" to a file, this try-finally syntax tends
# to be complicated and ugly.
# writer = open(filename, mode)
# try:
# 	writer.write("Hello ")
# 	writer.write("World")
# finally:
# 	writer.close()

# beautiful and safe
# the 'open' Context Manger
# the open function, can be used as both simple function, and as a Context Manager.
# 'with' is a new keyword, that always go along with Context Mangers.
# 'as' is another keyword, it says take what returned from the 'open' function,
# and assign it to a new variable.
# with open(filename, mode) as writer:
# 	writer.write('Hello ')
# 	writer.write('World!')



# Writing our own Context Manager.

# class PypixContextManagerDemo:
# 	def __enter__(self):
# 		print('Enter the block')
# 	def __exit__(self, *unused):
# 		print('Exiting the block')

# with PypixContextManagerDemo():
# 	print('In the block')

# Output:
# Enter the block
# In the block
# Exiting the block

# class PypixOpen:
# 	def __init__(self, filename, mode):
# 		self.filename = filename
# 		self.mode = mode

# 	def __enter__(self):
# 		self.openedFile = open(self.filename, self.mode)
# 		return self.openedFile

# 	def __exit__(self, *unused):
# 		self.openedFile.close()

# with PypixOpen(filename, mode) as writer:
# 	writer.write("Hell World from our new Context Manager!")



# More

with open('fileToRead.txt', 'r') as reader, open('fileToWrite.txt', 'w') as writer:
	writer.write(reader.read())
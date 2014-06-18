# ****************************************************************** #
# ************************* Byte of Python ************************* #
# ****************************************************************** #

########################
# try_except
########################
# try:
# 	text = input("Enter something --> ")
# except EOFError:
# 	print("Why did you do an EOF on me?")
# except KeyboardInterrupt:
# 	print("You cancelled the operation.")
# else:
# 	print("You entered {0}".format(text))


########################
# raising 
########################
# class ShortInputException(Exception):
# 	"""A user-defined exception class."""
# 	def __init__(self, length, atleast):
# 		Exception.__init__(self)
# 		self.length = length
# 		self.atleast = atleast

# try:
# 	text = input("Enter something --> ")
# 	if len(text) < 3:
# 		raise ShortInputException(len(text), 3)
# except EOFError:
# 	print("Why did you do an EOF on me?")
# except ShortInputException as ex:
# 	print("ShortInputException: The input was {0} long, expected at least {1}"
# 		.format(ex.length, ex.atleast))
# else:
# 	print("No exception was raised.")


########################
# finally
########################
# import time

# f = None
# try:
# 	f = open("poem.txt")
# 	while True:
# 		line = f.readline()
# 		if len(line) == 0:
# 			break
# 		print(line, end = "", flush = True)
# 		time.sleep(2)
# except FileNotFoundError:
# 	print("Could not find file poem.txt")
# except KeyboardInterrupt:
# 	print("!! You cancelled the reading from the file.")
# finally:
# 	if f:
# 		f.close()
# 	print("(Cleaning up: Closed the file)")


########################
# using_with
########################
with open("poem.txt") as f:
	for line in f:
		print(line, end = "")

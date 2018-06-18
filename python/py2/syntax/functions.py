# ****************************************************************** #
# ************************* Byte of Python ************************* #
# ****************************************************************** #

########################
# function1
########################
# def sayHello():
# 	print("Hello World!")

# sayHello()
# sayHello()

########################
# func_param
########################
# def printMax(a, b):
# 	if a > b:
# 		print(a, "is maximum")
# 	elif a == b:
# 		print(a, "is equal to", b)
# 	else:
# 		print(b, "is maximum")

# printMax(3, 4)

# x = 5
# y = 7
# printMax(x, y)

########################
# func_local
########################
# x = 50
# def func(x):
# 	print("x is", x)
# 	x = 2
# 	print("Changed local x to", x)
# func(x)
# print("x is still", x)

########################
# func_global
########################
# x = 50
# def func():
# 	global x
# 	print("x is", x)
# 	x = 2
# 	print("Changed global x to", x)
# func()
# print("Value of x is", x)

########################
# func_default
########################
# def say(message, times = 1):
# 	print(message * times)
# say("Hello")
# say("Hello", 5)

########################
# func_key
########################
# def func(a, b = 5, c = 10):
# 	print("a is", a, "and b is", b, "and c is", c)

# func(3, 7)
# func(25, c = 24)
# func(c = 50, a =100)
# #func(c = 50)	# Error

#######################
# total
#######################
# def total(initial = 5, *numbers, **keywords):
# 	count = initial
# 	for number in numbers:
# 		count += number
# 	for key in keywords:
# 		count += keywords[key]
# 	return count

# print(total(10, 1, 2, 3, vegetables = 50, fruits = 100))

#######################
# keyword_only
#######################
# def total(initial = 5, *numbers, extra_number):
# 	count = initial
# 	for number in numbers:
# 		count += number
# 	count += extra_number
# 	print(count)

# total(10, 1, 2, 3, extra_number = 50)
# total(10, 1, 2, 3)

########################
# func_return
########################
# def maximum(x, y):
# 	if x > y:
# 		return x
# 	elif x == y:
# 		return "The numbers are equal"
# 	else:
# 		return y
# print(maximum(2, 3))
# print(maximum(2, 2))

########################
# func_doc
########################
# def printMax(x, y):
# 	"""Prints the maximum of two numbers.

# 	The two values must be integers."""
# 	x = int(x)	# convert to integers, if possible
# 	y = int(y)

# 	if x > y:
# 		print(x, "is maximum")
# 	else:
# 		print(y, "is maximum")

# printMax(3, 5)
# print(printMax.__doc__)
# help(printMax)


# ****************************************************************** #
# ********************* Programming in python ********************** #
# ****************************************************************** #
def get_int(msg):
	while True:
		try:
			i = int(input(msg))
			return i
		except ValueError as err:
			print(err)

age = get_int("enter your age: ")
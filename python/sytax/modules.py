# ****************************************************************** #
# ************************* Byte of Python ************************* #
# ****************************************************************** #

########################
# using_sys
########################
# import sys

# print("The command line arguments are:")
# for i in sys.argv:
# 	print(i)

# print("\n\nThe PYTHONPATH is", sys.path, "\n")

########################
# using_name
########################
# if __name__ == "__main__":
# 	print("This program is being run by itself")
# else:
# 	print("I am being imported from another module")

########################
# mymodule
########################
# def sayhi():
# 	print("Hi, this is mymodule speaking.")

# __version__ = "0.1"


# ****************************************************************** #
# ********************* Programming in python ********************** #
# ****************************************************************** #
import random
x = random.randint(1, 6)
y = random.choice(['apple', 'banana', 'cherry', 'durian'])
print(x)
print(y)
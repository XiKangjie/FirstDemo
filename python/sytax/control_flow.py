# ****************************************************************** #
# *********************** <<Byte of Python>> *********************** #
# ****************************************************************** #

########################
# if
########################
# number = 23
# guess = int(input("Enter an integer : "))

# if guess == number:
# 	print("Congratulations, you guessed it.")
# 	print("(but you do not win any prizes!)")
# elif guess < number:
# 	print("No, it is a litter higher than that")
# else:
# 	print("No, it is a little lower than that")

# print("Done")

########################
# while
########################
# number = 23
# running = True

# while running:
# 	guess = int(input("Enter an integer: "))
# 	if guess == number:
# 		print("Congratulations, you guessed it.")
# 		running = False
# 	elif guess < number:
# 		print("No, it is a little higher than that.")
# 	else:
# 		print("No, it is a little lower than that.")
# else:
# 	print("The while loop is over.")

# print("Done")

########################
# for
########################
# for i in range(1, 5):
# 	print(i)
# else:
# 	print("The for loop is over")

########################
# break
########################
# while True:
# 	s = input("Enter something: ")
# 	if s == "quit":
# 		break
# 	print("Length of the string is", len(s))
# else:
# 	print("quit")
# print("done")

########################
# continue
########################
# while True:
# 	s = input("Enter something: ")
# 	if s == "quit":
# 		break
# 	if len(s) < 3:
# 		print("Too small")
# 		continue
# 	print("Input is of sufficient length")


# ****************************************************************** #
# ********************<<Programming in python>> ******************** #
# ****************************************************************** #
# for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
# 	if letter in "AEIOU":
# 		print(letter, "is a vowel")
# 	else:
# 		print(letter, "is a consonant")


# ****************************************************************** #
# *************************** Demo ********************************* #
# ****************************************************************** #
# ord is short for ordinal
sum = 0
for c in "Angelia":
	sum += ord(c)
print(sum)

s = ""
for c in "Consen":
	c = chr(ord(c) + 1)
	s += c
print(s)
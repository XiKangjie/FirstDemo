# ****************************************************************** #
# ************************* Byte of Python ************************* #
# ****************************************************************** #

########################
# user_input
########################
# def reverse(text):
# 	return text[::-1]

# def is_palindrome(text):
# 	return text == reverse(text)

# something = input("Enter text: ")
# if is_palindrome(something):
# 	print("Yes, it is a palindrome")
# else:
# 	print("No, it is not a palindrome")


########################
# using_file
########################
# poem = """\
# Programming is fun
# When the work is done
# if you wanna make your work also fun:
# 	use Python!
# """

# # if poem.txt does not exist, then create it. 
# f = open("poem.txt", "w")
# f.write(poem)
# f.close()

# f = open("poem.txt")
# while True:
# 	line = f.readline()
# 	if len(line) == 0:
# 		break
# 	print(line, end = "")
# f.close()


########################
# pickling
########################
# import pickle

# shoplistfile = "shoplist.data"
# shoplist = ["apple", "mango", "carrot"]

# f = open(shoplistfile, "wb")
# pickle.dump(shoplist, f)	# dump the object to a file
# f.close()

# del shoplist	# destroy the shoplist variable

# f = open(shoplistfile, "rb")
# storedlist = pickle.load(f)	# load the object from the file
# print(storedlist)


########################
# unicode -- python2
########################
print(type("hello world"))
print(type(u"hello world"))

f = open("abc.txt", "wt", encoding = "utf-8")
f.write("中国")
f.close()

text = open("abc.txt", encoding = "utf-8").read()

print(text)
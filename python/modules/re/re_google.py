import re

str = "an example word:cat!!"
match = re.search(r"word:\w\w\w", str)
if match:
	print("found", match.group())
else:
	print("did not find")

# Basic Examples

match = re.search(r"iii", "piiig")	# "iii"
match = re.search(r"igs", "piiig")	# None

match = re.search(r"..g", "piiig")	# "iig"

match = re.search(r"\d\d\d", "p123g")	# "123"
match = re.search(r"\w\w\w", "@@!3a_bcd!!")	# "3a_"
if match:
	print(match.group())


# Repetition Examples	(Leftmost & Largest)

# i+ = one or more i's, as many as possible
match = re.search(r"pi+", "piiig")	# "piii"

# Finds the first/leftmost solution, and within it drives the +
# as far as possible (aka "leftmost and largest").
# In this example, note that it does not get to the second set of i's.
match = re.search(r"i+", "piigiiii")	# "ii"

# \s* = zero or more whitespace chars
# Here look for 3 digits, possibly separated by whitespace.
match = re.search(r"\d\s*\d\s*\d", "xx1 2    3xx")	# "1 2    3"
match = re.search(r"\d\s*\d\s*\d", "xx12    3xx")	# "12    3"
match = re.search(r"\d\s*\d\s*\d", "xx123xx")	# "123"

# ^ = matchs the start of string, so this fails:
match = re.search(r"^b\w+", "foobar")	# None
# but without the ^ it succeeds:
match = re.search(r"b\w+", "foobar")	# "bar"



# Emails Example

str = "purple alice-b@google.com monkey dishwasher"
match = re.search(r"\w+@\w+", str)
if match:
	print(match.group())	# "b@google"

# Square Brackets
match = re.search(r"[\w.-]+@[\w.-]+", str)
if match:
	print(match.group())	# alice-b@google.com
# an up-hat(^) at the start of a square-bracket set inverts it,
# so [^ab] means any char except 'a' or 'b'.



# Group Extraction
str = "purple alice-b@google.com monkey dishwasher"
match = re.search("([\w.-]+)@([\w.-]+)", str)
if match:
	print(match.group())	# "alice-b@google.com"
	print(match.group(1))	# "alice-b"
	print(match.group(2))	# "google.com"


# findall
str = "purple alice@google.com, blah monkey bob@abc.com blah dishwasher"

# Here re.findall() returns a list of all the found email strings
emails = re.findall(r"[\w\.-]+@[\w\.-]+", str)	# ["alice@google.com", "bob@abc.com"]
for email in emails:
	print(email)

# # findall With Files
# f = open("test.txt", "r")
# # Feed the file text ino findall()
# strings = re.findall(r"some pattern", f.read())

# findall and Groups
str = "purple alice@google.com, blah monkey bob@abc.com blah dishwasher"
tuples = re.findall(r"([\w\.-]+)@([\w\.-]+)", str)
print(tuples)
for tuple in tuples:
	print(tuple[0])
	print(tuple[1])


# Substitution
str = "purple alice@google.com, blah monkey bob@abc.com blah dishwasher"
# \1 is group(1), \2 group(2) in the replacement.
print(re.sub(r"([\w\.-]+)@([\w\.-]+)", r"\1@yo-yo-dyne.com", str))
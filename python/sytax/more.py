# ****************************************************************** #
# ************************* Byte of Python ************************* #
# ****************************************************************** #

########################
# passing tuples around
########################
# def get_error_details():
# 	return (2, "second error details")

# errnum, errstr = get_error_details()
# print(errnum)
# print(errstr)

# a, *b = [1, 2, 3, 4]
# print(a)
# print(b)

# a = 5; b = 8
# a, b = b, a
# print(a, b)


########################
# special methods
########################
# __init__(self, ...)
# __del__(self)
# __str__(self)
# __lt__(self, other)
# __getitem__(self, key)
# __len__(self)


########################
# single_statement_block
########################
# if True: print("Yes")



########################
# lambda
########################
# points = [ {"x" : 2, "y" : 3}, {"x" : 4, "y" : 1} ]
# points.sort(key = lambda i : i["y"])
# print(points)


########################
# list_comprehension
########################
# listone = [2, 3, 4]
# listtwo = [2 * i for i in listone if i > 2]
# print(listtwo)


########################
# tuple and dic in func
########################
# def powersum(power, *args):
# 	"""return the sum of each argument raised to specified power."""
# 	total = 0
# 	for i in args:
# 		total += pow(i, power)
# 	return total

# print(powersum(2, 3, 4))
# print(powersum(2, 10))


########################
# assert
########################
# mylist = ["item"]
# assert len(mylist) >= 1

# mylist.pop()
# assert len(mylist) >= 1


########################
# decorators
########################
from time import sleep
from functools import wraps
import logging
logging.basicConfig()
log = logging.getLogger("retry")

def retry(f):
	@wraps(f)
	def wrapped_f(*args, **kwargs):
		MAX_ATTEMPTS = 5
		for attempt in range(1, MAX_ATTEMPTS + 1):
			try:
				return f(*args, **kwargs)
			except:
				log.exception( "Attemp %s/%s failed : %s",
								attempt,
								MAX_ATTEMPTS,
								(args, kwargs) )
				sleep(10 * attempt)
		log.critical("All %s attempts failed : %s",
					 MAX_ATTEMPTS,
					 (args, kwargs) )

	return wrapped_f

counter = 0

@retry
def save_to_database(arg):
	print("Write to a database or make a network call or etc.")
	print("This will be automatically retried if exception is thrown.")
	global counter
	counter += 1
	if counter < 2:
		raise ValueError(arg)

if __name__ == "__main__":
	save_to_database("Some bad value")
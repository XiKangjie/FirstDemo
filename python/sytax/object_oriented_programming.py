# ****************************************************************** #
# ************************* Byte of Python ************************* #
# ****************************************************************** #

########################
# simplestclass
########################
# class Person:
# 	pass

# p = Person()
# print(p)


########################
# methond
########################
# class Person:
# 	def sayhi(self):
# 		print("Hello, how are you?")

# p = Person()
# p.sayhi()


########################
# class_init
########################
# class Person:
# 	def __init__(self, name):
# 		self.name = name
# 	def sayHi(self):
# 		print("Hello, my name is", self.name)

# p = Person("Swaroop")
# p.sayHi()


########################
# objvar
########################
# class Robot:
# 	"""Represents a robot, with a name."""

# 	# A class variable, counting the number of robots
# 	population = 0

# 	def __init__(self, name):
# 		"""Initializes the data."""
# 		self.name = name
# 		print("(Initializeing {0})".format(self.name))
# 		Robot.population += 1

# 	def die(self):
# 		"""I am dying."""
# 		print("{0} is being destroyed!".format(self.name))
# 		Robot.population -= 1

# 		if Robot.population == 0:
# 			print("{0} was the last one.".format(self.name))
# 		else:
# 			print("There are still {0:d} robots working.".format(Robot.population))

# 	def sayHi(self):
# 		"""Greeting by the robot.

# 		Yeah, they can do that."""
# 		print("Greetings, my masters call me {0}.".format(self.name))

# 	@classmethod
# 	def howMany(cls):
# 		"""Prints the current population."""
# 		print("We have {0:d} robots.".format(cls.population))

# droid1 = Robot("R2-D2")
# droid1.name = "R2-D3"
# droid1.sayHi()
# Robot.howMany()

# droid2 = Robot("C-3PO")
# droid2.sayHi()
# Robot.howMany()

# print("\nRobots can do some work here.\n")

# print("Robots have finished their work. So let's destroy them.")
# droid1.die()
# droid2.die()

# Robot.howMany()


########################
# inherit
########################
# class SchoolMember:
# 	"""Represents any school member."""
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
# 		print("(Initialized SchoolMember: {0})".format(self.name))

# 	def tell(self):
# 		"""Tell my details."""
# 		print("Name: '{0}' Age:'{1}'".format(self.name, self.age), end = " ")

# class Teacher(SchoolMember):
# 	"""Represents a teacher."""
# 	def __init__(self, name, age, salary):
# 		SchoolMember.__init__(self, name, age)
# 		self.salary = salary
# 		print("(Initialized Teacher: {0})".format(self.name))

# 	def tell(self):		# all the methods are virtual in Python.
# 		SchoolMember.tell(self)
# 		print("Salary: '{0:d}'".format(self.salary))

# class Student(SchoolMember):
# 	"""Represents a student."""
# 	def __init__(self, name, age, marks):
# 		SchoolMember.__init__(self, name, age)
# 		self.marks = marks
# 		print("(Initialized Student: {0})".format(self.name))

# 	def tell(self):
# 		SchoolMember.tell(self)
# 		print("Marks: '{0:d}'".format(self.marks))

# t = Teacher("Mrs. Shrividya", 40, 30000)
# s = Student("Swaroop", 25, 75)

# print()		# prints a blank line

# members = [t, s]
# for member in members:
# 	member.tell()		# works for both Teachers and Students

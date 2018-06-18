import argparse

parser = argparse.ArgumentParser(description = 'parse person info')

parser.add_argument('-v', '--version', action = 'version', version = '%(prog)s 1.0 2014.10.10')
parser.add_argument('-n', '--name', required = True, help = 'your name')
parser.add_argument('-a', '--age', default = 12, type = int, help = 'your age')
parser.add_argument('-g', '--gender', choices = ['male', 'female'], help = 'your gender')
parser.add_argument('-o', '--ok', action = 'store_true', default = False, help = 'are you ok?')

#print(parser.parse_args(['-nconsen', '--age', '18', '-o']))
#print(parser.parse_args('-nconsen --age 18 -o'.split())) 
#Namespace(age=18, gender=None, name='consen', ok=True)

#print(parser.parse_args())
#Namespace(age=12, gender=None, name='none', ok=False)

info = parser.parse_args()
print('name: ', info.name)
print('age:', info.age)
print('gender:', info.gender)
print('ok:', info.ok)

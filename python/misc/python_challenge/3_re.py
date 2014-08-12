import re

text = open('re.txt').read()
m = re.findall(r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', text)
#print(m)
for i in m:
    print(i[4], end = '')
print()
# linkedlist


print(''.join(re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', text)))

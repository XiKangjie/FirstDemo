import re
string = open('cat.txt').read()
#print(string)
ans = re.search(r'([X-Z] | [0-9])([X-Z] | [0-9])[cat]\2\1', string)
print(ans.group())

'''
import re
string = open('cat.txt').read()
#print(string)
it = re.finditer(r'(\w)(\w).\2\1', string)
match = []
for i in it:
    # print(i.group())
    match.append(i.group())

#print(match)
length = len(match)
for i in range(0, length):
    for j in range(i + 1, length):
        for k in range(j + 1, length):
            #if (match[i][1] + match[j][0] == match[k][1]) or (ord(match[j][1]) - ord(match[i][0]) == ord(match[k][0]) - ord(match[j][1])):
            #if ord(match[j][1]) - ord(match[i][0]) == ord(match[k][0]) - ord(match[j][1]):
                print(match[0], match[1], match[2])
'''
import re
text = open('cat.txt').read()
it = re.finditer(r'([A-Z])([0-9])[a-z]\2\1|([0-9])([A-Z])[a-z]\4\3', text)
ans = ''
for i in it:
    print(i.group())
    ans += i.group()[2]

print('answer is : ', ans)

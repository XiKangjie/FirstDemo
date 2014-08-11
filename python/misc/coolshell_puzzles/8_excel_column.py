def excel_column_number(s):
    ret = 0
    base = 1
    for c in s[::-1]:
        ret += (ord(c) - ord('A') + 1) * base
        base *= 26
    return ret
#print(excel_column_number('AA'), excel_column_number('ZA'), excel_column_number('AAA'))
coolshell = excel_column_number('COOLSHELL')  
shell = excel_column_number('SHELL')
print('coolshell = ', coolshell, 'shell = ', shell)
print('coolshell / shell = ', coolshell / shell)    # 85165, cool, but you should covert the number to string!

def excel_column(n):
    ret = ''
    while n > 0:
        n, r = (0, 26) if n == 26 else divmod(n, 26)
        #print(n, r)
        ret = chr(r + ord('A') - 1) + ret
    return ret

#print(excel_column(1), excel_column(27), excel_column(677))
ans = excel_column(85165)
print('85165: ', ans)   # DUYO
print('answer is ', ans.lower())

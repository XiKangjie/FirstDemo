ans = [(None, None)] * 9
anss = []

def check_safe(posi, posj) :
    #print(posi, posj)
    '''
    if posj == 0:
        return True
    for (i, j) in ans:
        if i is not None and j is not None:
            if posi == i or posj == j or abs(posi - i) == abs(posj - j):
                return False
    '''
    for j in range(0, posj):
        if posi == ans[j][0] or posj == ans[j][1] or abs(posi - ans[j][0]) == abs(posj - ans[j][1]):
            return False
    return True

def nine_queens(j):
    #print(j)
    if j == 9:
        anss.append([str(i + 1) for (i, j) in ans])
        return
    for i in range(0, 9):
        if check_safe(i, j):
            ans[j] = (i, j)
            nine_queens(j + 1)

nine_queens(0)
#print(len(anss), anss)
anss_str = [''.join(i) for i in anss]
print(len(anss_str), anss_str)

import hashlib

#s = hashlib.sha1()
for code in anss_str:
    s = hashlib.sha1()
    # Repeated update() calls are equivalent to a single call with the concatenation of all the arguments
    s.update(('zWp8LGn01wxJ7' + code + "\n").encode('utf-8'))
    if s.hexdigest() == 'e48d316ed573d3273931e19f9ac9f9e6039a4242':
        print('answer is ', code)
# 953172864

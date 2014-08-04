# http://fun.coolshell.cn/unix.html

D = dict(zip('pvwdgazxubqfsnrhocitlkeymj',
             'abcdefghijklmnoqprstuvwxyz'))

string = 'Wxgcg txgcg ui p ixgff, txgcg ui p epm. I gyhgwt mrl lig txg ixgff wrsspnd tr irfkg txui hcrvfgs, nre, hfgpig tcm liunz txg crt13 ra "ixgff" tr gntgc ngyt fgkgf.'
answer = ''

for c in string:
    if c in D:
        answer += D[c]
    else:
        answer += c

print(answer)
# Where there is a shell, there is a way. I exqect you use the shell command to solve this qroblem, now, qlease try using the rot13 of "shell" to enter next level.

rot13 = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))
print([rot13[c] for c in 'shell'])

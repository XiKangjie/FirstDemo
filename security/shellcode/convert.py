with open('hello', 'rb') as f:
    shellcode = ''
    for line in f:
        for c in line:
            shellcode += '\\x' + str(c.encode('hex'))
    print shellcode

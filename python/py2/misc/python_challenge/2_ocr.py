import string

ans = ''
for line in open('ocr.txt'):
    for c in line:
        if c in string.ascii_letters:
            ans += c
print(ans)  # equality

text = open('ocr.txt').read()
print(''.join(filter(lambda x: x in string.ascii_letters, text)))

# in source there is <html> <!-- <-- zip -->
# download http://www.pythonchallenge.com/pc/def/channel.zip
import zipfile

z = zipfile.ZipFile('channel.zip')
num = 90052
f = '{0}.txt'.format(num)
comments = []
while True:
    data = z.read(f).decode('utf-8')
    #print(data)
    if data.startswith('Next'):     # Next nothing is 94758
        global num, f
        num = data.split()[-1]
        f = '{0}.txt'.format(num)
    else:                           # hint: Collect the comments
        break
    #print(z.getinfo(f).comment)
    comments.append(z.getinfo(f).comment.decode('utf-8'))
print(''.join(comments))
# hockey                            # hint: it's in the air. look at the letters.
# oxygen

# in source, there is a url http://www.pythonchallenge.com/pc/def/banner.p
import pickle

with open('banner.p', 'rb') as f:
    data = pickle.load(f)
#print(data)
for line in data:
    for (c, n) in line:
        print(c * n, end = '')
    print()
# channel

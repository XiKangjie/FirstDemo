from PIL import Image

img = Image.open('mozart.gif')
#straight = Image.new(img.mode, img.size, 253)
straight = img.copy()

w, h = img.size
for y in range(h):
	line = [img.getpixel((x, y)) for x in range(w)]
	pink = line.index(195)
	line = line[pink:] + line[:pink]
	for x in range(w):
		straight.putpixel((x, y), line[x])
straight.show()
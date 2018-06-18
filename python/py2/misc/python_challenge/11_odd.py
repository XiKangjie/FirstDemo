from PIL import Image, ImageDraw

img = Image.open('cave.jpg')
coords = []

w, h = img.size
for i in range(w):
	for j in range(h):
		if (i + j) % 2 == 1:
			coords.append((i, j))

draw = ImageDraw.Draw(img)
draw.point(coords, fill = 'black')

img.show()	# evil
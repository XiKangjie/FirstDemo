from PIL import Image

data = open('evil2.gfx', 'rb').read()
for i in range(5):
	f = 'image{0}.dat'.format(i)
	open(f, 'wb').write(data[i::5])
	img = Image.open(f)
	print(img.format)

# JPEG	dis
# PNG	pro
# GIF	port
# PNG	ional
# JPEG	(ity)
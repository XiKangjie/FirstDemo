from PIL import Image

img = Image.open('oxygen.png')
#print(img.size)		# (629, 95)
#row = [img.getpixel((x, 45)) for x in range(629)]
#print(row)
row = [img.getpixel((x, 45)) for x in range(0, img.size[0], 7)]
ords = [r for r, g, b, a in row if r == g == b]
print(''.join(map(chr, ords)))
# smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
print(''.join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121])))
# integrity
from PIL import Image

# 0   1   2   3 ... 9999

# 0   1   2   3 ... 99
# 394 395       ... 100
#               ... 101
# ...               ...
# 297           199 198

#         (x, y-1)
# (x-1,y) (x, y)    (x+1, y)
#         (x, y+1)
#

wire = Image.open('wire.png')
spiral = Image.new(wire.mode, (100, 100))
left, top, right, bottom = (0, 0, 99, 99)
x, y = 0, 0
dirx, diry = 1, 0
for i in range(10000):
    spiral.putpixel((x, y), wire.getpixel((i, 0)))
    if dirx == 1 and x == right:
        dirx, diry = 0, 1
        top += 1
    elif diry == 1 and y == bottom:
        dirx, diry = -1, 0
        right -= 1
    elif dirx == -1 and x == left:
        dirx, diry = 0, -1
        bottom -= 1
    elif diry == -1 and y == top:
        dirx, diry = 1, 0
        left += 1
    x += dirx
    y += diry

spiral.show()
spiral.save('spiral.png')

# from PIL import Image

# im = Image.open('Advanced/simpleQuant.jpg')
# # rgb_im = im.convert('RGB')
# r, g, b = im.getpixel((200, 300))
# print(r, g, b)
# # (66, 44, 7)

# im.putpixel((200, 300), (100, 100, 100))
# r, g, b = im.getpixel((200, 300))
# print(r, g, b)

from PIL import Image


def simple_quant():
    im = Image.open("Advanced/bubbles.jpg")
    w, h = im.size
    for row in range(h):
        for col in range(w):
            r, g, b = im.getpixel((col, row))
            r = r // 36 * 36
            g = g // 42 * 42
            b = b // 42 * 42
            im.putpixel((col, row), (r, g, b))
    im.show()


simple_quant()
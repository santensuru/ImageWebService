from PIL import Image

im = Image.open("lena.png")

print im.format, im.size, im.mode

'''
im.show()
'''

gs = im.convert("L")

gs.save("gs_lena.png", "png")

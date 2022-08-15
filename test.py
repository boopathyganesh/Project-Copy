from PIL import Image
im = Image.open("testocr.png")
print(im.format, im.size, im.mode)

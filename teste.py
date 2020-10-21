from PIL import Image

im = Image.open("example.png")
im.show()
im = im.rotate(45)
im.show()
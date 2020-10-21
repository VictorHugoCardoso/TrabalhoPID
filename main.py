from PIL import Image

name = "binary.png"
img = Image.open("imagens/"+name)

print("Formato:", img.format)
print("Size:", img.size)
print("Mode:", img.mode)

img.show()
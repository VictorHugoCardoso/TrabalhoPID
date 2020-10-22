import PIL
from PIL import Image
import numpy as np

name = "example.png"
img = Image.open("imagens/"+name).convert('L').point(lambda x: 0 if x<128 else 255, 'L')

print("Formato:", img.format)
print("Size:", img.size)
print("Mode:", img.mode)

ar = np.array(img)
print(ar)
print(ar[0, 199])

finalImage = Image.fromarray(np.uint8(ar))
finalImage.save('imagens/result.png')
#finalImage.show()
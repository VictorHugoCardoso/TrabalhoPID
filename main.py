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

for i in range(ar.shape[0]):
    for j in range(ar.shape[1]):
        if(ar[i, j] == 255):
            ar[i, j] = 0;
        else:
            ar[i, j] = 255;

finalImage = Image.fromarray(np.uint8(ar))
finalImage.save('imagens/result.png')
finalImage.show()
import PIL
from PIL import Image
import numpy as np

name = "example2.png"
img = Image.open("imagens/"+name).convert('L').point(lambda x: 0 if x<128 else 255, 'L')

print("Formato:", img.format)
print("Size:", img.size)
print("Mode:", img.mode)

ar = np.array(img)
print('Antes:\n',ar)

def dilate(ar):
    for i in range(ar.shape[0]):
        for j in range(ar.shape[1]):
            if (ar[i, j] == 255):
                if ((i>0) and (ar[i-1, j]==0)):
                    ar[i-1,j] = 2
                
                if ((j>0) and (ar[i, j-1]==0)):
                    ar[i,j-1] = 2
                
                if ((i+1<ar.shape[0]) and (ar[i+1, j]==0)):
                    ar[i+1, j] = 2

                if ((j+1<ar.shape[1]) and (ar[i, j+1]==0)):
                    ar[i, j+1] = 2

    for i in range(ar.shape[0]):
        for j in range(ar.shape[1]):
            if (ar[i, j] == 2):
                ar[i, j] = 255

dilate(ar)
print('Depois:\n',ar)

finalImage = Image.fromarray(np.uint8(ar))
finalImage.save('imagens/result.png')
finalImage.show()
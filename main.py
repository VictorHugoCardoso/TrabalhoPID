import PIL
from PIL import Image
from PIL import ImageFilter
import numpy as np

def dilate(ar,x):
    for n in range(x): 
        for i in range(ar.shape[0]):
            for j in range(ar.shape[1]):
                if (ar[i, j] == 255):
                    if ((i>0) and (ar[i-1, j]==0)):
                        ar[i-1,j] = 2 #cima
                    
                    if ((j>0) and (ar[i, j-1]==0)):
                        ar[i,j-1] = 2 #esquerda
                    
                    if ((i+1<ar.shape[0]) and (ar[i+1, j]==0)):
                        ar[i+1, j] = 2 #baixo

                    if ((j+1<ar.shape[1]) and (ar[i, j+1]==0)):
                        ar[i, j+1] = 2 #direita

        for i in range(ar.shape[0]):
            for j in range(ar.shape[1]):
                if (ar[i, j] == 2):
                    ar[i, j] = 255
        print(n,'...')

    print('Dilated:\n',ar)
    finalImage = Image.fromarray(np.uint8(ar))
    finalImage.save('imagens/dilated.png')
    #finalImage.show()

def erode(ar,x):
    for n in range(x):   
        for i in range(ar.shape[0]):
            for j in range(ar.shape[1]):
                if (ar[i, j] == 0):
                    if ((i>0) and (ar[i-1, j]==255)):
                        ar[i-1,j] = 2 #cima
                    
                    if ((j>0) and (ar[i, j-1]==255)):
                        ar[i,j-1] = 2 #esquerda
                    
                    if ((i+1<ar.shape[0]) and (ar[i+1, j]==255)):
                        ar[i+1, j] = 2 #baixo

                    if ((j+1<ar.shape[1]) and (ar[i, j+1]==255)):
                        ar[i, j+1] = 2 #direita

        for i in range(ar.shape[0]):
            for j in range(ar.shape[1]):
                if (ar[i, j] == 2):
                    ar[i, j] = 0

        print(n,'...')
    print('Eroded:\n',ar)
    finalImage = Image.fromarray(np.uint8(ar))
    finalImage.save('imagens/eroded.png')
    #finalImage.show()



name = "example1.png"
img = Image.open("imagens/"+name).convert('L').point(lambda x: 0 if x<128 else 255, 'L')

#cheat
'''
dilation_img = img.filter(ImageFilter.MaxFilter(3))
dilation_img.save('imagens/dilationFunction.png')
eroded_img = img.filter(ImageFilter.MinFilter(3))
eroded_img.save('imagens/erodedFunction.png')
'''

print("Formato:", img.format)
print("Size:", img.size)
print("Mode:", img.mode)

array1 = np.array(img)
array2 = np.array(img)

dilate(array1,2) #n
#erode(array2,10)
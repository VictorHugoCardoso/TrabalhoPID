import PIL
from PIL import Image
from PIL import ImageFilter
import numpy as np
import atlastk

def dilateCross(ar,x):
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
    finalImage.save('imagens/geradas/dilatedCross.png')
    #finalImage.show()

def dilateSquare(ar,x):
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

                    if ((ar[i-1, j-1]==0)):
                        ar[i-1,j-1] = 2 #cima diagonal esquerda

                    if ((ar[i-1, j-1]==0)):
                        ar[i-1,j+1] = 2 #cima diagonal direita

                    if ((ar[i-1, j-1]==0)):
                        ar[i+1,j-1] = 2 #baixo diagonal esquerda

                    if ((ar[i-1, j-1]==0)):
                        ar[i-1,j+1] = 2 #baixo diagonal direita

        for i in range(ar.shape[0]):
            for j in range(ar.shape[1]):
                if (ar[i, j] == 2):
                    ar[i, j] = 255
        print(n,'...')

    print('Dilated:\n',ar)
    finalImage = Image.fromarray(np.uint8(ar))
    finalImage.save('imagens/geradas/dilatedSquare.png')
    #finalImage.show()


def erodeCross(ar,x):
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
    finalImage.save('imagens/geradas/eroded.png')
    #finalImage.show()

def erodeSquare(ar,x):
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
                        
                    if ((ar[i-1, j-1]==255)):
                        ar[i-1,j-1] = 2 #cima diagonal esquerda

                    if ((ar[i-1, j-1]==255)):
                        ar[i-1,j+1] = 2 #cima diagonal direita

                    if ((ar[i-1, j-1]==255)):
                        ar[i+1,j-1] = 2 #baixo diagonal esquerda

                    if ((ar[i-1, j-1]==255)):
                        ar[i-1,j+1] = 2 #baixo diagonal direita


        for i in range(ar.shape[0]):
            for j in range(ar.shape[1]):
                if (ar[i, j] == 2):
                    ar[i, j] = 0

        print(n,'...')
    print('Eroded:\n',ar)
    finalImage = Image.fromarray(np.uint8(ar))
    finalImage.save('imagens/geradas/erodedSquare.png')
    #finalImage.show()


#---------------------------------------------------------------

def ac_connect(dom):
  dom.inner("", open("Main.html").read())
  dom.focus("input")

def ac_submit(dom):

  dom.disable_element("enviar")
  dom.disable_element("limpar")

  print("Caminho:", dom.get_value("input"))
  print("Dilate cross:", dom.get_value("dilateCross"))
  print("Dilate square:", dom.get_value("dilateSquare"))
  print("Erode cross:", dom.get_value("erodeCross"))
  print("Erode square:", dom.get_value("erodeSquare"))
  dom.focus("input")

  caminho_img = dom.get_value("input")
  img = Image.open('imagens/' + caminho_img).convert('L').point(lambda x: 0 if x < 128 else 255, 'L')

  print("Formato:", img.format)
  print("Size:", img.size)
  print("Mode:", img.mode)

  array1 = np.array(img)
  array2 = array1.copy()
  array3 = array1.copy()
  array4 = array1.copy()

  if dom.get_value("dilateCross") == "true" and int(dom.get_value("quantityDC")) > 0:
      dilateCross(array1, int(dom.get_value("quantityDC")))  # n

  if dom.get_value("dilateSquare") == "true" and int(dom.get_value("quantityDS")) > 0:
      dilateSquare(array2, int(dom.get_value("quantityDS")))  # n

  if dom.get_value("erodeCross") == "true" and int(dom.get_value("quantityEC")) > 0:
      erodeCross(array3, int(dom.get_value("quantityEC")))

  if dom.get_value("erodeSquare") == "true" and int(dom.get_value("quantityES")) > 0:
      erodeSquare(array4, int(dom.get_value("quantityES")))

  dom.alert("Imagens geradas e salvas na pasta \"imagens\geradas\" uma pasta dentro da pasta dos trabalho")
  dom.enable_element("enviar")
  dom.enable_element("limpar")

def ac_clear(dom):
  if ( dom.confirm("Tem certeza?") ):
    dom.set_value("input", "")
  dom.focus("input")

callbacks = {
  "": ac_connect,  # The action label for a new connection is an empty string.
  "Submit": ac_submit,
  "Clear": ac_clear,
}

atlastk.launch(callbacks, None, open("Head.html").read())


#name = "example1.png"


#cheat
'''
dilation_img = img.filter(ImageFilter.MaxFilter(3))
dilation_img.save('imagens/dilationFunction.png')
eroded_img = img.filter(ImageFilter.MinFilter(3))
eroded_img.save('imagens/erodedFunction.png')
'''


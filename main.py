import PIL
from PIL import Image
import numpy as np
import pandas as pd

name = "binary.png"
img = Image.open("imagens/"+name)


print("Formato:", img.format)
print("Size:", img.size)
print("Mode:", img.mode)

teste = np.array(img)
print(teste)

df = pd.DataFrame(teste)
print(df)

#img.show()
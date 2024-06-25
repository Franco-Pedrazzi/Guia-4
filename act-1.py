from PIL import Image
import os

def getRuta():
    ruta=input("inserte la ruta de la img ")
    if os.path.exists(ruta):
        return ruta
    else:
        return getRuta()
ruta=getRuta()
img=Image.open(ruta)
size=img.size
fileName=img.filename
fileName = fileName.split("\\")[-1]
print(fileName)
print(img.format)
print(img.size)
print(size[0]*size[1])
print(ruta)
img.show()

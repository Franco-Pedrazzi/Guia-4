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
formato=str(img.format).lower()
fileName=img.filename
fileName = str(fileName.split("\\")[-1]).lower()
img = img.convert('RGB')
pixeles=img.load()
fileName=fileName.replace(f".{formato}","")
for y in range(img.height):
    for x in range(img.width):
        r, g, b = pixeles[x, y]
        gris = int((r + g + b) / 3)
        pixeles[x, y] = (gris, gris, gris)

img.show()
img.save(f"{fileName}BN.{formato}")

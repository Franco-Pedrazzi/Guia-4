from PIL import Image
import os

def getRuta():
    ruta=input("inserte la ruta de la img ")
    if os.path.exists(ruta):
        return ruta
    else:
        return getRuta()
ruta=getRuta()

angulo=input("inserte el angulo de rotacion ")
img=Image.open(ruta)
formato=str(img.format).lower()
fileName=img.filename
fileName = str(fileName.split("\\")[-1]).lower()

fileName=fileName.replace(f".{formato}","")
img=img.rotate(int(angulo))
img.show()
img.save(f"{fileName} {angulo}.{formato}")
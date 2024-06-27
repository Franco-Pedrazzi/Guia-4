from PIL import Image
import os

def getRuta(ruta):
    if os.path.exists(ruta):
        return ruta
    else:
        return getRuta(input("inserte otra ruta "))
def selectEsquina(valor,imgSize):
    if valor.lower()=="superior izquierda":
        return (50,50)
    if valor.lower()=="superior derecha":
        return (imgSize-100,50)
    if valor.lower()=="inferior izquierda":
        return (50,imgSize-100)
    if valor.lower()=="inferior izquierda":
        return (imgSize-100,imgSize-100)
    return selectEsquina(input("seleccione una de estas opciones como posicion de la marca de agua: ● Superior izquierda ● Superior derecha ● Inferior izquierda ● Inferior derecha ",imgSize))

rutaDeLaImagen=getRuta(input("inserte la ruta de la img "))
rutaDeLaMarca=getRuta(input("inserte la ruta de la marca de agua "))
img=Image.open(rutaDeLaImagen)
marca=Image.open(rutaDeLaMarca)
imgSize=img.size
marca=marca.resize((50,50))
x,y=selectEsquina(input("seleccione una de estas opciones como posicion de la marca de agua: ● Superior izquierda ● Superior derecha ● Inferior izquierda ● Inferior derecha "),imgSize)
img.paste(marca, (x,y))
img.show()
img.save("imgConMarca.png")
from PIL import Image
import os

def getRuta():
    ruta=input("inserte la ruta de la img ")
    if os.path.exists(ruta):
        return ruta
    else:
        return getRuta()
def revisarC(lista,img):
    size=img.size
    if lista.count(",")==1:
        lista=lista.split(",")
        for value in lista:
            auxSize=size[lista.index(value)]
            if value.isdecimal()==False:
               return revisarC(input("inserte las cordenadas iniciales separandolas por coma y debe ser numeros enteros "),img)
    
            if int(value)<0 or int(value)>auxSize:
               return revisarC(input("inserte las cordenadas iniciales separandolas por coma y debe ser numeros enteros "),img)
    else:
        return revisarC(input("inserte las cordenadas iniciales separandolas por coma y debe ser numeros enteros "),img)
    return lista    
    
def revisarS(lista,img):
    size=img.size
    if lista.count(",")==1:
        lista=lista.split(",")
        for value in lista:
            auxSize=size[lista.index(value)]
            if value.isdecimal()==False:
               return revisarS(input("inserte las la anchura y altura separandolas por coma y debe ser numeros enteros "),img)
            if int(value)<0 or int(value)>auxSize:
               return revisarC(input("inserte las cordenadas iniciales separandolas por coma y debe ser numeros enteros "),img)
    else:
        return revisarC(input("inserte las cordenadas iniciales separandolas por coma y debe ser numeros enteros "),img)
   
    return lista              

ruta=getRuta()
img=Image.open(ruta)
x,y= revisarC(input("inserte las cordenadas iniciales separandolas por coma y debe ser numeros enteros "),img)

widht,height= revisarS(input("inserte las la anchura y altura separandolas por coma y debe ser numeros enteros "),img)
   

fileName=img.filename
fileName = fileName.split("\\")[-1]
img=img.crop((int(x), int(x), int(x)+int(widht), int(y)+int(height)))
img.show()

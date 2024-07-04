#C:\Users\d48457362\Desktop\Programacion\capeta con img
from PIL import Image
import os,pathlib,random
ListaDeImagenes=[]
ListaDeExtenciones=["JPG","PNG","GIF","TIFF","PSD","BMP","WEBP","JPEG","BMP","HEIC"]
def getResolution(values):
    if values.count(",")==1:
        values=values.split(",")
        for value in values:
            if value.isdecimal()==False:
                return getResolution(input("inserte una resolucion separando con coma los valores de ancho y alto "))
    else:
        return getResolution(input("inserte una resolucion separando con coma los valores de ancho y alto "))
    return [int(values[0]),int(values[1])]

def getRuta(ruta,ListaDeImagenes):
    if os.path.exists(ruta):
        carpeta = pathlib.Path(ruta)
        for rutaImg in carpeta.iterdir():
            name=rutaImg.name
            extencion=name.split(".")[-1]
            if extencion.upper() in ListaDeExtenciones:
                ListaDeImagenes.append(rutaImg)
       
        if len(ListaDeImagenes)>=9:
            return ListaDeImagenes
        else:    
            return getRuta(input("inserte la ruta de una carpeta con 9 imagesnes o más "),[])
    else:
         return getRuta(input("inserte una ruta que exista "),[])
        
   
ListaDeImagenes=getRuta(input("inserte la ruta de la carpeta "),[])
resolucion=getResolution(input("inserte una resolucion separando con coma los valores de ancho y alto "))

collage = Image.new('RGB', (resolucion[0],resolucion[1]))
countEnX=0
countEnY=0
ComenzarCountY=False
matrixVerificadora=[]

for fila in range(resolucion[0]):
    matrixVerificadora.append([])
    for columna in range(resolucion[1]):
        matrixVerificadora[fila].append(0)

def revisarTamaños(resolucion,matrixVerificadora):
    RegistroAncho=[0]
    RegistroAlto=[0]
    count=0
    countX=1
    liberarY=False
    for img in ListaDeImagenes:
        ancho=random.randint(RegistroAncho[ListaDeImagenes.index(img)], round(resolucion[0]/2)+RegistroAncho[ListaDeImagenes.index(img)]) 
       
        if len(RegistroAncho)>0:
            if ancho>=resolucion[0] and RegistroAncho[ListaDeImagenes.index(img)-1]==len(matrixVerificadora[0]):
                ancho=random.randint(0, round(resolucion[0]/2)) 
                print(ListaDeImagenes.index(img)+1,ancho)

        if ancho==0 or ancho==RegistroAncho[ListaDeImagenes.index(img)]:
            ancho+=1
        alto=random.randint(RegistroAlto[count], round(resolucion[1]/2)+RegistroAlto[count]) 
        if alto==0:
            alto+=1
        for fila in range(RegistroAlto[count],alto):
            if fila>=len(matrixVerificadora):
                alto=alto-1
                break
           
            for columna in range(RegistroAncho[ListaDeImagenes.index(img)],ancho):
                if columna>=resolucion[0]:
                    ancho=ancho-(ancho-len(matrixVerificadora[0]))
                    liberarY=True
                    break
                if matrixVerificadora[fila][columna]==0:
                    matrixVerificadora[fila][columna]=ListaDeImagenes.index(img)+1
                else:
                    ancho=ancho-1
                    break
        RegistroAlto.append(alto)
        RegistroAncho.append(ancho)
        if liberarY==True:
            count+=1
    print(RegistroAncho)
    print(" ")
    print(RegistroAlto)
    print(" ")
    for fila in range(resolucion[0]):
        print(matrixVerificadora[fila])
revisarTamaños(resolucion,matrixVerificadora)



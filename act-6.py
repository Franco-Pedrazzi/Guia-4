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
ancho=random.randint(1, round(resolucion[0]/2)) 
alto=random.randint(1, round(resolucion[1]/2)) 
RegistroAncho=[0]
RegistroAlto=[0]
countEnX=0
countEnY=0
ComenzarCountY=False
for img in ListaDeImagenes:
    img=Image.open(img)
    img=img.resize((ancho,alto))
    collage.paste(img,(RegistroAncho[countEnX],RegistroAlto[countEnY]))
    
    if ComenzarCountY==True:
        RegistroAlto[countEnY]=(alto+RegistroAlto[countEnY])
        RegistroAlto[countEnX]=(alto+RegistroAncho[countEnX])
    else:
        RegistroAlto.append(alto)
        RegistroAncho.append(ancho+RegistroAncho[countEnX])
    ancho=random.randint(1, round(resolucion[0]/2)) 
    alto=random.randint(1, round(resolucion[1]/2)) 
    countEnX+=1   
    if ComenzarCountY==True:
        countEnY+=1 
        if ancho+RegistroAncho[countEnX]>RegistroAncho[countEnX+1]:
            ancho=RegistroAncho[countEnX+1]-RegistroAncho[countEnX]
    
    if ancho+RegistroAncho[countEnX]>=resolucion[0]:
        ancho=resolucion[0]-RegistroAncho[countEnX]
        if ancho<=0:
            countEnX=0
            ComenzarCountY=True
            countEnY+=1 
            ancho=random.randint(1, round(resolucion[0]/2)) 


collage.show()


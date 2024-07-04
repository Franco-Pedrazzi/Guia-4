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
fileName=fileName.replace(f".{formato}","")
color=(0,0,0)
pixeles=img.load()
for y in range(img.height):
    for x in range(img.width):
        if y!=0 and x!=0 and y<img.height-1 and x<img.width-1:
            r= (pixeles[x-1,y-1][0]+ pixeles[x-1,y][0]+ pixeles[x-1,y+1][0]+ pixeles[x,y-1][0]+ pixeles[x,y+1][0]+ pixeles[x+1,y-1][0]+ pixeles[x+1,y][0]+ pixeles[x+1,y+1][0])/8
            g= (pixeles[x-1,y-1][1]+ pixeles[x-1,y][1]+ pixeles[x-1,y+1][1]+ pixeles[x,y-1][1]+ pixeles[x,y+1][1]+ pixeles[x+1,y-1][1]+ pixeles[x+1,y][1]+ pixeles[x+1,y+1][1])/8
            b= (pixeles[x-1,y-1][2]+ pixeles[x-1,y][2]+ pixeles[x-1,y+1][2]+ pixeles[x,y-1][2]+ pixeles[x,y+1][2]+ pixeles[x+1,y-1][2]+ pixeles[x+1,y][2]+ pixeles[x+1,y+1][2])/8
            pixeles[x,y]=(round(r),round(g),round(b))
img.show() 
img.save(f"{fileName}Gaussiano.{formato}")

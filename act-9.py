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
countY=0
x=0
color=(0,0,0)
pixel=10
countX=1
img=img.resize((img.width-img.width%pixel,img.height-img.height%pixel))
img = img.convert('RGB')
pixeles=img.load()

print(img.size)   
       
while x<img.width:
    if countY%pixel==0  and x==pixel*countX-pixel:
        color=pixeles[x, countY]
 
    if countY%pixel!=0 and x==pixel*countX-pixel:

        color=pixeles[x, countY-1]

    pixeles[x, countY] = color
    x+=1
    if x==pixel*countX:
        x=pixel*countX-pixel 
        countY+=1
        
    if countY>=img.height:
        countX+=1
        x=pixel*countX-pixel 
        countY=0
       
            

img.show()
img.save(f"{fileName}Pixelator.{formato}")

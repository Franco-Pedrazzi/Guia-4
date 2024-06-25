from PIL import Image
import os

ruta="C:\Users\d48457362\Desktop\ManoRusa2.png"
img=Image.open(ruta)
img.show()
img.save("ManoRusa.png")

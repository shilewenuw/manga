from PIL import Image
import os  
folder = "/home/shile/manga/engl/out"

def convertImage(imagename):
    if ".jpg" not in imagename:
        return
    print("n: " + imagename)
    img = Image.open(f"{folder}/{imagename}")
    img = img.convert("RGBA")
    #img = img.crop((0, 0, 500, 500))
    datas = img.getdata()
  
    newData = []
  
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
  
    img.putdata(newData)

    s = imagename.split(".")
    s = ".".join([s[0], "png"])
    #print("s " + s)
    img.save(f"{folder}/alpha/{s}", "PNG")
  
for f in os.listdir(folder):
    print(f)
    convertImage(f)

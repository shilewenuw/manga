#!/bin/python3

from PIL import Image
import os  
from argparse import ArgumentParser

parser = ArgumentParser(description='Convert white pixels to transparent pixels')
parser.add_argument('--dir', '-d',
                    type=str,
                    help='directory of the files to be converted',
                    required=True)

parser.add_argument('--out', '-o',
                    type=str,
                    help='directory to store the converted files',
                    required=True)

args = parser.parse_args()

os.chdir(args.dir)

if not os.path.exists(args.out):
    os.makedirs(args.out)

def convertImage(imagename):
    try:
        img = Image.open(imagename)
    except:
        return
    img = img.convert('RGBA')
    datas = img.getdata()
  
    newData = []
  
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
  
    img.putdata(newData)

    s = imagename.split('.')
    s = '.'.join([s[0], 'png'])
    img.save(os.path.join(args.out, imagename), 'PNG')
  
for f in os.listdir(args.dir):
    print(f)
    convertImage(f)

#!/usr/bin/python3

from PIL import Image
import os

import sys

folder = sys.argv[1]

args = sys.argv[2:]
if len(args) == 1 and '-' in args[0]:
    args = range(int(args[0].split('-')[0]), int(args[0].split('-')[1]) + 1)
else:
    args = [int(arg) for arg in args]

width = 5161
height = 7309

uncrop_width = 6071
uncrop_height = 8599

def thresh(img, threshold = 5):
    return img.point(lambda p: 255 * (p > threshold))

def remove_alpha(img):
    background = Image.new('RGBA', img.size, (255,255,255))
    img = Image.alpha_composite(background, img)

def kra2png(filename):
    imagename = filename.split('.')[0][:2] + filename.split('.')[0][2:].zfill(3) + ".png"
    
    print(imagename)
    
    os.system(f'krita {filename} --export --export-filename {imagename}')
    return imagename

def process(imagename):
    
    img = Image.open(f"{imagename}").convert('L')
    img = thresh(img)

    left = (uncrop_width - width)//2
    right = width + left
    top = (uncrop_height - height)//2
    bottom = height + top

    
    if img.width > 2*width: # 2 page spread case
        img = img.crop((left, top, right + width, bottom))
    else:
        img = img.crop((left, top, right, bottom))
    img.save(f"out/{imagename}")

if not os.path.exists(folder + "/out"):
    os.makedirs(folder + "/out")

os.chdir(folder)

def getNum(filename):
    return int(filename.split('pg')[1].split('.')[0])

for f in os.listdir(folder):
    if "pg" not in f or '.kra' not in f  or '~' in f:
        continue
    if args and getNum(f) not in args:
        continue
    process(kra2png(f))

#!/bin/python3

from PIL import Image
import os  
from argparse import ArgumentParser

parser = ArgumentParser(description='converts krita documents to png images, then thresholds, trims, and optionally resizes the image')
parser.add_argument('dir',
                    type=str,
                    help='directory of the files to be converted')

parser.add_argument('htrim',
                    metavar='H',
                    type=int,
                    help='size of horizontal trim in pixels')

parser.add_argument('vtrim',
                    metavar='V',
                    type=int,
                    help='size of vertical trim in pixels')

parser.add_argument('--thresh', '-t',
                    type=int,
                    help='threshold value',
                    default=5)

parser.add_argument('--halve',
                    help='halves the length and width',
                    action='store_true')

parser.add_argument('--out', '-o',
                    type=str,
                    help='directory to store the converted files',
                    default='out')

args = parser.parse_args()

width = 5161
height = 7309
left = 910//2
right = width + left
top = 1290//2
bottom = height + top

os.chdir(args.dir)

def thresh(img: Image, threshold = 5) -> Image:
    """apply binary threshold and return the new image. 
    useful for removing guidelines, pencils, etc.

    Args:
        img (Image): image to be thresholded
        threshold (int, optional): the threshold value. Defaults to 5.

    Returns:
        Image: thresholded image
    """
    return img.point(lambda p: 255 * (p > threshold))

def kra2png(filename: str) -> str:
    """creates a png file from a krita document.

    Args:
        filename (str): krita document (a .kra file)

    Returns:
        str: new png filename
    """
    imagename = filename.split('.')[0] + '.png'
    
    print(imagename)
    
    os.system(f'krita {filename} --export --export-filename {imagename}')
    return imagename

def process(imagename: str, htrim, vtrim, out="out", halve=False):
    """thresholds, crops, and (optionally) halves the length and width of the given image. 
    Saves image to the specified out folder.

    Args:
        imagename (str): filename of the image
        vtrim (int): vertical trim
        htrim (int): horizontal trim
        out (str, optional): directory of where the resulting image is saved. Defaults to 'out'.
        halve (bool, optional): if set, halves the length and width of the image. Defaults to False.
    """
    
    img = Image.open(f'{imagename}').convert('L')
    img = thresh(img)

    left = htrim
    top = vtrim
    right = img.width - htrim
    bottom = img.height - vtrim
    
    width = right - left
    height = bottom - top

    if img.width > 2*width: # 2 page spread case
        img = img.crop((left, top, right + width, bottom))
        if halve:
            img = img.resize((width, height//2), Image.NEAREST)
    else:
        img = img.crop((left, top, right, bottom))
        if halve:
            img = img.resize((width//2, height//2), Image.NEAREST)

    if not os.path.exists(out):
        os.makedirs(out)
    img.save(os.path.join(out, imagename))

for f in os.listdir(args.dir):
    # .kra~ are backup files
    if '.kra' not in f or '.kra~' in f:
        continue

    process(kra2png(f), args.htrim, args.vtrim, out=args.out, halve=args.halve)

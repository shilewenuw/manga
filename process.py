from PIL import Image
import os

folder = '/home/shile/manga/20230217library'

width = 5161
height = 7309
left = 910//2
right = width + left
top = 1290//2
bottom = height + top

if not os.path.exists(folder + '/out'):
    os.makedirs(folder + '/out')

os.chdir(folder)

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

def process(imagename):
    
    img = Image.open(f'{imagename}').convert('L')
    img = thresh(img)

    
    if img.width > 2*width: # 2 page spread case
        img = img.crop((left, top, right + width, bottom))
        img = img.resize((width, height//2), Image.NEAREST)
    else:
        img = img.crop((left, top, right, bottom))
        img = img.resize((width//2, height//2), Image.NEAREST)
    img.save(f'out/{imagename}')

# for f in os.listdir(folder):
#     if '.png' in f:
#         process(f)

for f in os.listdir(folder):
    if '.kra' not in f or '~' in f:
        continue
    process(kra2png(f))

import numpy as np
import os
import cv2
from configs import *

def extract_num(filename):
    return int(filename.split('_')[1].split('.')[0])

for file in os.listdir(raw_dir):
    if not 'jpg' in  file or extract_num(file) not in [32]:
        continue

    print(os.path.join(raw_dir, file))
    img  = cv2.imread(os.path.join(raw_dir, file), 0)
    new_img = np.array(img)
   
    new_img[new_img < 120] = 0
    new_img[new_img >= 120] = 255
    if not cv2.imwrite(os.path.join(out_dir, file), new_img):
        print('saving thresholded image fail')
        break
    continue


    '''
    # circular thresholding - used if the flash on phone is really bright
    cx = 1204
    cy = 1630
    r = 1000

    x = np.arange(0, len(new_img[0]))
    y = np.arange(0, len(new_img))

    mask = (x[np.newaxis,:]-cx)**2 + (y[:,np.newaxis]-cy)**2 < r**2
    
    new_img[np.logical_and(new_img < 120, mask)] = 0
    new_img[np.logical_and(new_img >= 120, mask)] = 255
    new_img[np.logical_and(new_img < 90, np.logical_not(mask))] = 0
    new_img[np.logical_and(new_img >= 90, np.logical_not(mask))] = 255

    
    if not cv2.imwrite(os.path.join(out_dir, file), new_img):
        print('fail')
        break
    '''

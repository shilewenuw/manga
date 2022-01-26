file = 'pg_11'

thresh = 200
use2 = ''

import cv2
import matplotlib.pyplot as plt
from configs import *

img = cv2.imread(f'misc/{file}.jpg', 0)
# plt.imshow(img, 'gray')

import numpy as np
new_img = np.array(img)

print(len(new_img))

#120
new_img[new_img < thresh] = 0
new_img[new_img >= thresh] = 255

if not cv2.imwrite(f'misc/{file}{use2}.jpg', new_img):
    print('fail')
    cv2.imwrite(f'misc/{file}2.jpg', new_img)

file = 'bun'

thresh = 120
use2 = ''

import cv2
import matplotlib.pyplot as plt
from configs import *

img = cv2.imread(f'misc/{file}.jpg', 0)
# plt.imshow(img, 'gray')

import numpy as np
new_img = np.array(img)

data = new_img.flatten()
binwidth = 2

plt.hist(data, bins=range(min(data), max(data) + binwidth, binwidth))
plt.show()

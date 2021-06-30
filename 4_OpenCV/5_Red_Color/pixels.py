import cv2
import numpy as np
from PIL import Image

im = np.array(Image.open("map1.png").convert('RGB'))
sought = [255, 0, 0]
result = np.count_nonzero(np.all(im == sought, axis = 2))
print(result)
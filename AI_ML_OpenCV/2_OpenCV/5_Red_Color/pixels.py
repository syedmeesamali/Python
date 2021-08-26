import cv2
import numpy as np
im = cv2.imread('small.bmp')
whites = [255, 255, 255]                #Always counted as B - G - R not RGB
reds = [0, 0, 255]                #Always counted as B - G - R not RGB
result_white = np.count_nonzero(np.all(im == whites, axis = 2))
result_red = np.count_nonzero(np.all(im == reds, axis = 2))
print(f"White pixels are {result_white}")
print(f"Red pixels are {result_red}")
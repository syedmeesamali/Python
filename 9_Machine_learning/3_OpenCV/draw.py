#From YT OpenCV course referred from "FreeCodeCamp" - Quincy
import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8')
cv.imshow('blank', blank)

#Paint certain color on the image
blank[:] = 0, 255, 0        #Green color code
cv.imshow('Green', blank)

cv.waitKey(0)
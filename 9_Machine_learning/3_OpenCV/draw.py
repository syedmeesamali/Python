#From YT OpenCV course referred from "FreeCodeCamp" - Quincy
import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8')

#Paint certain color on the image
#blank[200:300, 300:400] = 0, 255, 0        #Green color code
#cv.imshow('Green', blank)

cv.rectangle(blank, (0,0), (250, 250), (0, 0, 255), thickness = 2)
cv.imshow('Rectangle', blank)
cv.waitKey(0)
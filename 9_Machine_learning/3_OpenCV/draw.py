#From YT OpenCV course referred from "FreeCodeCamp" - Quincy
import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8')

#Paint certain color on the image
#blank[200:300, 300:400] = 0, 255, 0        #Green color code
#cv.imshow('Green', blank)
cv.rectangle(blank, (0,0), (blank.shape[0] // 2, blank.shape[0] // 2), (0, 255, 0), thickness = -1)
#cv.imshow('Rectangle', blank)

#Draw a circle now
cv.circle(blank, (blank.shape[0] // 2, blank.shape[0] // 2), 40, (0, 0, 255), thickness = -1)

#Draw a line
cv.line(blank, (0,0), (blank.shape[0] // 2, blank.shape[0] // 2), (255, 255, 0), thickness = 3)
cv.putText(blank, "Ali bhai", (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 150), thickness=2)

cv.imshow('Circle', blank)
cv.waitKey(0)
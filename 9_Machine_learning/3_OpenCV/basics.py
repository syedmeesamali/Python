#From YT OpenCV course referred from "FreeCodeCamp" - Quincy
import cv2 as cv
import numpy as np

img = cv.imread('rsrc/boss.JPG')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

cv.waitKey(0)
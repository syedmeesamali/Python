#From YT OpenCV course referred from "FreeCodeCamp" - Quincy
import cv2 as cv
import numpy as np

img = cv.imread('rsrc/boss.JPG')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
#cv.imshow('Canny', canny)

#Dilating the images
dilated = cv.dilate(canny, (4,4), iterations=3)      #Kernel size of 3 x 3
#cv.imshow('Dilated', dilated)

#Resizing the images as well as cropping
resized = cv.resize(img, (500, 500))
cv.imshow('Resized', resized)

cv.waitKey(0)
#From YT OpenCV course referred from "FreeCodeCamp" - Quincy
import cv2 as cv
import numpy as np

img = cv.imread('rsrc/boss.jpg')
cv.imshow('value', img)
cv.waitKey(0)
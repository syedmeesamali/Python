#From YT OpenCV course referred from "FreeCodeCamp" - Quincy
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('rsrc/boss.JPG')
#cv.imshow('Boss', img)

plt.imshow(img)
plt.show()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Grey', gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#cv.imshow('HSV', hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
#cv.imshow('lab', lab)

cv.waitKey(0)
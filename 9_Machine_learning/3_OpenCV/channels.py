#From YT OpenCV course referred from "FreeCodeCamp" - Quincy
import cv2 as cv
import numpy as np

img = cv.imread('rsrc/boss.JPG')
cv.imshow('Boss', img)

b,g,r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)
print(img.shape)

merged = cv.merge([b, g, r])
cv.imshow("Merged", merged)

cv.waitKey(0)
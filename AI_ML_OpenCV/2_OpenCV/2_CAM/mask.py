#From YT OpenCV course referred from "FreeCodeCamp" - Quincy
import cv2 as cv
import numpy as np

img = cv.imread('rsrc/boss.JPG')
#cv.imshow('Boss', img)


blank = np.zeros(img.shape[:2], dtype = 'uint8')
#cv.imshow('Blank', blank)

#mask = cv.circle(blank, (img.shape[1]//2 + 150, img.shape[0] // 2), 100, 255, -1)
mask2 = cv.rectangle(blank, (img.shape[1]//2 + 150, img.shape[0] // 2), (((img.shape[1]//2) + 300), ((img.shape[0] // 2) + 300)), 255, -1)
#cv.imshow('Blank', mask)

#masked = cv.bitwise_and(img, img, mask = mask)
masked2 = cv.bitwise_and(img, img, mask = mask2)
#cv.imshow('Masked', masked)
cv.imshow('Masked2', masked2)


cv.waitKey(0)
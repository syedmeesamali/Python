#From YT OpenCV course referred from "FreeCodeCamp" - Quincy
import cv2 as cv

import numpy as np

blank = np.zeros((400, 400), dtype = 'uint8')
rect = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('Rectangle', rect)
cv.imshow('Circle', circle)

#Bitwise AND
bitwise_and = cv.bitwise_and(rect, circle)
cv.imshow('Bitwise AND', bitwise_and)

#Bitwise OR
bitwise_or = cv.bitwise_or(rect, circle)
cv.imshow('Bitwise OR', bitwise_or)

cv.waitKey(0)
import sys
import math
import cv2 as cv
import numpy as np
sumof = []

src = cv.imread('lines.jpg')

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
thresh = cv.threshold(gray, 120, 255, cv.THRESH_BINARY_INV)[1]
cnts = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

lines = 0
for c in cnts:
    cv.drawContours(src, [c], -1, (36,255,12), 3)
    lines += 1

print(lines)
cv.imshow("Thresh", thresh)
cv.imshow("Image", src)
print(len(sumof))
cv.waitKey()
#From YT OpenCV course referred from "FreeCodeCamp" - Quincy
import cv2 as cv
import numpy as np

img = cv.imread('rsrc/boss.JPG')
cv.imshow('Boss', img)

def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])      #Tuple of width and height
    return cv.warpAffine(img, transMat, dimensions)

# -x means left shift
# -y means upward shift
translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width/2, height/2)      #Rotate around center

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -70)
#cv.imshow('Rotated', rotated)

#Resizing an image
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
#cv.imshow('Resized', resized)

#Flipping an image
flip = cv.flip(img, 1)
cv.imshow('Flipped', flip)

#Image cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
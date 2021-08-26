import cv2
import numpy as np

#Read the image from same directory where this program is
img = cv2.imread('lines.jpg')


#Convert the image to a gray-scale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

#Use the edge detection method on the image
edges = cv2.Canny(gray, 50, 150, apertureSize = 5)

#It will return r and theta values
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

#Below loop will run till the values are in the range of 2d array
for r, theta in lines[0]:
    #Store value of cos(theta) in a
    a = np.cos(theta)
    #Store value of sin(theta) in b
    b = np.sin(theta)

    #x0 is r . cos (theta)
    x0 = a * r
    y0 = b * r

    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))

    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))

    #Draw line from (x1, y1) to (x2, y2) with color red (0, 0, 255)
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imwrite('detected.jpg', img)


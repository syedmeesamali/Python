import cv2 as cv
img = cv.imread('../rsrc/boss.JPG')
cv.imshow('boss', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)


haar_cascade = cv.CascadeClassifier('haarcascade.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 3)

print(f'No of faces found = {len(faces_rect)}')
for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), thickness=2)
cv.imshow('Detected faces', img)


cv.waitKey(0)
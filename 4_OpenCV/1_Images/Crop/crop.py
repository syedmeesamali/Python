#this program will crop an image into n number of pieces with x and y dims of each 
#piece and save in the same parent folder
import cv2
#install python library open-cv by using 'pip install opencv-python

img = cv2.imread('alphabets.jpg')
for r in range(0, img.shape[0], 214):
    for c in range(0, img.shape[1], 214):
        cv2.imwrite(f"img{r}_{c}.png", img[r:r+214, c:c+214, :])


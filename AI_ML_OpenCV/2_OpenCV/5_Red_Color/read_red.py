import cv2
import matplotlib.pyplot as plt
image = cv2.imread("map1_red.jpg")
h, w, c = image.shape               #height, width, channel
for i in range(h):
    for j in range(w):
        b, g, r = image[i, j]
        if (r>240 and g>240 and b>240):
            b=0
            g=0
            r=255
        else:
            b=255
            g=255
            r=255
        image[i, j] = [r, g, b]
plt.figure(figsize= (20, 10))
plt.imshow(image)
plt.show()
plt.imsave("map11.bmp", image)
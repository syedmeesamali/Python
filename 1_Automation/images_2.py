import os
from PIL import Image
loveImg = Image.open('heart.jpg')
print(loveImg.size)
print(loveImg.filename)

croppedIm = loveImg.crop((335, 345,565,560))
croppedIm.save('cropped.png')

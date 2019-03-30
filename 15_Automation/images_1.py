import os
from PIL import Image
loveImg = Image.open('heart.jpg')
print(loveImg.size)
print(loveImg.filename)

im = Image.new('RGBA', (100, 200), 'purple')
im.save('purpleImage.png')
im2 = Image.new('RGBA', (20, 20))
im2.save('transparent.png')

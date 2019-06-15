import os
from PIL import Image
loveImg = Image.open('heart.jpg')
print(loveImg.size)
print(loveImg.filename)

width, height = loveImg.size
quarterSize = loveImg.resize((int(width/2), int(height/2)))
quarterSize.save('quarterLove.png')
quarterSize.rotate(90).save('rotated.png')
saveItem = loveImg.resize((width, height+200))
saveItem.save('saveItem.png')
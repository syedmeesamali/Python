import os
from PIL import Image

def crop(input, height, width):
    im = Image.open(input)
    imgWidth, imgHeight = im.size
    for i in range(0, imgHeight, height):
        for j in range(0, imgWidth, width):
            box = (j, i, j+width, i+height)
            a = im.crop(box)
            try:
                o = a.crop(area)
                o.save(os.path.join("PNG", "%s", "Letter-%s.png"))
            except:
                pass

crop('alphabets.jpg', 200,200)
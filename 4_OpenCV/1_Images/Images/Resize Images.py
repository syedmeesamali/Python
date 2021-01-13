import os
from PIL import Image

count = 0
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.JPG')):
        continue
    else:
        count = count + 1
        im = Image.open(filename)
        print("File name is {}".format((filename)))
        print("Count now is {}".format(count))
        im2 = im.resize((533,400))
        im2.save(str(count) + "_" + filename)

import os

from PIL import Image
sq_fit_size = 300
logo_file = 'logo.png'

logoIm = Image.open(logo_file)
logoWidth, logoHeight = logoIm

os.makedirs('withlogo', exist_ok = True)
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
       or filename == logo_file:
        continue
    im = Image.open(filename)
    width, height = im.size

    if width > sq_fit_size and height > sq_fit_size:
        

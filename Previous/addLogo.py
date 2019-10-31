import os
from PIL import Image

sq_fit_size = 600
logo_file = 'mylogo.png'
logoIm = Image.open(logo_file).convert("RGBA")
logoWidth, logoHeight = logoIm.size

os.makedirs('withlogo', exist_ok = True)
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == logo_file:
        continue
    im = Image.open(filename)
    width, height = im.size

    if width > sq_fit_size and height > sq_fit_size:
        if width > height:
            height = int((sq_fit_size / width) * height)
            width = sq_fit_size
        else:
            width = int((sq_fit_size / height) * width)
            height = sq_fit_size
    print("Adding logo to %s" % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
    im.save(os.path.join('withlogo', filename), format="png")

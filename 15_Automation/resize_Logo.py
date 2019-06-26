#This script is for resizing the images as well as adding logo to each image on certain location
import os
from PIL import Image

Fit_Size = 300
logo_Name = 'cropped.png'
logoIm = Image.open(logo_Name)

logo_width, logo_height = logoIm.size

os.makedirs('withlogo', exist_ok= True)
#Loop over the files in the working directory

for filename in os.listdir('.'):
    if not (filename.endswith('.png')) or (filename.endswith('.jpg')) or (filename ==logo_Name):
        continue
    im = Image.open(filename)
    width, height = im.size


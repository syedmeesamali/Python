#This script is for resizing the images as well as adding logo to each image on certain location
import os
from PIL import Image

Fit_Size = 300
logo_Name = 'catlogo.png'
logoIm = Image.open(logo_Name)

logo_width, logo_height = logoIm.size 


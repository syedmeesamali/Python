from PIL import Image
im = Image.new('RGBA',(100,100)) #Create an RGB image
print(im.getpixel((0,0)))  #Get pixels at 0,0 for this new image
from PIL import Image
im = Image.new('RGBA',(100,100)) #Create an RGB image
print(im.getpixel((0,0)))  #Get pixels at 0,0 for this new image

for x in range(100):
    for y in range(50):
        im.putpixel((x,y),(210,210,210))

from PIL import ImageColor
for x in range(100):
    for y in range(50,100):
        im.putpixel((x,y), ImageColor.getcolor('darkgrey','RGBA'))

print(im.getpixel((0,0)))
print(im.getpixel((0,50)))
im.save('putPixel.png')  #Save the image as putPixel
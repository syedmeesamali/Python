from PIL import Image, ImageDraw
im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)
draw.line([(0,0), (199,0), (199,199), (0,199), (0,0)], fill='black')

im.save('drawing.png')

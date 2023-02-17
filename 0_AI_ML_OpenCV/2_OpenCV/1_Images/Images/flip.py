from PIL import Image
catIm = Image.open('cat1.png') #Open the cat image
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')

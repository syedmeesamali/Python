import os
try:
    from PIL import Image
except ImportError:
    import Image
import numpy as np

count = 0
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.JPG')):
        continue
    else:
        count = count + 1
        im = Image.open(filename)
        im = im.convert('RGBA')
        data = np.array(im)   # "data" is a height x width x 4 numpy array
        red, green, blue, alpha = data.T # Temporarily unpack the bands for readability
        # Replace white with green... (leaves alpha values alone...)
        white_areas = (red == 0) & (blue == 0) & (green == 0)
        data[..., :-1][white_areas.T] = (0, 128, 0) # Transpose back needed
        im2 = Image.fromarray(data)
        im2.save(str(count) + "g_" + filename)

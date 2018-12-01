import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
import imageio

photo1 = imageio.imread("E:\Python\cracks.jpg")
print(type(photo1))

low_filter = photo1 < 60
photo1[low_filter] = 0
plt.figure(figsize=(10,10))
plt.imshow(photo1)
plt.show()

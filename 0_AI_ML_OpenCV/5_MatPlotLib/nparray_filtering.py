import random
import numpy as np
import matplotlib.pyplot as plt

arr1 = np.array([[11,12], [21,22], [31,32]])
print("Original Array")
print(arr1)
filter = (arr1 > 15)
print("Filtered print with values more than 15")
print(arr1[filter])
filter2 = ((arr1 > 15) & (arr1 < 30))
print("Filtered print with values more than 15 and less than 30")
print(arr1[filter2])

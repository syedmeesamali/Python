import matplotlib.pyplot as plt
import numpy as np
import random

ys = []
for rep in range(1000):
    y = 0
    for k in range(10):
        x = random.choice([1,2,3,4,5,6])
        y = y + x
    ys.append(y)
plt.hist(ys)
plt.show()

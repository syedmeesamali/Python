import random
import numpy as np
import matplotlib.pyplot as plt

#X_0 will give 0,0 as the origin of the random walker
X_0 = np.array([[0],[0]])
delta_X = np.random.normal(0,1,(2,10000))

X = np.concatenate((X_0, np.cumsum(delta_X, axis=1)), axis=1)
plt.plot(X[0], X[1], "ro-")
plt.show()

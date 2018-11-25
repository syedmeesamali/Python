import numpy as np
import matplotlib.pyplot as plt
X = np.random.randint(1,7,(100,10))
Y = np.sum(X, axis=1)
plt.hist(Y)
plt.show()

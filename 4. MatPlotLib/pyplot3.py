import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(size=1000)
plt.hist(x, normed=True, bins=np.linspace(-5,5,201));
#plt.subplot(3,3,3)
#plt.show()
plt.hist(x,bins=30,cumulative=True,normed=True,histtype="step")
plt.show()

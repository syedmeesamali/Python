import matplotlib.pyplot as plt
import numpy as np

x = np.logspace(-1,1,40)
y = x**2

y1 = x**2.0
y2 = x**1.5
plt.loglog(x,y1,"bo-",linewidth=2,markersize=12, label="First")
plt.loglog(x,y2,"gs-",linewidth=2,markersize=12, label="Second")
plt.xlabel("$X$")
plt.ylabel("$Y$")
plt.axis([-0.5, 10.5, -5, 105])
plt.legend(loc="upper left")
plt.show()

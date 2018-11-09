import matplotlib.pyplot as plt
import numpy as np
plt.plot([0,1,4,9,16])


x = np.linspace(0,10,20)
y = x**2.0
#plt.plot(x,y)
#plt.show()

y1 = x**2.0
y2 = x**1.5
plt.plot(x,y1,"bo-",linewidth=2,markersize=12, label="First")
plt.plot(x,y2,"gs-",linewidth=2,markersize=12, label="Second")
plt.xlabel("$X$")
plt.ylabel("$Y$")
plt.axis([-0.5, 10.5, -5, 105])
plt.legend(loc="upper left")
plt.savefig("myplot.pdf")

plt.show()

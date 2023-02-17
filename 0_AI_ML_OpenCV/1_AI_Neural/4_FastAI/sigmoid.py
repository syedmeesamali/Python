#Just a revision of sigmoids
#Reading short book with title "The Matrix Calculus You Need For Deep Learning"
import numpy as np
import matplotlib.pyplot as plt

#100 points between -10 and 10
input = np.linspace(-10, 10, 100)

#Define sigmoid
def sigmoid(x):
    val = 1 / (1 + np.exp(-x))
    return val

output = sigmoid(input)
plt.plot(input, output)
plt.xlabel("Input")
plt.ylabel("Output")
plt.title("Sigmoid")
plt.show()
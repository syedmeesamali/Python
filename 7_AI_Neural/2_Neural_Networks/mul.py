import numpy as np

a = [1, 2, 3]
b = [2, 3, 4]
a = np.array([a])
b = np.array([b]).T

print(np.dot(a, b))

inputs = [[1.0, 2.0, 3.0, 4.0], 
          [2.0, 5.0, -2.0, 3.0], 
          [-1.7, 2.7, 3.5, 4.25]]

weights = [[0.2, 0.8, -0.6, 1.0], 
          [0.5, -0.91, -0.26, 0.5], 
          [-1.7, 2.7, 3.5, 4.25]]

biases = [2.0, 3.0, 0.5]

print(np.dot(inputs, np.array(weights).T) + biases)


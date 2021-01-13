import numpy as np


inputs = [1, 2, 3, 2.5]
weights = [[0.2, 0.8, -0.5, 1], 
            [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87] ]
biases = [2, 3, 0.5]

output = np.dot(weights, inputs) + biases

# At the back the dot product will be done like this
# [np.dot(weights[0], inputs), np.dot(weights[2], inputs), np.dot(weights[2], inputs),]

print(output)
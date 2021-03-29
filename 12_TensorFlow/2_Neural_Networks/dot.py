import numpy as np
a = [1, 3, 5]
b = [2, 4, 6]
dot_product = a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

print(dot_product)

inputs = a
weights = b
bias = 2.5
output = np.dot(inputs, weights) + bias
print(output)

inputs2 =  [1.0, 2.0, 3.0, -2.5]
weights2 = [[1.0, 2.0, 3.0, -2.5], [1.0, 2.0, 3.0, -2.5], [1.0, 2.0, 3.0, -2.5]]
biases =   [2.0, 3.5, 4.5]

output2 = np.dot(weights2, inputs2) + biases
print(output2)
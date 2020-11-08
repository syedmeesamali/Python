#This is a simple exercise to build neurons and then neural networks from ground-up

inputs = [2.1, 5.2, 3.5]
weights = [3.1, 2.5, 4.7]
bias = 3            #every neuron has unique bias

output = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + bias
#print(output)

inputs = [1, 2, 3]
weights = [0.2, 0.8, -0.5]
bias = 2            #every neuron has unique bias
output2 = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + bias
print(output2)
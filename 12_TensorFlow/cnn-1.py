#This is a simple exercise to build neurons and then neural networks from ground-up
inputs = [1, 2, 3, 2.5]
weights = [[0.2, 0.8, -0.5, 1], 
            [0.5, -0.91, 0.26, -0.5],
           [0.5, -0.91, 0.26, -0.5]   ]


bias1 = 2            #every neuron has unique bias
bias2 = 3
bias3 = 0.5
output = [inputs[0] * weights1[0] + inputs[1] * weights1[1] + inputs[2] * weights1[2] + inputs[3] * weights1[3] + bias1,
          inputs[0] * weights2[0] + inputs[1] * weights2[1] + inputs[2] * weights2[2] + inputs[3] * weights2[3] + bias2,
          inputs[0] * weights3[0] + inputs[1] * weights3[1] + inputs[2] * weights3[2] + inputs[3] * weights3[3] + bias3]

print(output)
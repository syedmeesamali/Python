import numpy as np

def sigmoid(x):
    #This is a classic activation function
    return 1 / (1 + np.exp(-x))

class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):
        #Weight the inputs, add bias and then use the activation function
        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total)

#Below is demonstration of above created nueron
weights = np.array([0, 1])
bias = 4
n = Neuron(weights, bias)
x = np.array([2, 3])            #Inputs for the neuron
print(n.feedforward(x))
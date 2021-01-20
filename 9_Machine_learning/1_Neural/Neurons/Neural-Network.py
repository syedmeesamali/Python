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

class NeuralNetwork:
    '''
    - A simpel neural network with 2 inputs, a hidden layer with 2 neurons
    - An output layer with one neuron
    Each neuron has same weights and biases
    - w = [0, 1]
    - b = 0
    '''
    def __init__(self):
        weights = np.array([0, 1])
        bias = 0

        self.h1 = Neuron(weights, bias)         #First neuron of hidden layer
        self.h2 = Neuron(weights, bias)         #Second neuron of hidden layer
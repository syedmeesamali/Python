import numpy as np

def sigmoid(x):
    #This is a classic activation function
    return 1 / (1 + np.exp(-x))

def deriv_sigmoid(x):
    #Derivative of sigmoid: F'(x) = f(x) * (1 - f(x))
    fx = sigmoid(x)
    return fx * (1 - fx)

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
        self.o1 = Neuron(weights, bias)         #This is the output neuron
        self.w1 = 
    
    def feedforward(self, x):
        out_h1 = self.h1.feedforward(x)
        out_h2 = self.h2.feedforward(x)

        #Inputs to o1 will be the outputs from h1 and h2
        out_o1 = self.o1.feedforward(np.array([out_h1, out_h2]))
        return out_o1

#Mean square error function for training
def mse_loss(y_true, y_pred):
    #y_true and y_pred are numpy arrays of same length
    return ((y_true - y_pred)**2).mean()                #Mean square error

y_true = np.array([1, 0, 0, 1])             #1 is male and 0 is female (refer photo in same folder for table)
y_pred = np.array([0, 0, 0, 0])             #Assuming all as female

print(mse_loss(y_true, y_pred))

# network = NeuralNetwork()
# x = np.array([2, 3])
# print(network.feedforward(x))
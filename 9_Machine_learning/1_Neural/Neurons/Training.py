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

class OurNeuralNetwork:
    '''
    - A simpel neural network with 2 inputs, a hidden layer with 2 neurons (h1, h2)
    - An output layer with one neuron (o1)
    
    '''
    def __init__(self):
        #Define the weights
        self.w1 = np.random.normal()
        self.w2 = np.random.normal()
        self.w3 = np.random.normal()
        self.w4 = np.random.normal()
        self.w5 = np.random.normal()
        self.w6 = np.random.normal()
    
        #Define random biases
        self.b1 = np.random.normal()
        self.b2 = np.random.normal()
        self.b3 = np.random.normal()

    def feedforward(self, x):
        h1 = sigmoid(self.w1 * x[0] + self.w2 * x[1] + self.b1)
        h2 = sigmoid(self.w3 * x[0] + self.w4 * x[1] + self.b2)
        o1 = sigmoid(self.w5 * h1 + self.w6 * h2 + self.b3)
        return o1

    #Main training algorithm
    def train(self, data, all_y_trues):
        '''
        - data is a (n x 2) numpy array, n = # of samples in the dataset.
        - all_y_trues is a numpy array with n elements.
        Elements in all_y_trues correspond to those in data.
        '''
        learn_rate = 0.1
        epochs = 1000           #No. of iterations to check for solution
        for epoch in range(epochs):
            for x, y_true in zip(data, all_y_trues):
                # -- carry out a feed forward
                sum_h1 = self.w1 * x[0] + self.w2 * x[1] + self.b1
                h1 = sigmoid(sum_h1)

                sum_h2 = self.w3 * x[0] + self.w4 * x[1] + self.b2
                h2 = sigmoid(sum_h2)

                sum_o1 = self.w5 * h1 + self.w6 * h2 + self.b3
                o1 = sigmoid(sum_o1)
                y_pred = o1

                #Calculate the partial derivatives
                # -- Naming d_L / d_w1 is represented as "partial L / partial w1"
                d_L_d_ypred = -2 * (y_true - y_pred)

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
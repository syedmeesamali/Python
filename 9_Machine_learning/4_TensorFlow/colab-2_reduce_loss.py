from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


#Define our initial guess
initial_w = 10
initial_b = 10

#Define loss function
def loss(predicted_y, target_y):
    return tf.reduce_mean(tf.square(predicted_y - target_y))

#Define our training procedure
def train(model, inputs, outputs, learning_rate):
    with tf.GradientTape() as t:
        current_loss = loss(model(inputs), outputs)

        #Differentiate model values with respect to loss function
        dw, db = t.gradient(current_loss, [model.w, model.b])

        #Update model values based on the learning rate
        model.w.assign_sub(learning_rate * dw)
        model.b.assign_sub(learning_rate * db)
        return current_loss
        

#Define a simple regression model
class Model(object):
    def __init__(self):
        #Initialize the weights
        self.w = np.array(initial_w)
        self.b = np.array(initial_b)

    def __call__(self, x):
        return self.w * x + self.b

# Define our input data and learning rate
xs = [-1.0, 0.0, 1.0, 2.0, 3.0, 4.0]
ys = [-3.0, -1.0, 1.0, 3.0, 5.0, 7.0]
LEARNING_RATE = 0.09

#Instantiate our model
model = Model()

# Collect the history of w-values and b-values to plot later
list_w, list_b = [], []
epochs = range(50)
losses = []

for epoch in epochs:
    list_w.append(model.w)
    list_b.append(model.b)
    current_loss = train(model, xs, ys, learning_rate = LEARNING_RATE)
    losses.append(current_loss)

print('Epoch %2d: w=%1.2f b=%1.2f, loss=%2.5f' %(epoch, list_w[-1], list_b[-1], current_loss))
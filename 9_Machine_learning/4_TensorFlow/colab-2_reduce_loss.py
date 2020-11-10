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
        
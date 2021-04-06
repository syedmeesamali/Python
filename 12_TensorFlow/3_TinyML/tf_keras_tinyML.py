#Load the tensorflow library
import tensorflow as tf

#Define the custom neural network model
class MyModel(tf.keras.model):
    def __init__(self):
        super(MyModel, self).__init__()

        #Define various layer types
        self.conv = tf.keras.layers.Conv2D(32, 3, activation='relu')
        self.flatten = tf.keras.layers.Flatten()
        self.dense1 = tf.keras.layers.Dense(128, activation='relu')
        self.dense2 = tf.keras.layers.Dense(10)

#Run neural network by running each layer on some input data
def call(self, x):
    x = self.conv(x)
    x = self.flatten(x)
    x = self.dense1(x)
    x = self.dense2(x)
    return x

#Create instance of the model
model = MyModel()

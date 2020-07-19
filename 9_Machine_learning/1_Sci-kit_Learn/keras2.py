import keras
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical

#Packages for CNNs (Convolutional Neural Networks)
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D #for pooling layers
from keras.layers import Flatten

#import the data
from keras.datasets import mnist

#Load the data
(X_train, y_train), (X_test, y_test) = mnist.load_data()

#reshape the data
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1).astype('float32')
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1).astype('float32')

#Let's normalize the values between 0 and 1
X_train = X_train / 255 #normalize the training data
X_test = X_test / 255   #normalize the test data as well

#Let's convert target variables into binary categories
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

num_classes = y_test.shape[1]       #Number of categories

def convolutional_model():
    #Create the model
    model = Sequential()
    model.add(Conv2D(16, (5,5), strides = (1,1), activation = 'relu', input_shape = (28, 28, 1)))
    model.add(MaxPooling2D(pool_size = (2,2), strides=(2,2)))

    model.add(Flatten())
    model.add(Dense(100, activation = 'relu'))
    model.add(Dense(num_classes, activation = 'softmax'))

    #compile the model
    model.compile(optimizer = 'adam', loss = 'categorical_crossentroy', metrics = ['accuracy'])
    return model

#Let's build the model
model = convolutional_model()

#Fit the model
model.fit(X_train, y_train, validation_data = (X_test, y_test), epochs = 10, batch_size = 200, verbose = 2)
print("Accuracy: {} \n Error: {}".format(scores[1], 100-scores[1]*100))

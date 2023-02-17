import tensorflow as tf
import numpy as np
from tensorflow import keras

#Network and training parameters
Epochs = 200
Batch_size = 128
Verbose = 1
NB_Classes = 10         # number of outputs = number of digits
N_hidden = 128
Validation_Split = 0.2  #How much training is reserved for validation

#Load MNIST, verify, and split for training and test
mnist = keras.datasets.mnist
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

reshaped = 784
X_train = X_train.reshape(60000, reshaped)
X_test = X_test.reshape(10000, reshaped)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

#Normalize inputs to be in between (0, 1)
X_train /= 255
X_test /= 255
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')

Y_train = tf.keras.utils.to_categorical(Y_train, NB_Classes)
Y_test = tf.keras.utils.to_categorical(Y_test, NB_Classes)

model = tf.keras.models.Sequential()
model.add(keras.layers.Dense(NB_Classes, input_shape = (reshaped,), name= 'dense_layer', activation='softmax'))

model.compile(optimizer='SGD', loss='categorical_crossentropy', metrics=['accuracy'])

#Training the model
model.fit(X_train, Y_train, batch_size=Batch_size, epochs=Epochs, verbose=Verbose, validation_split=Validation_Split)

#Finally evaluate the model
test_loss, test_acc = model.evaluate(X_test, Y_test)
print('Test accuracy: ', test_acc)


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

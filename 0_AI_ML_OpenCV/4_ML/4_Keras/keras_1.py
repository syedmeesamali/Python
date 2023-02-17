import pandas as pd
import keras
import numpy as np

predictors = np.array([[540.,0.,0.,162.0,2.5,1040.,676.,28],[540.,0.,0.,162.0,2.5,1055.,676.,28]
                     ,[332.5,142.5,0.,228.,0.,932.,594.,270],[332.5,142.5,0.,228.,0.,932.,594.,365]
                     ,[198.6,132.4,0.,192.0,0.,978.4,825.5,360]])

target = np.array([[79.99],[61.89],[40.27],[41.05],[44.3]])

from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
n_cols = predictors.shape[1]

model.add(Dense(5, activation='relu', input_shape=(n_cols,)))
model.add(Dense(5, activation='relu'))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(predictors, target)

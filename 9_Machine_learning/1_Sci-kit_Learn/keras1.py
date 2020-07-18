import keras
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

model = Sequential() #sequential model
concrete_data = pd.read_csv('concrete_data.csv')
concrete_data.head()

concrete_data_columns = concrete_data.columns
predictors = concrete_data[concrete_data_columns[concrete_data_columns != 'Strength']] # all columns except Strength
target = concrete_data['Strength'] # Strength column

#print(predictors.head())
print(target.head())
predictors_norm = (predictors - predictors.mean()) / predictors.std()
predictors_norm.head()

n_cols = predictors_norm.shape[1] # number of predictors

#Define the regression model
def regression_model():
    #Create the model
    model = Sequential()
    model.add(Dense(50, activation='relu', input_shape = (n_cols,)))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(1))

    #Compile the model
    model.compile(optimizer = 'adam', loss = 'mean_squared_error')
    return model

#Train and Test the models

#Compile the model
model = regression_model()
model.fit(predictors_norm, target, validation_split = 0.3, epochs = 100, verbose = 2)
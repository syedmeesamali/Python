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

print(predictors.head())
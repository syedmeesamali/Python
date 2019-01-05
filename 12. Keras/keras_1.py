import pandas as pd
import keras

concrete_data = pd.read_csv('https://ibm.box.com/shared/static/svl8tu7cmod6tizo6rk0ke4sbuhtpdfx.csv')
concrete_data.shape
predictors = concrete_data.iloc[:,0:8]
target =concrete_data.iloc[:,8]

from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
n_cols = concrete_data.shape[1]

model.add(Dense(5, activation='relu', input_shape=(n_cols,)))
model.add(Dense(5, activation='relu'))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(predictors, target)

predictions = model.predict(test_data)

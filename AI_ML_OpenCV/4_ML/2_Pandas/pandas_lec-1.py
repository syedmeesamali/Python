from pandas import DataFrame, read_csv

import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib

print("Python version " + sys.version)
print("Pandas version " + pd.__version__)
print("Matplotlib version " + matplotlib.__version__)

names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]

BabyDataSet = list(zip(names, births))
#print(BabyDataSet)

df = pd.DataFrame(data = BabyDataSet, columns = ['Names', 'Births'])
df.to_csv('births1880.csv', index=False, header=False)

Location = r'C:\Users\SYED\Desktop\Python\5. Pandas\births1880.csv'
df = pd.read_csv(Location)

df = pd.read_csv(Location, names=['Names','Births'])
df['Births'].plot()

MaxValue = df['Births'].max()
MaxName = df['Names'][df['Births'] == df['Births'].max()].values
Text = str(MaxValue) + " - " + MaxName

plt.annotate(Text, xy=(1, MaxValue), xytext = (8,0), xycoords=('axes fraction', 'data'), textcoords='offset points')
plt.show()

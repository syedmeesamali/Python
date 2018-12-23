import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib
import random

#print("Python version " + sys.version)
#print("Pandas version " + pd.__version__)
#print("Matplotlib version " + matplotlib.__version__)

names = ['Bob','Jessica','Mary','John','Mel']

random.seed(500)
random_names = [names[random.randint(0,len(names)-1)] for i in range(1000)]
random_names[:10]

births = [random.randint(0,999) for i in range(1000)]
births[:10]

BabyDataSet = list(zip(random_names, births))
BabyDataSet[:10]
print(BabyDataSet[:10])
df = pd.DataFrame(data = BabyDataSet, columns = ['Names', 'Births'])
df[:10]
df.to_csv('births1880b.txt',index=False,header=False)

Location = r'C:\Users\SYED\Desktop\Python\5. Pandas\births1880b.txt'
df = pd.read_csv(Location, names = ['Names', 'Births'])
print(df.info())
print(df.head(5))
print(df['Names'].unique())

name = df.groupby('Names')
df = name.sum()


df['Births'].plot.bar()
print("The most popular name")
df.sort_values(by='Births', ascending=False)
plt.show()

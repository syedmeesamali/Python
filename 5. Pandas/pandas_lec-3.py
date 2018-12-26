import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np
import random
import sys
import matplotlib

#print("Python version " + sys.version)
#print("Pandas version " + pd.__version__)
#print("Matplotlib version " + matplotlib.__version__)

random.seed(111)

def CreateDataSet(Number = 1):
    Output = []
    for i in range(Number):
        rng = pd.date_range(start = '1/1/2009', end='12/31/2012', freq='W-MON')

        data = np.randint(25,999,size=len(rng))
        status = [1,2,3]
        random_status = [status[np.randint(0, len(status))] for i in range(len(rng))]

        states = ['GA', 'FL', 'fl', 'NY', 'NJ', 'TX']
        random_states = [states[np.randint(0,len(states))] for i in range(len(rng))]

        Output.extend(zip(random_states, random_status, data, rng))
    return Output

dataset = CreateDataSet(4)
df = pd.DataFrame(data=dataset, columns=['State', 'Status', 'CustomerCount', 'StatusDate'])
print(df.head())

Location = r'C:\Users\SYED\Desktop\Python\5. Pandas\Lesson3.xls'
df = pd.read_excel(Location, 0, index_col = 'StatusDate')
print(df.dtypes)

#Prepare data
# 1. Make sure the state column is all in upper case
# 2. Only select records where account status is equal to "1"
# 3. Merge (NJ and NY) to NY in the state column
# 4. Remove any outliers (any odd results in the data set)

print(df['State'].unique())
df['State'] = df.State.apply(lambda x: x.upper())

print(df['State'].unique())
mask = df['Status'] == 1
df = df[mask]
mask = df.State == 'NJ'
df['State'][mask] = 'NY'

print(df['State'].unique())
df['CustomerCount'].plot(figsize=(15,5));
#plt.show()
sortdf = df[df['State'] == 'NY'].sort_index(axis=0)
print(sortdf.head(10))

Daily = df.reset_index().groupby(['State', 'StatusDate']).sum()
print(Daily.head())

del Daily['Status']
print(Daily.head())

Daily.loc['FL']['2012':].plot()
plt.show()

print(Daily.index)

print(Daily.index.levels[0])

StateYearMonth = Daily.groupby([Daily.index.get_level_values(0), Daily.index.get_values(1).year,
                                Daily.index.get_level_values(1).month])
Daily['Lower'] = StateYearMonth['CustomerCount'].transform( lambda x: x.quantile(q=0.25) - (1.5*x.quantile(q=0.75)-x.quantile(q=0.25)) )
Daily['Upper'] = StateYearMonth['CustomerCount'].transform( lambda x: x.quantile(q=0.75) - (1.5*x.quantile(q=0.75)-x.quantile(q=0.25)) )
Daily['Outlier'] = (Daily['CustomerCount'] < Daily['Lower']) | (Daily['CustomerCount'] > Daily['Upper'])

Daily = Daily[Daily['Outlier'] == False]

ALL = pd.DataFrame(Daily['CustomerCount'].groupby(Daily.index.get_level_values(1)).sum())
ALL.columns = ['CustomerCount']

YearMonth = ALL.groupby([lambda x:x.year, lambda x:x.month])
print(ALL.head())

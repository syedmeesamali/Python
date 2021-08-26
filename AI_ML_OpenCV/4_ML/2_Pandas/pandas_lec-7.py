import pandas as pd
import sys

#Create a dataframe with dates as your index
States = ['NY', 'NY', 'NY', 'NY', 'FL', 'FL', 'GA', 'GA', 'FL', 'FL']

data = [1.0, 2, 3, 4, 5, 6, 7, 8, 9, 10]
idx = pd.date_range('1/1/2012', periods=10, freq='MS')
df1 = pd.DataFrame(data, index=idx, columns=['Revenue'])
df1['State'] = States

#Create a second dataframe
data2 = [10.0, 10.0, 9, 9, 8, 8, 7, 7, 6, 6]
idx2 = pd.date_range('1/1/2013', periods=10, freq='MS')
df2 = pd.DataFrame(data2, index=idx2, columns=['Revenue'])
df2['State'] = States

#Combine the two dataframes
df = pd.concat([df1, df2])
print(df)


#Ways to calculate the outliers
#Method-1: make a copy of original df
newdf = df.copy()
newdf['X-Mean'] = abs(newdf['Revenue']-newdf['Revenue'].mean())
newdf['1.96*std'] = 1.96*newdf['Revenue'].std()
newdf['Outlier'] = abs(newdf['Revenue'] - newdf['Revenue'].mean()) > 1.96*newdf['Revenue'].std()
#print(newdf)

#Method-2: Group by item
newdf2 = df.copy()
State = newdf2.groupby('State')
newdf2['Outlier'] = State.transform( lambda x: abs(x-x.mean()) > 1.96*x.std() )
newdf2['x-Mean'] = State.transform( lambda x: abs(x-x.mean()) )
newdf['1.96*std'] = State.transform( lambda x: 1.96*x.std() )
print(newdf2)

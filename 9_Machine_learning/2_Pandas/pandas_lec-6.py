import pandas as pd
import sys

d = {'one':[1,1,1,1,1], 'two':[2,2,2,2,2], 'letter':['a','a','b','b','c']}

df = pd.DataFrame(d)
print(df)

one = df.groupby('letter')
print(one.sum())

letterone = df.groupby(['letter', 'one']).sum()
print(letterone)

print(letterone.index)

letterone = df.groupby(['letter', 'one'], as_index=False).sum()
print(letterone)



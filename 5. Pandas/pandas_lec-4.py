import pandas as pd
import sys

df = pd.DataFrame(list(range(10)))
#print(df)

df.columns = ['Rev']
df['NewCol'] = 5
#print(df)

df['NewCol'] = df['NewCol'] + 1
print(df)
df['test'] = 3
df['col'] = df['Rev']
print(df)
i = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df.index = i
print(df)

print(df.head())
print(df.tail())

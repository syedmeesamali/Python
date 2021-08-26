import pandas as pd
import sys

d = {'one':[1,1], 'two':[2,2]}
i = ['a', 'b']
df = pd.DataFrame(data = d, index = i)
print(df)

stack = df.stack()
print(stack)

unstack = df.unstack()
print(unstack)

transpose = df.T
print(transpose)

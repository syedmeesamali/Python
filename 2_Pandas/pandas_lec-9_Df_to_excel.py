import pandas as pd
import sys

d = [1,2,3,4,5,6,7,8,9]
df = pd.DataFrame(d, columns = ['None'])
print(df)
df.to_excel("Lesson10.xlsx", sheet_name="testing", index = False)

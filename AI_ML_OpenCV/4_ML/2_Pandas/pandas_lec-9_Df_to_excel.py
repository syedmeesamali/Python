import pandas as pd
import sys

d = [1,2,3,4,5,6,7,8,9]
df = pd.DataFrame(d, columns = ['None'])
#print(df)
#df.to_excel("Lesson10.xlsx", sheet_name="testing", index = False)

loc = r"C:\Users\SYED\Desktop\Python\2_Pandas\Lesson10.xlsx"
df = pd.read_excel(loc, 0)
df.head()

#Dataframe export to JSON file
#df.to_json('Lesson10.json')


#Read data from JSON file
loc1 = r"C:\Users\SYED\Desktop\Python\2_Pandas\Lesson10.json"
df2 = pd.read_json(loc1)
print(df2)

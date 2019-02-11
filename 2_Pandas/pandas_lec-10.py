import pandas as pd
import matplotlib as mplot
import os
import sys
'exec(%matplotlib inline)'

d = {'Channel': [1], 'Number': [255]}
df = pd.DataFrame(d)
#print(df)


##df.to_excel('test1.xlsx', sheet_name = 'test1', index = False)
##df.to_excel('test2.xlsx', sheet_name = 'test2', index = False)
##df.to_excel('test3.xlsx', sheet_name = 'test3', index = False)

Filenames = []
os.chdir(r"C:\Users\SYED\Desktop\Python\2_Pandas\update")
for files in os.listdir("."):
    if files.endswith(".xlsx"):
        Filenames.append(files)

#print(Filenames)

def GetFile(fnum):
    loc = r"C:\Users\SYED\Desktop\Python\2_Pandas\update\\" + fnum
    df = pd.read_excel(loc, 0)
    df['File'] = fnum
    return df.set_index(['File'])

df_list = [GetFile(fnum) for fnum in Filenames]
#print(df_list)


bg_df = pd.concat(df_list)
print(bg_df)
plt = bg_df['Channel'].plot.bar();
plt.show()

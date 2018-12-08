import pandas as pd
ser = pd.Series(data = [100,200,300,400,500], index=['ali','tom','bob','nancy','jen'])
print(ser)
#outputs location of nancy
#print(ser.loc['nancy'])
#print(ser[[4,3,1]])
print("Multiply whole series by 2")
print(ser*2)


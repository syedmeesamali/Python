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
#print(df.info())
print(df.head())

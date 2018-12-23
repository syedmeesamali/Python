import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib
import random

print("Python version " + sys.version)
print("Pandas version " + pd.__version__)
print("Matplotlib version " + matplotlib.__version__)

names = ['Bob','Jessica','Mary','John','Mel']

random.seed(500)
random_names = [names[random.randint(low=0,high=len(names))] for i in range(1000)]
random_names[:10]
print(random_names)
births = [random.randint(low=0,high=1000) for i in range(1000)]
births[:10]

BabyDataSet = list(zip(random_names, births))
BabyDataSet[:10]
print(BabyDataSet)

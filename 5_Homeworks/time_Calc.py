import time

def calcProd():
    prod = 1
    for i in range(1,100000):
        prod = prod * i
    return prod

startTime = time.time()
product = calcProd()
endTime = time.time()
print("The result is %s digits long." %(len(str(product))))
print("It took %s seconds to calculate" %(endTime - startTime))

#A list of numbers can be very unsmooth, meaning very high numbers can be right
#next to very low numbers. This list may represent a smooth path in reality
#that is masked with random noise (for example, satellite trajectories with
#inaccurate transmission). One way to smooth the values in the list is to
#replace each value with the average of each value's neighbors, including the
#value itself.

import random
random.seed(1)

def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    result_list = []
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    # To complete the function,
    # return a list of the mean of values from i to i+width for all values i from 0 to n-1.
    i=0
    avg = round((x[i]*2 + x[i+1])/3,2)
    result_list.append(avg)
    while i < n-2:
        i = i + 1
        avg = round((x[i-1] + x[i] + x[i+1])/3,2)
        result_list.append(avg)
    i = i + 1
    avg = round((x[i]*2 + x[i-1])/3,2)
    result_list.append(avg)
    return result_list

x=[0,10,5,3,1,5]
print(moving_window_average(x,1))

print(x)
x = list()

#Below is part-2 of problem where random list is stored in new list and then
#moving_window_average is applied to each item of random list and appended
#to the result list.

for m in range(0,50):
    x.append(random.uniform(0,1))
print("New x is below!")
print(x)

print("New range Y including x is below")
Y = list()
for a in range(1,10):
    Y.append(moving_window_average(x, a))          
Y.insert(0,x)
print(Y)
ranges=list()
for a in range(0,len(Y)):
    ranges.append(max(Y[a])-min(Y[a]))

print("Below list shows the range for max. and min. difference for each set of Y")
print(ranges)

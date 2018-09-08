#A list of numbers can be very unsmooth, meaning very high numbers can be right
#next to very low numbers. This list may represent a smooth path in reality
#that is masked with random noise (for example, satellite trajectories with
#inaccurate transmission). One way to smooth the values in the list is to
#replace each value with the average of each value's neighbors, including the
#value itself.

import random
random.seed(1)

def moving_window_average(input_list, n_neighbors=1):
    n = len(input_list)
    width = n_neighbors*2 + 1
    result_list = []
    # x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    # To complete the function,
    # return a list of the mean of values from i to i+width for all values i from 0 to n-1.
    for i in range(n):
        if i==0:
            avg = (input_list[i]*2 + input_list[i+1])/3
            result_list.append(avg)
        elif i==n-1:
            avg = (input_list[i]*2 + input_list[i-1])/3
            result_list.append(avg)
        else:
            avg = (input_list[i] + input_list[i-1] + input_list[i-1])/3
            result_list.append(avg)
    return result_list

x=[0,10,5,3,1,5]
print(moving_window_average(x,1))

from typing import Tuple
from itertools import combinations

##my_list1 = [-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
##my_list2 = [-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
##my_list3 = [-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]

my_list1 = [0,1,2,3,4,5,6,7,8,9,10]
my_list2 = [0,1,2,3,4,5,6,7,8,9,10]
my_list3 = [0,1,2,3,4,5,6,7,8,9,10]

def sum1(a):
    return a[0] + a[1] - a[2]

def sum2(a):
    return a[0] * a[1] + a[2]

def sum3(a):
    return a[0] + a[1] * a[2]

for i in range(1, len(my_list1)+1):
    for comb in combinations(my_list1, 3):
        for comb2 in combinations(my_list2, 3):
            for comb3 in combinations(my_list3, 3):
                if sum1(comb3) == 15 and sum2(comb2) == 23 and sum3(comb1) == 50:# and sum2(comb3) == 10:
                    print("Winning Combo")
                    print(comb1)
                    print(comb2)
                    print(comb3)
            

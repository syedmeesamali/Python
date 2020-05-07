from itertools import combinations
#range(-25,25,1)
my_list = [-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
##combinations = itertools.combinations(my_list, 3)
##print [result for result in combinations if sum(result) == 10]
for i in range(1, len(my_list)+1):
    for comb in combinations(my_list, 3):
        if sum(comb) == 10:
            print(comb)

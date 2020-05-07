import itertools

nums = range(1,25)
chose1 = 19
result = [seq for i in range(len(nums), 0, -1) for seq in itertools.combinations(nums,i) if sum(seq) == chose1]
print(result)

list_alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z']

def make_list(n_ints):
    return list([x for x in range(1, n_ints)])
nums = make_list(27)
nums_list = [chr(96+x) for x in nums]
map_list = dict(zip(list_alphabets, nums))
list_final = dict(zip(list_alphabets, nums_list))
print(list_final)

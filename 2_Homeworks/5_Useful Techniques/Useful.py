#Now you don’t have to use indexes to access your
#features but instead can use human-understandable names.
from collections import namedtuple
Features = namedtuple('Features', ['age', 'gender', 'name'])
row = Features(age=22, gender='male', name='ali')
print("Age is: " + str(row.age))


from collections import Counter
ages = [22, 22, 23, 26, 27, 29, 31, 33, 34, 38, 25, 26, 23]
value_counts = Counter(ages)
print(value_counts.most_common())

# DefaultDict is a dictionary that is initialized with a
#default value when each key is encountered for the first time.
from collections import defaultdict
my_def_dict = defaultdict(int)
for letter in 'the red fox ran as fast as it could':
    my_def_dict[letter] += 1
print(my_def_dict)

import numpy as np

#below will force the np-array to have datatype of "int64"
ex1 = np.array([11.0,12], dtype = np.int64)

#some basic statistical operations
arr1 = 10 * np.random.randn(2,5)
print(arr1)

#Print the array mean
print(arr1.mean())
#Print a mean by ROW
print(arr1.mean(axis = 1))

#Print a mean by COLUMN
print(arr1.mean(axis = 0))

unsorted = np.random.randn(10)
print("Unsorted array")
print(unsorted)
sorted = np.array(unsorted)
sorted.sort()
print("Sorted now")
print(sorted)

#Below some practice for concept of BROADCASTING
arr2 = np.zeros((4,3))
print(arr2)
add_arr = np.array([1,0,2])
y = arr2 + add_arr
print(y)

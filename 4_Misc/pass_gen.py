import random

nums = input("Amount of passwords to generate: ")
nums = int(nums)

length = input("Enter length of password: ")
length = int(length)

chars = 'abcdefghijklmnopqrstuvwxyz.123456789$_-[]<>'

print("\nBelow are possible password!")
for pwd in range(nums):
    password = ''
    for val in range(length):
        password += random.choice(chars)
    print(password)


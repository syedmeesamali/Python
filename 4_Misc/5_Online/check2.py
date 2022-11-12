"""
Demonstration of logical expressions.
"""

# Boolean values are True and False
value1 = True
value2 = False
print(value1, value2)

print("")

# Logical NOT
print("Logical NOT")
print("===========")
print(not value1)
print(not value2)

print("")

# Logical AND
print("Logical AND")
print("===========")
print(value1 and value1)
print(value1 and value2)
print(value2 and value2)

print("")

# Logical OR
print("Logical OR")
print("==========")
print(value1 or value1)
print(value1 or value2)
print(value2 or value2)

print("")

value3 = True
value4 = True

print(value2 or ((value1 and value4) or value3))

def greet(friend, money):
    if friend and (money > 20):
        print("Hi")
        money = money - 20
    elif friend:
        print("Hello friend")
    else:
        print("Ha hahahahah")
        money = money - 10
    return money


money = 25
money = greet(True, money)

'''

Write a Python function \color{red}{\verb|is_even|}is_even that takes as input the parameter \color{red}{\verb|number|}number (an integer) and returns \color{red}{\verb|True|}True if \color{red}{\verb|number|}number is even and \color{red}{\verb|False|}False if \color{red}{\verb|number|}number is odd. Hint: Apply the remainder operator to \color{red}{\verb|n|}n (i.e., \color{red}{\verb|number % 2|}number % 2) and compare to zero. Even template --- Even solution

'''

def evens(val):
    if val % 2 == 0:
        print("Even")
    else:
        print("Odd")

evens(5)
evens(24)

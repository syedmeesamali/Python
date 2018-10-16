def add(a,b):
    return a+b

def factorial(n):
    if n<=0:
        return 1
    else:
        return n * factorial(n-1)

def circle_area(radius):
    result = math.pi * raidus **2
    return result

def isEven(num):
    if num % 2 == 0:
        return "YES"
    else:
        return "NO"

def blastoff(n):
    if n<=0:
        print("Blast off")
    else:
        print(n)
        blastoff(n-1)

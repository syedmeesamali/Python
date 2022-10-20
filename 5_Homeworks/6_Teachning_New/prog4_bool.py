x = float(input("Enter a number (such as 3.5 or 4.5): "))
y = float(input("Enter a second number: "))

if x == y:
    print("They are same")
else:
    if x > y:
        print("First is larger")
    else:
        print("First is smaller")
    if -0.01 < x - y and x - y < 0.01:
        print("Numbers are close")
    if x == y + 1 or x == y - 1:
        print("Numbers are 1 apart")
    if x > 0 and y > 0 or x < 0 and y < 0:
        print("Numbers have same sign")
    else:
        print("Numbers have different sign")
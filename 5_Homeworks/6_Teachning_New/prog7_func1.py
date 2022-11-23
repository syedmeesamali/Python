def main():
    x = int(input("Enter value: "))
    result = calculateCube(x)
    result2 = CalculateRoot(x)
    print("Cube is: ", result)
    print("Cube root is: ", result2)


def calculateCube(a):
    if a > 0:
        return a ** 3
    else:
        return 0

def CalculateRoot(a):
    if a > 0:
        return a ** (1/3)
    else:
        return 0

main()
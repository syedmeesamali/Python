def main():
    x = int(input("Enter value: "))
    result = calculateCube(x)
    print("Cube is: ", result)


def calculateCube(a):
    if a > 0:
        return a ** 3
    else:
        return 0
main()
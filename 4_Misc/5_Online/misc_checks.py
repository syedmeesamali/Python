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
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print(a+b)

#Function to concatenate two lists item by item
def concat(a: list, b: list) -> list:
    ans = []
    for i in range(3):
        for j in range(3):
            ans[j] = a[j] + b[j]
        ans[i] = a[i] + b[i]
    return ans

print(concat(a, b))
import math
w = 3
b = -1
x = [-1, 0, 1, 2, 3, 4]
y = [-3, -1, 1, 3, 5, 7]

myY = []            #Our result or final guess Y

for thisX in x:
    thisY = (w * thisX) + b
    myY.append(thisY)

print("Real Y is: " + str(y))
print("My guessed Y is: " + str(myY))

#Let's calculate the loss now
total_square_error = 0
for i in range(0, len(y)):
    square_error = (y[i] - myY[i]) ** 2
    total_square_error += square_error

print("My loss is: " + str(math.sqrt(total_square_error)))

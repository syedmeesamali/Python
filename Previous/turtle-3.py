from turtle import *
for angle in range(0,360,30):
    setheading(angle)
    forward(200)
    write(str(angle)+ '*')
    backward(200)

for j in range(47):
    undo()

write(str(j)+ ' times')

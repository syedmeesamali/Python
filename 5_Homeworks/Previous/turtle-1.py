from turtle import *
color('red','yellow')
begin_fill()
while True:
    forward(150)
    left(110)
    if abs(pos()) < 1:
        break
end_fill()

turtle.pos(-200,0)
turtle.seth(0)

from turtle import *
colors = ['red','purple','orange','blue','green','yellow']
for i in range(360):
    pencolor(colors[i % 6])
    width(i/100 + 1)
    forward(i)
    left(58)

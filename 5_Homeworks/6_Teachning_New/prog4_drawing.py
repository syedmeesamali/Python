from sys import exit
from graphics import *

x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x < 0 or y < 0:
    exit("Enter greater than 0 only !!!")
win = GraphWin("My Circle", 100, 100)
oval = Circle(Point(x, y), 10)
oval.draw(win)
win.getMouse()

win.close()
#filling line and angle shapes; using gradiant color
import turtle
from Rodneyfunctions import*
turtle.colormode(255)
bob.width(5)
bob.speed(0)
import random


x = -900
y = 500
jump(x, y)
for times in range(225):
    c = (125,times,125)
    bob.color(c)
    bob.forward(2000)
    jump(x,y-times*5)

#shapes and fillcolor
bob.begin_fill()
jump(-200,100)
bob.color("yellow")
for times in range(5):
    bob.forward(400)
    bob.right(144)
bob.end_fill()







import turtle
import random
import time

x = 0
y = 0
ox = [10,0,-10,0]
oy = [0,10,0,-10]
def check(x,y):
    return (x*x + y*y <= 10000)
direction = 0
kame = turtle.Turtle()
kame.shape('turtle')
kame.penup()
kame.goto(0,-100)
kame.pendown()
kame.circle(100)
kame.penup()
kame.goto(0,0)
kame.pendown()

while True:
    angle = 0
    while True:
        angle = random.randint(0,3)
        if (check(x + ox[(direction + angle) % 4], y + oy[(direction + angle) % 4])):
            break
    print(x,y, kame.pos())
    direction = (direction + angle) % 4
    x+=ox[direction]
    y+=oy[direction] 
    kame.left(angle * 90)
    kame.forward(10)

    

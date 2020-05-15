import turtle
import random

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
        if (kame.distance(0,0) > 100):
            kame.undo()
        angle = random.randint(0,3)
        kame.left(angle * 90)
        kame.forward(10)
        

    

import turtle
kame = turtle.Turtle()
def koch(kame, length, level):
    if (level == 0):
        kame.forward(length)
        return
    new_length = length/3
    koch(kame,new_length,level-1)
    kame.left(60)
    koch(kame,new_length,level-1)
    kame.right(120)
    koch(kame,new_length,level-1)
    kame.left(60)
    koch(kame,new_length,level-1)
koch(kame, 100, 2)
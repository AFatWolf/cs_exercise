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
def koch_snow(kame, length, level):
    kame.left(60)
    koch(kame,length,level)
    kame.right(120)
    koch(kame,length,level)
    kame.right(120)
    koch(kame,length,level)
koch_snow(kame, 200, 3)
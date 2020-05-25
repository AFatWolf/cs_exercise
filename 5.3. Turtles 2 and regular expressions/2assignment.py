import turtle
import re
import time
angle = {'F':0, 'L':90, 'B':180, 'R':270}
direction = {'F':'forward', 'B':'backward', 'L':'left', 'R':'right'}
def turtle_init():
    kame = turtle.Turtle()
    kame.shape('turtle')
    return kame  
def input_command():
    command = input()
    if re.fullmatch('^(F|L|B|R)((\d)*)$', command):
        match = re.fullmatch('^(F|L|B|R)((\d)*)$', command)
        method = match.group(1)
        parameter =int(match.group(2))
        return method, parameter
    return "Wrong input",""
def moving_turtle(kame,method,parameter):
    kame.left(angle[method])
    kame.forward(parameter)
    kame.left(360 - angle[method])
# Main code
kame = turtle_init()
while True:
    method,parameter = input_command()
    # print(method, parameter)
    if (method != "Wrong input"):
        moving_turtle(kame,method,parameter)
        print("Move "+ direction[method] + " by " + str(parameter) + " step(s).")
    

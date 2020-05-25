import turtle
import re
import time
angle = {'forward':0, 'left':90, 'backward':180, 'right':270}
direction = {'F':'forward', 'B':'backward', 'L':'left', 'R':'right'}
def turtle_init():
    kame = turtle.Turtle()
    kame.shape('turtle')
    return kame  
def input_command():
    command = input()
    if re.search('(forward|left|backward|right)', command.lower()):
        method = re.search('(forward|left|backward|right)', command.lower()).group(0)
        parameter = int(re.search('\d+',command).group(0))
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
        print("Move "+ method + " by " + str(parameter) + " step(s).")
    

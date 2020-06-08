import math
def fan(a,r):
    s = r*r*math.pi
    return s * a/360
print(fan(30, 10))
print(fan(90, 10))
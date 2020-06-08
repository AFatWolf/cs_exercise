import random
import math
def gcd(x,y):
    if (x > y):
        x,y = y,x
    if x == 0:
        return y
    return gcd(y%x, x)
def common_multiple(x, y):
    GCD = gcd(x,y)
    return int(x * y / gcd(x,y))
print(common_multiple(12, 16))
print(common_multiple(13, 7))
print(common_multiple())
for i in range(20):
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    print(a,b)
    if math.gcd(a,b) != gcd(a,b):
        print("WRONG ANSWER")
        
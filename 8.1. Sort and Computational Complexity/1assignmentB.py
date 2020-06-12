class Animal:
    def __init__(self, nm, spd):
        self.name = nm
        self.speed = spd
def func(a):
    return a[1]
x = ["mokey", 10]
y = ["Bao", 100]
z = ["X-factor", 20]
a = [x,y,z]

for x in sorted(a, key = func):
    print(x[0])
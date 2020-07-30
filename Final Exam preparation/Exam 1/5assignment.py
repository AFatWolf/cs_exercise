class Person:
    def __init__(self,h,w):
        self.height = h
        self.weight = w
    def diff(self):
        return self.height - self.weight
p1 = Person(170, 60)
p2 = Person(155, 50)
print(p1.diff())
print(p2.diff())

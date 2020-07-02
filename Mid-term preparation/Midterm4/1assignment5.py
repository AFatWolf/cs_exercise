class Circle:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
    def distance(self, other):
        d = (self.x - other.x)*(self.x - other.x) + (self.y - other.y)*(self.y - other.y)
        return d ** (1/2)
    def contains(self, other):
        return self.r >= other.r + self.distance(other)
c2 = Circle(0,0,1)
print(Circle(3,0,1).contains(c2))
print(Circle(3,0,2).contains(c2))
print(Circle(3,0,4).contains(c2))
print(Circle(3,0,5).contains(c2))
print(Circle(10,20,23.3).contains(c2))
print(Circle(10,20,23.4).contains(c2))


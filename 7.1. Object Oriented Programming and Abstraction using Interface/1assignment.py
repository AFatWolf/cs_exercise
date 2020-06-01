import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        xdiff = self.x - other.x
        ydiff = self.y - other.y
        return math.sqrt(xdiff ** 2 + ydiff ** 2)
p1 = Point(2,3)
p2 = Point(4,7)
print('distance of p1 and p2:', p1.distance(p2))
import math
class Point:
    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
    def distance(self, point):
        return math.sqrt((self.x_coordinate - point.x_coordinate) ** 2 
        + (self.y_coordinate - point.y_coordinate) ** 2)
a = Point(1,2)
b = Point(2,3)
print(a.distance(b))
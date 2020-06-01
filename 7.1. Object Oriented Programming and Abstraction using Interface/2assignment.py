class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h
    def area(self):
        return self.width * self.height
r = Rectangle(5, 4)
print(r.width)
print(r.height)
print(r.area())


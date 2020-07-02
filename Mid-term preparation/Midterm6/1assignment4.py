def above(x, y, a, b):
    return (a*x + b < y)
print(above(0, 1, 1, 0))
print(above(0, -1, 1, 0))
print(above(1, 1, 1, 0))
print(above(2, 2/3, -1/3, 1))
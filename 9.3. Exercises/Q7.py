def last(x):
    return x[-1]
l = [(1, 5), (3, 1), (2, 3), (5, 4),  (4, 2)]
l = sorted(l, key = last)
print(l)
def negative_list(xs):
    return [x for x in xs if x < 0]
print(negative_list([2, 20, -6, 4]))
print(negative_list([-3, -2, -1, 0, 1, 2, 3]))
print(negative_list(range(-10,10)))


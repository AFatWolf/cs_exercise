def my_compare(x, y):
    if len(x) == y:
        return 'equal'
    if len(x) > y:
        return 'larger'
    return'smaller'
print(my_compare('apple', 3))
print(my_compare('banana', 7))
print(my_compare('tomato', 6))


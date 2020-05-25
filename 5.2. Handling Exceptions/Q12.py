def filter_odd(lst):
    return [x for x in lst if x % 2 == 1]
print(filter_odd(list(range(0,10))))
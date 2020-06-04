def indivisble_any(xs, p):
    if all(map(lambda x: x % p == 0, xs)):
        return "NOT FOUND"
    return "FOUND"
print(indivisble_any([10,20,30,40], 10))
print(indivisble_any([10,20,30,41], 10))
print(indivisble_any([0,20,30,40], 10))


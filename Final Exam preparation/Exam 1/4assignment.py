def indivisble_any(xs, p):
    for x in xs:
        if (x % p):
            return "FOUND"
    return "NOT FOUND"
print(indivisble_any([10, 20, 30], 10))
print(indivisble_any([10, 21, 30, 60], 10))

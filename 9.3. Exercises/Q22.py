def geo_sum(n):
    if (n < 0):
        return 0
    return 1/ (2**n) + geo_sum(n-1)
print(geo_sum(10))
print(geo_sum(20))

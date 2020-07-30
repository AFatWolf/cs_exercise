def above_avg(xs):
    avg = sum(xs)/len(xs)
    return [x for x in xs if (x > avg)]
print(above_avg([3,4,5]))
print(above_avg([10,5,-20,15]))

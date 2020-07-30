def average_over_40(x):
    xs = [u for u in x if (u > 40)]
    return sum(xs)/len(xs)
print(average_over_40([10, 30, 50, 70, 90]))
print(average_over_40([0, 20, 40, 60, 80, 100]))
def result(p1, p2):
    if (p1 > p2):
        return 'win'
    if (p1 == p2):
        return 'draw'
    return 'lose'
print(result(3, 2))
print(result(0, 1))
print(result(2, 2))

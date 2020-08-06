def cont(xs):
    for i in range(1, len(xs)):
        if (xs[i] == xs[i-1]):
            return True
    return False
print(cont( [ 10, 10, 7, 12 ] ))
print(cont( [ 4, 5, 5, 9 ] ))
print(cont( [ 9, 2, 2, 2 ] ))
print(cont( [ 11, 23, 33, 4 ] ))
print(cont( [ 1,2,1,2,1] ))

    
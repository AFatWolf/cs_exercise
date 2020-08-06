def same_mod2(xs):
    newXs = [x%2 for x in xs]
    val = newXs[0]
    for x in newXs:
        if (x != val):
            return False
    return True
print(same_mod2( [ 2, 4, 8 ] ))
print(same_mod2( [ 11, 3, 7 ] ))
print(same_mod2( [ 11, 6, 7 ] ))
print(same_mod2( [ 11, 0, 7 ] ))
print(same_mod2( [ 1, 3, 13 ] ))


def my_judge(xs):
    check = set()
    for x in xs:
        if (x in check):
            return False
        check.add(x)
    return True
print(my_judge([1,3,2,4]))
print(my_judge([2,5,3,5]))
print(my_judge([4,7,1,6]))
print(my_judge([8,5,3,8]))
print(my_judge([8,5,3,8,8,3]))



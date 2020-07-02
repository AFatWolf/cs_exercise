def my_judge(lst):
    for i in range(1,len(lst)):
        if (lst[i] <= lst[i-1]):
            return False
    return True
print(my_judge([1, 3, 8, 17, 35]))
print(my_judge([2, 7, 22, 70])  )
print(my_judge([2, 4, 3, 12])  )
print(my_judge([3, 5, 8, 8, 10]))  
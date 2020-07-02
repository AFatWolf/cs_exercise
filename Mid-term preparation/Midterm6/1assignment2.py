def my_score(lst, c):
    check = [(x >= c) for x in lst]
    if (sum(check) >= 4):
        return "NICE"
    if (sum(check) > 1):
        return "OK"
    return 'NG'
print(my_score([100, 65, 80, 72, 90], 70))
print(my_score([10, 85, 82, 72, 90], 75) )
print(my_score([20, 61, 90, 52, 40], 70) )
print(my_score([20, 61, 60, 52, 69], 70) )


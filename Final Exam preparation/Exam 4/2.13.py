def divisor(x):
    ans = []
    for i in range(1, x+1):
        if x % i == 0:
            ans += [i]
    return ans
print(divisor(10))
# [1, 2, 5, 10]
print(divisor(144))
# [1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 36, 48, 72, 144]

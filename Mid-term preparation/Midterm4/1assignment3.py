def my_repeat(c):
    ans = 'AB' * (c//2)
    if (c % 2 == 1):
        ans += 'A'
    return ans
for i in range(10):
    print(my_repeat(i))

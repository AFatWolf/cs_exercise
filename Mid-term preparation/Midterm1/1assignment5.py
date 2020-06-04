def common_divisors(x,y):
    ans = []
    for i in range(1, min(x,y)+1):
        if (x % i or y % i):
            continue
        ans.append(i)
    return ans
print(common_divisors(18, 36))
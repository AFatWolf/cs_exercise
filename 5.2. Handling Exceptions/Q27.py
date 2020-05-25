def ternary(n):
    base = [1]
    while (base[-1] * 3 <= n):
        base += [base[-1] * 3]
    ans = ""
    for m in base[::-1]:
        ans += str(n//m)
        n%=m
    return ans
print(ternary(28))
print(ternary(5))
for i in range(1, 20):
    print(i, ternary(i), sep = ":")

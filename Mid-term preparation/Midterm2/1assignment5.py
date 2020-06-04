def combination(n, k):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    for i in range(1,k+1):
        ans /=i
    for i in range(1,n-k+1):
        ans /=i
    return int(ans)
print(combination(10,5))
print(combination(10,3))
print(combination(4,2))


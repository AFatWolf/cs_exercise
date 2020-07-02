def permutation(n, k):
    ans = 1
    for i in range(n-k+1,n+1):
        ans *= i
    return ans
print(permutation(5,2))
print(permutation(10,3))
print(permutation(7,4))


def repeat(xs, n):
    ans = []
    for x in xs:
        ans += [x for i in range(n)]
    return ans
print(repeat(['I', "Have", "a", "pen"], 3))
print(repeat(['I', "Have", "a", "pen"], 1))

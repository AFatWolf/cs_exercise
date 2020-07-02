def binary_search(x, val):
    l = 0
    r = len(x) - 1
    ans = ""
    while(l <= r):
        mid = (l + r + 1)/2
        ans += str(x[mid]) + ","
        if (x[mid] > val):
            r = mid - 1
        else:
            l = mid + 1
    return ans
print(binary_search([5,8,15,22,24,26,32,42,69,71,81,92,96], 92))
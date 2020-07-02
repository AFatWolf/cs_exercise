def binary_search(x, val):
    l = 0
    r = len(x) - 1
    ans = ""
    while(l <= r):
        mid = (l + r + 1)//2
        ans += str(x[mid]) + ","
        if (x[mid] > val):
            r = mid - 1
        else:
            l = mid + 1
    return ans
print(binary_search([19, 23, 37, 38, 42, 47, 53, 56, 62, 65, 67, 70, 76, 77, 96], 37))
def consecutive_wins(lst):
    ans = 0
    cur = 0
    for i in lst:
        if i:
            cur+=1
            ans = max(ans, cur)
        else:
            cur = 0
    return ans
print(consecutive_wins([True, True, False, True, True, True, True]))
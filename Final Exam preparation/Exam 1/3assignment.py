def below_threshold(xs, threshold):
    
    ans = [x for x in xs if (len(x) < threshold)]
    return ans
print(below_threshold(["baseball", "basketball", "swimming"], 10))
print(below_threshold(["baseball", "basketball", "swimming"], 8))

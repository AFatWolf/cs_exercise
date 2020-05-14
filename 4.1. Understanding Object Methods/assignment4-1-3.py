def overlap(xs, ys):
    dic = set({})
    res = set({})
    for s in xs:
        dic.add(s)
    for s in ys:
        if (s in dic):
            res.add(s)
    return list(res)
print(overlap([1,2,3,4,5], [2,3,5,7,11,4]))  

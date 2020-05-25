def find(lst, x):
    return any(xs == x for xs in lst)
print(find([1,2,3,4,5], 5))
print(find(["I", "Love", "Myself"], "love"))

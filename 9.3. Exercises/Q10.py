list1 = ["Apple", "Banana", "Peach", "Apple"]
list2 = ["Banana", "Orange", "Watermelon", "Kiwi", "Banana", "Apple"]
set1 = set(list1)
set2 = set(list2)
ans = set()
for x in set1:
    if (x in set2):
        ans.add(x)
ans = list(ans)
print(ans)
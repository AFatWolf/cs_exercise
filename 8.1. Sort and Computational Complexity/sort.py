a = [5, 2, 3, 1, 4]
print("Before sorting: ", a)
cost = 0
totalCost = 0
for i in range(len(a)):
    min_val = a[i]
    min_pos = i
    cost = 0
    for j in range(i+1, len(a)):
        if a[j] < min_val:
            min_val = a[j]
            min_pos = j
        cost +=1
    print("#", i , ":", cost, "comparision")
    a[i], a[min_pos] = a[min_pos], a[i]
    totalCost += cost
print("After sorting: ", a)
print(totalCost, " steps")

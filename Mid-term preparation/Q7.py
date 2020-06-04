def summer_percentage(temp):
    cnt = [x for x in temp if x >= 30]
    return len(cnt)/len(temp) * 100
temp = [29,28,27,27,31,32,33,28,27,33]
print(summer_percentage(temp), "%")
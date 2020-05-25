def summer_percentage(temp):
    ans = [x for x in temp if x >= 30]
    return len(ans)/len(temp) * 100
print(summer_percentage([29,28,27,27,31,32,33,28,33,28]), "%")
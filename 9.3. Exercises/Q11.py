dic = {1: 2, 3: 0, 4: 3, 0: 1}
dic[2] = 4
print("New dicitionary:", dic)
print("By value:", dict(sorted(dic.items(), key = lambda x: x[1])))
print("By value:", dict(sorted(dic.items(), key = lambda x: x[0])))

def my_function(x):
	return (x % 7 == 0 and x % 5 !=0)
ans = []
for x in range(100, 201):
	if (my_function(x)):
		ans.append(x)
for i in range(len(ans)):
	print(ans[i], end = "")
	if (i != len(ans) - 1):
		print(", ", end = "")
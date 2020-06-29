def average(xs):
	lenEven = 0
	sumEven = 0
	for x in xs:
		if x % 2 == 0:
			lenEven+=1
			sumEven+=x

	return sumEven/lenEven
print(average([1, 2, 3, 4, 5, 6]))
def is_leap_year(year):
	if (year % 400 == 0):
		return True
	if (year % 100 == 0):
		return False
	if (year % 4 == 0):
		return True
	return False
def print_year(year):
	if (is_leap_year(year)):
		return "a leap year"
	return "not a leap year"
for i in range(1900, 2011):
	print(str(i) + ": " + print_year(i))
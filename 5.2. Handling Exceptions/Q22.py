def is_leap(year):
    if year % 100:
        return year % 4 == 0
    return year % 400 == 0
print(is_leap(2017))
print(is_leap(2016))
print(is_leap(2000))
print(is_leap(2100))

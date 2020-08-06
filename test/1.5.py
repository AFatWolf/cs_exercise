import re
def is_num3(s):
    return bool(re.fullmatch(r"^\d{3}$", s))
print(is_num3('123'))
print(is_num3('230'))
print(is_num3('9-9'))
print(is_num3('ABC'))
print(is_num3('12'))
print(is_num3('12A'))
print(is_num3('1234'))
print(is_num3('234c'))

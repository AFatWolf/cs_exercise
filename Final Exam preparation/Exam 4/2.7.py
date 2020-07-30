import re
def intl_phone(x):
    return re.sub("^0", "+81-", x)
print(intl_phone('03-1234-5678'))
print(intl_phone('080-1234-5678'))
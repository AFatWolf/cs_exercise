import re
def check(s):
    return re.fullmatch('0(7|8|9)0-\d{4}-\d{4}', s)
print(check("080-9999-0000"))
print(check("090-1234-5678"))
print(check("aaa-bbb-cccc"))
print(check("03-1234-5678"))  
print(check("000-1234-9876"))

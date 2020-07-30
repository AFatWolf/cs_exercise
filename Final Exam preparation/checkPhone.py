import re
def checkphone(s):
    return bool(re.fullmatch(r"0[789]0-\d{4}-\d{4}", s))
print(checkphone("090-1234-5678"))
print(checkphone("080-9999-0000"))
print(checkphone("080-9999-00a0"))
print(checkphone("060-9999-0000"))
print(checkphone("070-999-0000"))

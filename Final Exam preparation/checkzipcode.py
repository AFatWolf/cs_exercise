import re
def check_zipcode(s):
    if bool(re.fullmatch(r'\d{3}-\d{4}', s)):
        return "OK"
    return "NG"
print(check_zipcode("inoue enryo"))
print(check_zipcode("00-11-22"))
print(check_zipcode("115-005d"))
print(check_zipcode("115-0553"))




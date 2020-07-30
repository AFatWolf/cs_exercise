import re
def ishtml(s):
    return bool(re.match(r'<[^<>]+>', s))
print(ishtml('<p>We are <b>INIAD</b>!</p>'))
print(ishtml('Let us assume: x < 567.8'))
print(ishtml('But not: x >= 1.234'))
import re
def to_minutes(s):
    match = re.fullmatch('(\d*):(\d*)', s)
    
    return (int(match.group(1))*60 + int(match.group(2)))
def time_diff(s1, s2):
    t1 = to_minutes(s1)
    t2 = to_minutes(s2)
    return abs(t1-t2)
print( to_minutes('1:30'))
print(to_minutes('21:15'))
print(time_diff('1:30', '6:30'))
print(time_diff('3:15', '2:50'))

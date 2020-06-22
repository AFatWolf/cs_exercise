import re
def iniad2year(s):
    return "20" + re.search(r"1F10(\d{2})", s).group(1)
print(iniad2year("s1F10200000@iniad.org"))
    
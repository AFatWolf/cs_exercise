import re
def iniad2id(s):
    match = re.search(r"1F10180\d{3}", s)
    print(match.group(0))
iniad2id("s1F10180000@iniad.org")
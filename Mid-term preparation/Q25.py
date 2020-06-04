import re
def receiver(email):
    return re.search(r'(\d{3})\d@iniad.org',email).group(1)
print(receiver('S1f0123456@iniad.org'))
print(receiver('s12223f0123@iniad.org'))
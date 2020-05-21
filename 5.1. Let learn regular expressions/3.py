import re
def us_to_bk(s):
    return re.sub(r'(\d*)/(\d*)/(\d*)', r'\2/\1/\3', s)
print(us_to_bk('9/4/2013'))  


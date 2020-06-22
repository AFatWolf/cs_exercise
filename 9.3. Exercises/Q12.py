import re
s = "033-5924-2600"
if re.fullmatch(r'\d{3}-\d{4}-\d{4}', s):
    print("Match")
else:
    print("Not Match")
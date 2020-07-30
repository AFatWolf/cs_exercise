import re
def changeName(name):
    return re.sub(r"M[rs]\. ([a-zA-Z]+) ([a-zA-Z]+)", r"\2 \1 san", name)
print(changeName("Mr. Tran Ba"))
print(changeName("Ms. Nguyen Uyen"))      
def changeNameFM(name):
    match = re.fullmatch(r"M[rs]\. (\w+) (\w+)")
    return "{} {} san".format(match.group(1), match.group(2))
print(changeName("Mr. Tran Ba"))
print(changeName("Ms. Nguyen Uyen"))      
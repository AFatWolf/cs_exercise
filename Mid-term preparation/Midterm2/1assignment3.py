import re
def abbrev(text):
    return re.sub('[aiueo]', '', text)
print(abbrev("supermarket"))
print(abbrev("I love myself"))
print(abbrev("Toyo university is wonderful")) 


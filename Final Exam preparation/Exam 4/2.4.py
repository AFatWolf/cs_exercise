import re
def noun_to_adj(word):
    return re.sub(r'.*ability$', r".*able$", word)
print(noun_to_adj("ablity"))
print(noun_to_adj("disablity"))



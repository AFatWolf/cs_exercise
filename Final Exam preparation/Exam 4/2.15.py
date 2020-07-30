import re
def past_to_present(word):
    return re.sub("ed$", "ing", word)
print(past_to_present('worked'))
print(past_to_present('programmed'))

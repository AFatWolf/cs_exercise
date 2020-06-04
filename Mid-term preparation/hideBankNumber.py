import re
text = "My bank number is: 000111231345"
print(re.sub("(\d{9})(\d{3})",'*'*9 + "\\2", text))
print(text)
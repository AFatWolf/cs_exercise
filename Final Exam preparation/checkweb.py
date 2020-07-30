import re
def checkweb(link):
    return bool(re.fullmatch(r"https?://.+",link))
print(checkweb("https://moocs.iniad.org/courses/2020/IE101/05-1/04"))
print(checkweb("http://moocs.iniad.org/courses/2020/IE101/05-1/04"))
print(checkweb("http:/moocs.iniad.org/courses/2020/IE101/05-1/04"))
print(checkweb("http://"))


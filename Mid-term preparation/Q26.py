import re
def palindrome(s):
    newString = re.sub('[^a-zA-Z]', "", s)
    print(newString)
    return newString == newString[::-1]
print(palindrome("I love my self .... flesymevoli"))
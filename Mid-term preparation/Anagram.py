def anagram(s1, s2):
    s1 = list(s1)
    s1.sort()
    s2 = list(s2)
    s2.sort()
    return s1 == s2
print(anagram('abbc', "abbc"))
def anagram(s1, s2):
    dic1 = dict()
    dic2 = dict()
    for s in s1:
        if (s in dic1):
            dic1[s]+=1
        else:
            dic1[s] = 1
    for s in s2:
        if (s in dic2):
            dic2[s]+=1
        else:
            dic2[s] = 1
    return dic1 == dic2
print(anagram("dormitory","dirtyroom"))
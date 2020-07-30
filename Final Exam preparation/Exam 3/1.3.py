def count(s):
    return len([x for x in s if (x == 'e')])
print(count('enemies enter from east'))
print(count('GReeeeN'))
print(count(''))
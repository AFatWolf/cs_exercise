def count_caps(words):
    return len([x for x in words if x[0] == x[0].upper()])
in_list = ["A", "Tuyen", "uyen", "love", "iS"]
print(count_caps(in_list))
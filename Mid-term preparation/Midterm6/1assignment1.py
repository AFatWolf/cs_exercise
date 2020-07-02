def my_center(words):
    word_new = sorted(words, key = lambda x : len(x))
    return word_new[1]
print(my_center(['apple', 'pen', 'banana']))
print(my_center(['one', 'three', 'eleven']))
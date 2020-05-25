def max_cont_char(line, c):
    for i in range(len(line), -1,-1):
        if line.find(c*i) != -1:
            return i
print(max_cont_char("oh! woooooww", "w"))
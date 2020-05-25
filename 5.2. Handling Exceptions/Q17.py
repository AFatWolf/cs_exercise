def my_arrow(length, direction):
    ans = "-" * (length-1)
    if direction == 0:
        ans = "<" + ans
    else:
        ans += ">"
    return ans
print(my_arrow(5,0))
print(my_arrow(5,1))
print(my_arrow(4,1))


    
# solution with str.format.
# def mikitani(n):
#     return "{:,}".format(n)

def mikitani(n):
    ans = ""
    while (n):
        if (n >= 1000):
            ans = "," + str(n % 1000) + ans
        else:
            ans = str(n) + ans
        n = int(n/1000)
    return ans
print(mikitani(69))
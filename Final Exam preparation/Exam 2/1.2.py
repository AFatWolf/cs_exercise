def my_limit(x, lower, upper):
    if (len(x) >= lower and len(x) <= upper):
        return "in"
    return "out"
print(my_limit('Apple', 4, 10))
print(my_limit('Toyo', 4, 7))
print(my_limit('INIAD', 2, 5))
print(my_limit('University',2,6))
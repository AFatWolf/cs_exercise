def check_weight(x):
    if (x < 50):
        return "light"
    if (x < 100):
        return "med"
    return "heavy"
print(check_weight(100.0))
print(check_weight(50.0))
print(check_weight(20.0))
def time(seconds):
    if (seconds >= 60):
        return str(seconds//60) + " minutes and " + str(seconds%60) + " seconds"
    return str(seconds) + " seconds"
for i in range(0, 70, 10):
    print(time(i))
print(time(1600))
print(time(120))
print(time(121))
print(time(3599))



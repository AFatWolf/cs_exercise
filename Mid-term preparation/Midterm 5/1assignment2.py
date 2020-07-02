while True:
    cm = int(input('length = '))
    m = cm/100
    if (m < 1):
        print(cm, " centimeters")
    else:
        print(m, " meters")

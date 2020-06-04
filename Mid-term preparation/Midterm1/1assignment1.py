def pound_to_yen(pound):
    return pound*140.6
def yen_to_euro(yen):
    return yen/122.7
pound = float(input("Pound= "))
yen = pound_to_yen(pound)
euro = yen_to_euro(yen)
print(euro, "Euro")
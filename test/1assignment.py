def ms_to_kmh(ms):
    return ms * 3.6
ms = float(input("m/s:"))
kmh = ms_to_kmh(ms)
print(kmh, "km/h")
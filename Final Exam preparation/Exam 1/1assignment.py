def convert(btc):
    return btc * 12345 * 0.9
while True:
    btc = float(input("BTC="))
    euro = convert(btc)
    print(str(euro) + " EUR")
import re
def repl(match):
    yen = float(match.group(1)) * 110.8
    return '{0} yens'.format(yen)
def yen(s):
    # Yen to dollars
    return re.sub(r'(\d*\.?\d*) dollars', repl, s)
print(yen("When I ate ramen in New York, it costed 17 dollars"))
print(yen("Apple for 1 dollars; Orange for 0.5 dollars"))

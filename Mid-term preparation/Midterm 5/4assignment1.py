import re
def yen(s):
    xs = re.findall("(\d+\.?\d*)", s)
    for x in xs:
        s = re.sub(x + " dollars", str(float(x) * 110.8) + " yens", s) 
    return s
print(yen("When I ate ramen in New York, it costed 172 dollars"))
print(yen("When I ate ramen in New York, it costed 17 dollars"))
print(yen("Apple for 1 dollars; Orange for 0.5 dollars"))
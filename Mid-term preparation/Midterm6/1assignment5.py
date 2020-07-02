class MyStr:
    def __init__(self, xs):
        self.xs = xs
    def abbrev(self):
        ans = ""
        for x in self.xs:
            if (x != 'for'):
               ans += x[0]
        return ans
s1=MyStr(['Sustainable','Development','Goals'])
s2=MyStr(['information','networking','for','innovation','and','design', 'for'])
s2=MyStr(['information','networking','for','innovation','and','for', 'for', 'ford'])

print(s1.abbrev())
print(s2.abbrev())
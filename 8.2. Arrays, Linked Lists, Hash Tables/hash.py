class MyDictUsingHashTable:
    def __init__(self):
        self.count = 0
        self.size = 256
        self.mask = 255
        self.table = [None] * self.size
    def pop(self, key):
        t = self.table
        v = None
        i = (hash(key) & self.mask)
        if (t[i].key == key):
            v = t[i].value
            t[i] = None
        else:
            raise
        self.count -= 1
        return v
    def __str__(self):
        s = '< '
        for i in range(self.size):
            if (self.table[i] != None):
                s += str(self.table[i]) + ' '
        s += '>'
        return s
    def setitem(self, k, v):
        i = (hash(k) & self.mask)
        if (self.table[i] == None):
            self.table[i] = _Entry(k,v)
        else:
            if (self.table[i].key == k):
                self.table[i].value = v
            else:
                raise
        self.count += 1
class _Entry:
    def __init__(self, k, v):
        self.key = k
        self.value = v
    def __str__(self):
        return str(self.key) + '-->' + str(self.value)
x = MyDictUsingHashTable()
print(str(x))
x.setitem('apple', 'リンゴ')
print(str(x))
x.setitem('banana', 'ばなな')
print(str(x))
x.pop('banana')
print(str(x))
x.pop('apple')
print(str(x))
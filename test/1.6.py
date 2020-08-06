class Health:
    def __init__(self, n, h, w):
        self.name = n
        self.height = h
        self.weight = w
    def bmi(self):
        return self.weight/(self.height*self.height)
taro = Health('Toyo Taro', 1.7, 70.0)
print(taro.name)
print(taro.height)
print(taro.weight)
print(taro.bmi())
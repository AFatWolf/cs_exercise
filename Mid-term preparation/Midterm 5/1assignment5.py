class Food:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def can_afford(self, amount):
        return (amount >= self.price)
chicken = Food("Fried Chicken Bowl", 380)
mango = Food('Mango Pudding', 270)
print(chicken.name)
print(mango.price)
print(chicken.can_afford(300))
print(mango.can_afford(300))
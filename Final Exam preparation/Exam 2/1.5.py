class Ramen:
    def __init__(self,sp, tp):
        self.soup = sp
        self.topping = tp
    def menu_name(self):
        return self.soup + "-ramen-with-" + self.topping
menu1 = Ramen( 'miso', 'egg' )
menu2 = Ramen( 'shio', 'pork' )
print(menu1.topping)
print(menu2.soup)
name1 = menu1.menu_name()
print(name1)
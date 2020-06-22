class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greeting(self):
        print("Hello my name is " + self.name)
p1 = Person("John", 25)
p1.greeting()
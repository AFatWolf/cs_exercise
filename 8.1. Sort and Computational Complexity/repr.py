class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return repr([self.name, self.age])
    # def __str__(self):
    #     return "My name is " + self.name
Student1 = Student("Tuyen", 20)
print(Student1)
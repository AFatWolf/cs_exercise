from operator import attrgetter, itemgetter
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return repr([self.name, self.age])
    def __lt__(self, other):
        return self.age > other.age
    # def __str__(self):
    #     return "My name is " + self.name
StudentA = Student("Tuyen", 20)
StudentB = Student("uyen", 15)
StudentC = Student("Chuyen", 25)
student_list = [StudentA, StudentB, StudentC]
student_list = sorted(student_list, key = attrgetter('age'))
print(student_list)
student_list = sorted(student_list)
print(student_list)

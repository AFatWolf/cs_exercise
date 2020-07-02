student_tuples = [('john', 2), ("Tuyen", 20), ("Uyen", 19)]
student_tuples = sorted(student_tuples, key = lambda student: student[1])
print(student_tuples)
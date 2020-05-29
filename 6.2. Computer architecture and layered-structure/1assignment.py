import os
path = r"C:\Users\Tuyen Tran\Documents\example\CS_course"
os.mkdir(os.mkdir(path))
with open(path + r"\first.txt", "w") as firstFile: 
    firstFile.write("Python")
with open(path + r"\second.txt","w") as secondFile:
    secondFile.write("Homework")


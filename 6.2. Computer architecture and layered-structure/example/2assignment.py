import os
path = "./CS_course"
with open(path + "/first.txt", "r") as file:
    for line in file:
        print(line)
with open(path + "/second.txt","r") as file:
    for line in file:
        print(line)
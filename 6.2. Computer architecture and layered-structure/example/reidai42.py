import os
path = "../example2/memo2.txt"
with open(path, "r") as file:
    for line in file:
        print(line)
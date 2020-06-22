import os
homepage = os.path.expanduser("~")
l = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open("./color.txt","w") as file:
    for x in l:
        file.write(x + "\n")
with open("./color.txt","r") as file:
    for lines in file:
        print(lines)
import os
homepage = os.path.expanduser("~")
l = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open("./color.txt","w") as file:
    for x in l:
        file.write(x + "\n")
with open("./color.txt","r") as file:
    totalLine = 0
    for lines in file:
        totalLine+=1
    print(totalLine)
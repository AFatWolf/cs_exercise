f = open("collectdata.txt","r")
for line in f:
    print(line.strip().split(","))
# Strip to remove whitespace characters such \n
f.close()
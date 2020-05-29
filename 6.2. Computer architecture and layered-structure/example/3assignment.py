f = open("collectdata.txt","r")
count = 0
japanese_sum = 0
for line in f:
    if line[0] == '#':
        continue
    else:
        ss = line.strip().split(",")
        count+=1
        japanese_sum += int(ss[1])
print("mean score of Japanese is", japanese_sum/count)
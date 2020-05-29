import os
path = "./practice-6-3-1"
os.makedirs(path, exist_ok=True)
with open(path + "/result.txt","w") as file:
    file.write("Tran Ba Tuyen")

import os
os.makedirs(r"../example2", exist_ok=True)
with open("../example2/memo2.txt","w") as file:
    file.write("This is a new memo")

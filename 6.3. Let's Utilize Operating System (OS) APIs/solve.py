import os
path = "./test"
os.makedirs("./test", exist_ok=True)
with open("./test/text.txt","w") as file:
    file.write("test3")
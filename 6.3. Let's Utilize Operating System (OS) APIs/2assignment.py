import requests
import os
# The file was saved in cs_exercise directory.  
postal_code = input()
address = "http://zip.cgis.biz/csv/zip.php?zn=" + postal_code
response = requests.get(address)
os.makedirs("./6", exist_ok=True)
with open("./6/result.csv","w",encoding="utf-8") as file:
    file.write(str(response.text))  
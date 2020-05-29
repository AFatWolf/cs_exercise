import requests
import csv
import re
import os
# The file was saved in cs_exercise directory.  
while True:
    postal_code = input("Please enter your postal code:")
    if (re.fullmatch('^\d{7}$', postal_code)):
        break
    print("Wrong postal code, please input again.")
zip_code = set()
kana = []
kanji = []

# postal_code = "1150053"
address = "http://zip.cgis.biz/csv/zip.php?zn=" + postal_code
response = requests.get(address)
os.makedirs("./6", exist_ok=True)
with open("./6/result.csv","w",encoding="utf-8") as file:
    file.write(str(response.text))
with open("./6/result.csv","r",encoding="utf-8") as file:
    data = csv.reader(file) 
    for row in data:
        for character in row:
            # print(character)
            if (re.fullmatch("^\d{7}$", character)):
                zip_code.add(character)
                continue
            if (re.search("[a-zA-z0-9]+", character)):
                continue
            if (re.search("[ぁ-んァ-ン]",character)):
                kana.append(character)
                continue
            kanji.append(character)
            
print("zip code:", list(zip_code))
print("kana:",kana)
print("Kanji:",kanji)    


import requests
response = requests.get("http://zip.cgis.biz/csv/zip.php?zn=1150053")
print(response.text)  

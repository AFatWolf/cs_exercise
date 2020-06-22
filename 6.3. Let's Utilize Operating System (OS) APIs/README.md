### Let's Utilize Operating System (OS) APIs.  
## **2. Data handling in the computer.**  
- Everything is running in binary numbers in the computer.  
**Hexadecimal and computer**  
- Hexadecimal: number with base 16.  
- How to distinguish among hexadecimal number, decimal number and binary number.  
+ Hex: "0x" is attached.  
+ Binary: "0b".   
+ Decimal: Nothing is attached.  

![hexcharacter](hexcharacter.png)  

**Supplement: Cloud storage appears**  
- Conventional --> All data saved locally.  
- Current --> Data can now be stored not only locally but also cloud storage.  
## **3. OS API**  
- Windows APIs are provided by Windows.  
Start calculator from Python.  
```
impost os
os.system("calc")
```  
Call homepath.  
```
import os
homepath = os.path.expanduser("~")
>>> homepath
>>> 'C:\\Users\\Tuyen Tran'
```  
Call real path:
```
homepage = os.path.realpath(__file__)
```  

## **5. Web API**  
- World Wide Web: An information providing system where documents and other web resources are identified by URLs and presented in a hypertext format.  
--> abbreviated as "Web".  
- Web API: various services on the Internet (cloud services) also provide APIs to provide various functions. Ex: Speech recognition API is one of them.  

**Access the web API**.  
- Search address from zip code API. You can try using the published [Web API](http://zip.cgis.biz/).  
1. Install "requests" with pip.  
2. Create the following program and run it.
```
import requests
response = requests.get("http://zip.cgis.biz/csv/zip.php?zn=1150053")
print(response.text)  
```
Results will look like this:  
```
"ZipSearchXML","1.01","http://zip.cgis.biz/csv/zip.php?zn=1150053","1150053","none","1","1150053","0","1"
"トウキョウト","キタク","アカバネダイ","none","東京都","北区","赤羽台","none"
```  
The information is separated by "," --> CSV(comma-separated values) format.  
**Note:** There is a big different between 'r' and 'w' method. Also, when trying to open csv format, let try to use `encoding="utf-8"`.  
```
with open("./6/result.csv","w",encoding="utf-8") as file:
    file.write(str(response.text))
```  





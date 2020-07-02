# Preparation for Midterm test.  
LP code
```
import pulp
pr = pulp.LpProblem("Farm_mgnt.problem", pulp.LpMaximize)
x = pulp.LpVariable("x", lowBound = 0) # x >= 0
y = pulp.LpVariable("y", lowBound = 0) # y >= 0
pr += 4*x + y <= 36 # condition 1.
pr += 0.2*x + 0.1*y <= 2 # condition 2.
pr += 30*x + 10*y # goal
pr.solve()
P = 30*x.value() + 10*y.value()
print("The maximum value can be achieved at x=" + str(x.value()) + " y=", str(y.value()), "P =", P) 
```  
Binary Search template:  
```
def binary_search(x, val):
    l = 0
    r = len(x) - 1
    ans = ""
    while(l <= r):
        mid = (l + r + 1)/2
        ans += str(x[mid]) + ","
        if (x[mid] > val):
            r = mid - 1
        else:
            l = mid + 1
    return ans
print(binary_search([5,8,15,22,24,26,32,42,69,71,81,92,96], 92))
```  
OS file template:  
Typical file structure operations.  
+ Make directory: `os.mkdir(path)`.  
+ remove directory: `os.rmdir(path)`.  
Typical file operations (*import os is not needed*)  
- open file: `file = open(file_name, mode)`.  
- write into file: `file.write(string)`  
- read from file: `file.read()`
- close file `file.close()`  

Note: `os.makedirs` also is an useful method.  
```
os.makedirs(r"../example2", exist_ok=True)
# exist_ok = True --> overwrite the current folder.
```  
To get the path of the file:
```
base = os.path.dirname(os.path.abspath(__file__))
```  
To look into .txt file:  
```
with open("memo.txt","r") as file:
    for line in file:
        print(line)
```  
To read data from file:  
```
f = open("collectdata.txt","r")
for line in f:
    print(line.strip().split(","))
# Strip to remove whitespace characters such \n
f.close()
```  
Regex:
```

```
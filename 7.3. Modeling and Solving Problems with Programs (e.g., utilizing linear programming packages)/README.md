# Modeling and Solving problems with programs.
## 1. Electronic cash system.  
Let's add more functions for class Bank.  
- Let's modify the class Bank you have created in CS essentials 7.1. 

Write two more methods:  
- `def charge(self, account, yen)` to deposit money in a designated account.  
- Add function to check account balance (Using print method.): `def balance(self, account)`.  

The program is below:  
```
class Bank:
    def __init__(self, amounts):
        self.amounts = amounts.copy()
    def transfer(self, sender, receiver, yen):
        self.amounts[sender] -= yen
        self.amounts[receiver] += yen
    def charge(self, account, yen):
        self.amounts[account] += yen
    def balance(self, account):
        print(self.amounts[account])
```  
Create an instance of a class.  
```
from bank import Bank
bank = Bank({'alice' : 100000, 'bob' : 1234, 'shop' : 100000})
```  
Note: You need to import classes if they are not defined in the file of your main method.  


import os
path = os.path.dirname(os.path.abspath(__file__))
path += "\\Bank"
class Bank:
    def __init__(self, Amounts, name):
        self.name = path + "\\" + name
        self.amounts = {}
        if type(self.amounts) is None:
            self.amounts = Amounts.copy()
        with open(self.name,"r") as file:
            for line in file:
                account, yen = line.split(",")
                self.amounts[account] = int(yen)
    def transfer(self, sender, receiver, yen):
        self.amounts[sender] -= yen
        self.amounts[receiver] += yen
    def charge(self, account, yen):
        self.amounts[account] += yen
    def withdraw(self, account, yen):
        self.amounts[account] -= yen
    def transferFrom(self, bankB, sender, receiver, yen):
        bankB.withdraw(sender, yen)
        self.charge(receiver, yen)
    def balance(self, account):
        print(self.amounts[account])
    def all_balance(self):
        for account in self.amounts:
            print(account + " has " + str(self.amounts[account]) + " yen.")
    def save(self):
        with open(self.name,"w") as file:
            for account in self.amounts:
                file.write(account + "," + str(self.amounts[account]) + '\n')
                # print(account + "," + str(self.amounts[account]))
bankA = Bank(None, "bankA.txt")
bankB = Bank(None, "bankB.txt")
bankA.all_balance()
bankB.all_balance()
bankA.transferFrom(bankB, 'INIAD', 'bob', 1000)
bankA.balance('bob')
bankB.balance('INIAD')
bankA.save()
bankB.save()


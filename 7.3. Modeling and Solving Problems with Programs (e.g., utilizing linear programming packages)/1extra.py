import os
path = os.path.dirname(os.path.abspath(__file__))
path += "\\Bank"
os.makedirs(path, exist_ok=True)
class Bank:
    def __init__(self, data):
        self.data = "data.txt"
        if type(data) is str:
            with open(path + "\\" + data,"r") as file:
                self.data = data
                self.amounts = {}
                for line in file:
                    account, yen = line.split(",")
                    self.amounts[account] = int(yen)
                    self.record("created", account, account, yen, 'w')
        else:
            self.amounts = data.copy()
            for account in self.amounts:
                self.record("created", account, account, self.amounts[account], 'w')

    # update 
    def getPathName(self, account):
        return path + "\\" + account + ".txt"
    def updateHistory(self, pathName, message, tp = 'a'):
        with open(pathName,tp) as file:
            file.write(message + '\n')
    def record(self, typ, sender, receiver, yen, tp = 'a'):
            message = ""
            if typ == 'created':
                message = ("Account " + sender + " is created. " + self.balance(sender))
                self.updateHistory(self.getPathName(sender), message, tp)
            if typ == 'receives':
                message = receiver + " receives " + str(yen) + " Yen from " + sender + ". " + self.balance(receiver)
                self.updateHistory(self.getPathName(receiver), message, tp)
            if typ == "sends":
                message = sender + " sends " + str(yen) + " Yen to " + receiver + ". " + self.balance(sender)
                self.updateHistory(self.getPathName(sender), message, tp)
            if typ == "charge":
                message = str(yen) + " Yen is deposited in account " + sender + ". " + self.balance(sender)
                self.updateHistory(self.getPathName(sender), message, tp)
            return message

    # transactions.
    def transfer(self, sender, receiver, yen):
        self.amounts[sender] -= yen
        self.amounts[receiver] += yen
        self.record("receives", sender, receiver, yen)
        self.record("sends", sender, receiver, yen)
    def charge(self, account, yen):
        self.amounts[account] += yen
        self.record("charge", account, account, yen)

    #get data.
    def getHistory(self,account):
        print(account + "'s history:")
        with open(self.getPathName(account),"r") as file:
            for line in file:
                print(line, end = "")
        print()
    def balance(self, account):
        return "Current balance: " + str(self.amounts[account]) + "."
    def all_balance(self):
        for account in self.amounts:
            print(account + " has " + str(self.amounts[account]) + " Yen.")

    def save(self):
        with open(path + "\\" + self.data,"w") as file:
            for account in self.amounts:
                file.write(account + "," + str(self.amounts[account]) + '\n')
                print(account + "," + str(self.amounts[account]))
            
bank = Bank("data.txt")
bank.charge('bob', 10000)
bank.transfer("bob","shop", 2000)
bank.getHistory("bob")
bank.getHistory("alice")
bank.getHistory("shop")
bank.save()





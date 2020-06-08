class Bank:
    def __init__(self, Amounts):
        self.amounts = Amounts.copy()
    def transfer(self, sender, receiver, yen):
        self.amounts[sender] -= yen
        self.amounts[receiver] += yen
    def charge(self, account, yen):
        self.amounts[account] += yen
    def balance(self, account):
        print(self.amounts[account])
    def all_balance(self):
        for account in self.amounts:
            print(account + "has " + str(self.amounts[account]) + " yen.")
bank = Bank({'enryo' : 5000, 'aki' : 8000, 'mike' : 900})
bank.transfer('enryo', 'mike', 1000)
bank.charge("aki", 2000)
bank.all_balance()


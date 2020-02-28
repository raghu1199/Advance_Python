class BankAccount:

    def __init__(self, name, acc_num, balance=0):
        self.transactions = []
        self.name = name
        self.acc_num = acc_num
        self.balance = balance


class Account:
    li = []

    def create_acc(self, name, acc_num, balance=0):
        self.acc = BankAccount(name, acc_num, balance)  ##object of BankAccount
        Account.li.append(self.acc)

    def deposite(self,amt):
        self.acc.balance+=amt
        self.acc.transactions.append(+amt)
        print(f"{amt} is deposited in {self.acc.name}")

    def withdraw(self,amt):
        self.acc.balance-=amt
        self.acc.transactions.append(-amt)
        print(f"{amt} is withdrawl from {self.acc.name}")

    def recent_tr(self):
        print("recent is:",self.acc.transactions.pop(-1))
        print(self.acc.transactions)

    @staticmethod
    def account_list():
        for acc in Account.li:
            print(acc.name,acc.acc_num,acc.balance)
    @staticmethod
    def manage_account():
        for acc in Account.li:
            if acc.balance<500:
                Account.li.remove(acc)

a=Account()
a.create_acc('Raghu',160130117047)
a.deposite(4050)
a.deposite(3500)
a.withdraw(5500)
a.recent_tr()
b=Account()
b.create_acc("rahul",160130117040)
b.deposite(2000)
b.deposite(4000)
b.withdraw(5000)
b.recent_tr()
Account.account_list()
b.withdraw(600)
b.recent_tr()
print("managing account for low balance")
Account.manage_account()
Account.account_list()


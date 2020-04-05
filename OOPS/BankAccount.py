class BankAccount:
    def __init__(self,name,acc_num,balance=0):
        self.transactions=[]
        self.name=name
        self.acc_num=acc_num
        self.balance=balance
        if self.balance>=500:
            self.lock=False
        else:
            self.lock=True

class Account:
    li=[]
    def create_acc(self,name,acc_num,balance=0):
        self.acc=BankAccount(name,acc_num,balance)
        Account.li.append(self.acc)

    def deposite(self,amt):
        self.acc.balance+=amt
        self.acc.transactions.append(+amt)
        print(f"{amt} is Deposited in {self.acc.name}'s Account")
        if self.acc.balance>=500:
            self.acc.lock=False

    def withdraw(self,amt):
        if not self.acc.lock:
            self.acc.balance-=amt
            self.acc.transactions.append(-amt)
            print(f"{amt} is Withdrawn from {self.acc.name}'s Account")
            if self.acc.balance<=500:
                self.acc.lock=True
        else:
            print(f"Sorry {self.acc.name} Account has been Blocked For Any withdraw Due to Low Balance.Please Deposite some cash")
            print(f"BALANCE IS:{self.acc.balance}")


    def recent_tr(self):
        print("Recent transaction is:",self.acc.transactions[-1])
        print("Total Transactions:",self.acc.transactions)

    @staticmethod
    def account_list():
        print(f"Total Account:{len(Account.li)} \n Details are following. ")
        for acc in Account.li:
            print(acc.name,acc.acc_num,"Balance:",acc.balance,end=" ")
            if acc.lock :
                print("->Withdraw is Blocked Right Now!")
                continue
            print()


    @staticmethod
    def manage_account():
        for acc in Account.li:
            if acc.balance<500 :
                acc.balance-=100
                acc.transactions.append(-100)
                acc.lock=True




raghu=Account()
raghu.create_acc("RAGHU",160130117047)
Account.account_list()
raghu.deposite(5000)
rahul=Account()
rahul.create_acc("RAHUL",160130117040)
ashu=Account()
ashu.create_acc("ASHU",160130117001,4000)
Account.account_list()
rahul.withdraw(500)
rahul.deposite(6000)
Account.account_list()

raghu.withdraw(4500)
raghu.recent_tr()
#Account.manage_account()
Account.account_list()
raghu.withdraw(100)
Account.account_list()
raghu.withdraw(100)
raghu.recent_tr()

ashu.withdraw(3800)
Account.manage_account()
Account.account_list()
ashu.withdraw(50)
ashu.recent_tr()



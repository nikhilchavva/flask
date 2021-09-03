class Bank_Account():
    def __init__(self, name, balance):
        self.name=name
        self.balance=balance
    def withdraw(self, amount):
        if(amount>self.balance):
            print(f"insufficient funds, Available balance is: {self.balance}")
        else:
            self.balance-=amount
            print(f"Available balance after withdrawal: {self.balance}")

    def deposite(self, amount):
        self.balance+=amount
        print(f"Available balance after depositing: {self.balance}")
account = Bank_Account("Hithesh Reddy K", 10000)
print(f"Account details, name:{account.name}, available balance:{account.balance}")
def switch():
    while(True):
        print("Press 1 for Deposit\npress 2 for Withdraw \npress 3 for Exit ")
        option = int(input("your option : "))
        if option == 1:
            amount=(int(input("enter the amount to be deposited: ")))
            account.deposite(amount)
            continue
        elif option == 2:
            amount=(int(input("enter the amount to be withdrawn: ")))
            account.withdraw(amount)
            continue
        elif option == 3:
            print("Thank You")
            break
        else:
            print("Incorrect option")
switch()
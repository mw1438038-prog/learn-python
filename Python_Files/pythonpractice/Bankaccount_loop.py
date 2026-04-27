class BankAccount:
    def __init__(self,balance=0):
        self.balance=balance
    def checkbalance(self):
      return self.balance
    def deposit(self,amount):
        self.balance+=amount
        print('deposit',amount)
        return self.balance
    def withdraw(self,amount):
     if self.balance>=amount:
         print('withdraw',amount)
         self.balance-=amount
     else:
         return "insufficient balance"
    def finishid(self):
        return "Thank you for using Bank system"

myAccount = BankAccount(1000)
myBalance = myAccount.checkbalance()

print(myBalance)
myAccount.deposit(2000)
myAccount.withdraw(3000)
print(myAccount.balance)


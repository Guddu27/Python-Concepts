# Create an account class with 2 attributes : 
    #balance & acount no
#Create methods for debit, credit & printing the balance

class account:
    def __init__(self,bal, acc_no):
        self.balance = bal
        self.accont_no = acc_no
        print("\n------------Welcome to your acount status checking----------------\n")

    #! Debit Method
    def debit(self, amount):
        self.balance -= amount
        print(f"Account Number : {self.accont_no}\n")
        print(f"Rs.{amount} was Debited.")
        print(f"Total Balance : {self.get_balance()}")

    #! Credit Method
    def credit(self, amount):
        self.balance += amount
        print(f"Rs.{amount} was Credited.")
        print(f"Total Balance : {self.get_balance()}")

    #! Function to fetch balance
    def get_balance(self):
        return self.balance

acc1 = account(10000, 5568930038300)
acc1.debit(1000) #! amount argument
acc1.credit(2000)

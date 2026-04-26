#09
#P-2
#=========================================================================#
#Practice Questions
#=========================================================================#
#@1# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.

class Account():
    def __init__(self,balance,account_no):
        self.balance = balance
        self.account_no = account_no
    
    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "is debited.")
        print("total balance =", self.balance)

    
    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "is credited.")
        print("total balance =", self.balance)

    
    def get_balance(self):
        return self.balance
        
acc1 = Account(10000, 28249)
# print(acc1.balance)
# print(acc1.account_no,"\n")

acc1.debit(900)
# print(acc1.balance)

# acc1.credit(500)
# print(acc1.balance)
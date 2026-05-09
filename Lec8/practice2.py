#09
#P-2
#=========================================================================#
#Practice Questions
#=========================================================================#
#@1# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.

class Account():
    def __init__(self,balance,account_no):
        # self -> current object being created
        # balance & account_no -> values passed during object creation
        self.balance = balance
        self.account_no = account_no
    
    def debit(self, amount):
        # accesing current object's attributes using self
        self.balance -= amount
        print("Rs", amount, "is debited.")
        print("total balance =", self.balance)

    
    def credit(self, amount):
        # self -> object calling the method
        # num2 -> secound object passed as argument
        
        # 'amount' is just a parameter name.
        # it can be anything like:
        # other, obj, x, abc etc
        
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
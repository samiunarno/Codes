class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc 
    def debit (self,amount):
        self.balance -= amount
        print("BDT",amount,"was debited") 
    def credit(self,amount):
        self.balance += amount
        print("BDT", amount, "Was Credited")
    def get_balance(self):
        return self.balance    


acc1 = Account(40000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(5000)
print(acc1.balance)           
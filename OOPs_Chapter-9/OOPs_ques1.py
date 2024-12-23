# create account class with 2 attributes - balance and account no. Create a methods for debit & credit and printing the balance.
class Account():
    def __init__(self, bal, acc):
        self.balance = bal
        self.account = acc
    
    def debit(self, account):
        self.balance -account
        print("Rs" , account, "was debited")
        print("total balance = ", self.get_started())
    
    def credit(self, account):
        self.balance += account
        print("Rs.", account, "was credited")
        print("total balance = ", self.get_started())
    
    def get_started(self):
        return self.balance

acc1 = Account(100000000, 12345)
acc1.debit(1000)
acc1.credit(500)


class Student():
    def __init__(self, name):
        self.name = name

s1 = Student("Kriti")
print(s1.name)
del s1.name
print(s1.name)

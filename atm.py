class Atm(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.balance= 1000
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("gender:",self.gender)
        print("balance:",str(self.balance))
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        self.balance=self.balance-amount
arya=Atm("arya","15","male")
arya.display()
arya.deposit(1000000)
arya.display()
arya.withdraw(12345)
arya.display()
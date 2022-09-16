class BankAccount:

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance


    def deposit(self,amount):
        self.balance = self.balance + amount
        print(self.balance)
        return self

    def withdraw(self,amount):
        self.balance = self.balance - amount
        print(self.balance)
        return self

    def display_account_info(self):
        print(self.int_rate)
        print(self.balance)
        return self

    def yield_interest(self):
        self.balance = self.balance * (self.balance * self.int_rate)
        print(self.balance)
        return self

christian =BankAccount(0.01, 100)
stacy =BankAccount(0.01, 100)

christian.deposit(5).deposit(20).deposit(100).withdraw(20).yield_interest()


stacy.deposit(50).deposit(120).withdraw(15).withdraw(30).withdraw(8).withdraw(5).yield_interest()


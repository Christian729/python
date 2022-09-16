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

class User:

    def __init__(self,first_name, last_name, email,age, is_rewards_member, gold_card_points):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email 
        self.age = age 
        self.is_rewards_member= False
        self.gold_card_points=0
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(self.account.balance)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        print(self.account.balance)
        return self

    def display_user_balance(self):
        print(self.account.balance)
        return self

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self
        
    def enroll(self):
        christian.is_rewards_member = True
        christian.gold_card_points = 200
        print()
        return self

    def spend_points(self,amount):
        self.gold_card_points= self.gold_card_points - amount
        print(self.gold_card_points)
        return self



christian = User("Christian","lozano","cl@email.com", 22, True, 200)
stacy = User("Stacy", "Smith", "SSm@email.com", 29, True, 100)
nick = User("Nick", "flores", "NF@email.com", 40, False, 0)


christian.enroll().spend_points(50).display_info().display_user_balance()


stacy.enroll().spend_points(80).display_info().display_user_balance()



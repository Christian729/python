class User:

    def __init__(self,first_name, last_name, email,age, is_rewards_member, gold_card_points):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email 
        self.age = age 
        self.is_rewards_member= False
        self.gold_card_points=0


    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        
    def enroll(self):
        christian.is_rewards_member = True
        christian.gold_card_points = 200
        print()

    def spend_points(self,amount):
        self.gold_card_points= self.gold_card_points - amount
        print(self.gold_card_points)



christian = User("Christian","lozano","cl@email.com", 22, True, 200)
stacy = User("Stacy", "Smith", "SSm@email.com", 29, True, 100)
nick = User("Nick", "flores", "NF@email.com", 40, False, 0)

christian.enroll()
christian.spend_points(50)
christian.display_info()

stacy.enroll()
stacy.spend_points(80)
stacy.display_info()


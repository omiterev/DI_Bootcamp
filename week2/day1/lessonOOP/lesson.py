class ElienDog:
    def __init__(self,breed,nickname,color,age,favoritefood='no', is_trained=False):
        print('object was created')
        self.breed = breed
        self.nickname = nickname
        self.color = color
        self.age = age
        self.favoritefood = favoritefood
        self.is_trained=is_trained
        self.dog_years_age=age*7
    #Methods, behavior of the object
    def bark(self):
        print(f'{self.nickname} is barking')
    
    def sit(self):
        if self.is_trained:
            print(f'{self.nickname} is sitting')
        else:
            print(f'{self.nickname} is not trained')
    
    def rename(self, newname):
        self.nickname=newname
        return self
# creating an object from the class Dog
dog1 = ElienDog('chowchow','Lion','orange', 5,'fish')
dog2 = ElienDog('collie','Laddy','bage and white',15, None, True)
dog2.is_service_dog=True
print(dog1.color)
print(dog1.__dict__)
print(dog2.__dict__)
dog3=ElienDog('labrabor','Rex','golden',7,'Meet',True)

dog3.bark()
ElienDog.bark(dog3)

dog3.sit()
dog1.sit()

dog1.rename('BigLion')
print(dog1.nickname)
my_dogs = [dog1, dog2, dog3]
for dog in my_dogs:
    print(dog.nickname)
    dog.sit
#print(type(dog3))

class BankAccount:

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def view_balance(self):
        self.transactions.append("View Balance")
        print(f"Balance for account {self.account_number}: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}")
            print("Deposit Succcessful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdraw Approved")
            return amount

    def view_transactions(self):
        print("Transactions:")
        print("-------------")
        for transaction in self.transactions:
            print(transaction)

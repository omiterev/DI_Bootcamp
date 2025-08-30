#1
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

all_cats=[Bengal('Mitchel',3), Chartreux('Lex',6), Siamese('Sia',3)]
sara_pets=Pets(all_cats)
def _democat():   
    for cat in sara_pets.animals:
        print(cat.walk())
#2
class Dog:
    def __init__(self, name, age:int, weight:int):
        self.name=name
        self.age=age
        self.weight=weight
        pass
    def bark(self):
        return f'{self.name} is barking'
    def run_speed(self):
        return (self.weight/self.age)*10
    def fight(self,other_dog):
        dog1_strenght=self.run_speed()*self.weight
        dog2_strenght=other_dog.run_speed()*other_dog.weight
        if dog1_strenght>dog2_strenght:
            return self.name
        else:
            return other_dog.name
def _demo():       
    dog1 = Dog("Buddy", 3, 12)
    dog2 = Dog("Max", 5, 20)
    dog3 = Dog("Bella", 2, 8)
    print(dog1.bark())
    print(dog3.run_speed())
    print(dog1.fight(dog3))
if __name__ == "__main__":
    _democat()
    _demo()
#3
from XP_exercises1 import Dog
import random
class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        self.trained=trained
        super().__init__(name, age, weight)
    def train(self):
        print(self.bark())
        self.trained=True
        return self.trained
    def play(self,*args):
        print(f'{", ".join(args)} all play together')
    def do_a_trick(self):
        tricks=["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
        random_trick=random.randint(0, len(tricks)-1)
        if self.trained:
            print(f'{self.name} {tricks[random_trick]}')
        else:
            print(f'{self.name} is not trained')


my_dog1= PetDog("Fido", 2, 15)
my_dog2 = PetDog("Jey", 6, 22)
my_dog3 = PetDog("Bob", 3, 9)
my_dog2.train()
my_dog1.play("Buddy", "Max")
my_dog3.do_a_trick()
my_dog3.train()
my_dog3.do_a_trick()
#4
class Person:
    def __init__(self,first_name,age,last_name:str=''):
        self.first_name=first_name
        self.age=age
        self.last_name=last_name
        pass
    def is_18(self):
        return self.age>18
     
           

class Family:
    def __init__(self,last_name):
        self.last_name=last_name
        self.members=[]
    def born(self,first_name, age:int):
        person=Person(first_name,age,self.last_name)
        return self.members.append(person)
    def check_majority(self,first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print('You are over 18, your parents Jane and John accept that you will go out with your friends')
                else:
                    print('Sorry, you are not allowed to go out with your friends.')
    def family_presentation(self):
        print(self.last_name)
        for person in self.members:
            print(person.first_name, person.age)



family1=Family('Smit')
family1.born('Jane',45)
family1.born('John',52)
family1.born('Luke',8)
family1.born('Nina',19)
family1.check_majority('Luke')
family1.check_majority('Nina')
family1.check_majority('Mike')
family1.family_presentation()
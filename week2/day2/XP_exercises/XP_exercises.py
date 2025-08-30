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
    
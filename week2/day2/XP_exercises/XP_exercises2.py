from XP_exercises import Dog
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

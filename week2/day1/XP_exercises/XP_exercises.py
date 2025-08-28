#1
class Cat:
    def __init__(self, cat_name:str ,cat_age:int):
        self.cat_name=cat_name
        self.cat_age=cat_age
        pass
cat1 = Cat("Tom", 4)
cat2 = Cat("Luna", 1)
cat3 = Cat("Barsik", 3)
cat4 = Cat("Kasandra", 5)
cat5 = Cat("Luk", 5)

def oldest_cat(*cats):
    oldest=cats[0]
    for cat in cats[1:]:
        if cat.cat_age > oldest.cat_age:
            oldest=cat
    return oldest

def oldest_cat2(*cats):
    oldest_cat2=max(cats, key=lambda cat:cat.cat_age)
    return oldest_cat2

oldest1=oldest_cat(cat1, cat2, cat3, cat4, cat5)
oldest2=oldest_cat2(cat1, cat2, cat3, cat4, cat5)

print(f' Oldest cat is {oldest1.cat_name}, age {oldest1.cat_age}.')
print(f' Oldest cat is {oldest2.cat_name}, age {oldest2.cat_age}.')
#2
class Dog:
    def __init__(self, dog_name, dog_height):
        self.dog_name=dog_name
        self.dog_height=dog_height
        pass

    def bark(self):
        print(f'{self.dog_name} goes woof')

    def jump(self):
        print(f'{self.dog_name} jumps {self.dog_height*2} cm high!')

davids_dog  = Dog("Buddy", 30)
sarahs_dog  = Dog("Max", 60)

print(davids_dog.__dict__)
print(sarahs_dog.__dict__)

davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()

def heigtest_dog(*dogs):
    heigtest=max(dogs, key=lambda dog:dog.dog_height)
    return heigtest
heigtest=heigtest_dog(davids_dog,sarahs_dog)
print(f'The heigtest dog is {heigtest.dog_name}.')

#3
class Song:
    def __init__(self,lyrics:list):
        self.lyrics=lyrics
        pass
    def sing_me_a_song(self):
        for line in self.lyrics: 
            print(line)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

#4
class Zoo:
    def __init__(self,zoo_name:str):
        self.zoo_name=zoo_name
        self.animals=[]
        self.animal_dict={}
        pass
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
    def get_animals(self):
        print(self.animals)
    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f'The {animal_sold} is sold')
        else:
            print(f'There is no such animal in the zoo')
    def sort_animals(self):
        self.animal_dict={}
        for animal in self.animals:
            first_letter = animal[0].upper()
            self.animal_dict.setdefault(first_letter,[]).append(animal)
        return self.animal_dict
    def get_groups(self):
        for letter in self.animal_dict:
            print(letter, self.animal_dict[letter])

brooklyn_safari = Zoo("Brooklyn Safari")
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Cat")
brooklyn_safari.add_animal("Cougar")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()
class Farm:
    def __init__(self, farm_name:str):
        self.name=farm_name
        self.animals={} 
        pass

    def add_animal(self, animal_type:str, count:int=1):
        if animal_type in self.animals:
            self.animals[animal_type]+=count
        else:
            self.animals[animal_type]=count

    def get_info(self):
        result=f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            result+=f"{animal} : {count}\n"
        result+="\n    E-I-E-I-0!"
        return result

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_list=self.get_animal_types()
        formatted=[f"{a}{'s' if self.animals[a]>1 else ''}" for a in animal_list]
        if len(formatted)>1:
            animals_str=", ".join(formatted[:-1])+" and "+formatted[-1]
        else:
            animals_str=formatted[0]
        return f"{self.name}'s farm has {animals_str}."

macdonald=Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat',12)

print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())
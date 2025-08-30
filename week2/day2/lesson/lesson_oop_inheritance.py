class Animal: #Parent Class
    def __init__(self, name, family, legs):
        self.name=name
        self.family=family
        self.legs=legs
        pass
    def sleep(self):
        return f'{self.name} is sleeping (parent class)'


class Dog(Animal): #Child class
    def __init__(self, name, family, legs=4, age=0, trained=False):
        super().__init__(name, family, legs)
        self.age=age
        self.trained=trained
    def sleep(self):
        print(f'{self.name} is sleeping (child class)')
        return 
    def fetch_ball(self):
        print(f'{self.name} is running')
    pass
class Cat(Animal):
    def sleep(self):
        base_msg = super().sleep()
        print(f'{base_msg} on the roof')

class Alien:

    def __init__(self, planet, super_power):
        self.planet = planet
        self.super_power = super_power

    def fly(self):
        return f'{self.name} is flying'
    
    def sleep(self):
        return f'{self.name} is sleeping (alien class)'
   
    
#Multiple Inheritance
class AlienDog(Alien, Dog):
    def __init__(self, name, family, legs, age, trained, planet, super_power):
        Alien.__init__(self, planet, super_power)
        Dog.__init__(self, name, family, legs, age, trained)



dog1=Dog('Rex','Canie',5, 5,True,)
horse=Animal('Spirit','Equidae',4)
cat1=Cat('Lola','Felide',4)

print(dog1.__dict__)
print(dog1.legs)
dog1.sleep()
cat1.sleep()


secret_n=55
while True:
    try:
        number = int(input("number: "))
        if number>secret_n:
            print('Congrats')
            break
        else:
            print(f'{number} is not a sicret number')
            continue
    except Exception as e:
        print(e)
        print('Please enter a number')
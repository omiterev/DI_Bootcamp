from datetime import datetime,date
from faker import Faker

class Person:
    def __init__(self,first_name, last_name,birth_date):
        self.first_name=self.format_name(first_name)
        self.last_name=self.format_name(last_name)
        self.birth_date=self.parse_birthdate(birth_date)
        self._email=None
        pass

    @staticmethod
    def format_name(name):
        return name.title()
    
    @staticmethod
    def parse_birthdate(date_str):
        return datetime.strptime(date_str,'%d-%m-%Y').date()
    
    @classmethod
    def from_age(cls,first_name, last_name, age):
        current_year = datetime.today().year
        birth_year=current_year-age
        birth_date=f'01-01-{birth_year}'
        return cls(first_name, last_name, birth_date)
    
    @property
    def age(self):
        today=date.today()
        age=today.year-self.birth_date.year
        return age
    
    @property
    def email(self):
        _email=f'{self.first_name[0].lower()}.{self.last_name.lower()}@gmail.com'
        return _email
    
    #Dunder method
    
    def __str__(self):
        return f'Hello , this is {self.first_name}, {self.last_name}'
    
    def __repr__(self):
        return f'{self.__dict__}'
    def __eq__(self, other):
        return self.last_name==other.last_name
    def __lt__(self, other):#less then
        return self.age<other.age
    

p1=Person('john de','snow','21-08-1990')
p3=Person.from_age('Sisi','stark',21)
print(p1.birth_date)
print(p1.first_name)
print(p1.age)
print(datetime.today())
p2=Person.from_age('aris','stark',18)
print(p2.birth_date)
print(p1.email)

print(p1)
print(repr(p1))

print(p2==p3)

print(p1<p2)
fake=Faker()
first_name=fake.first_name()
last_name=fake.last_name()
birth_date=datetime.strftime(fake.date_of_birth(), '%d-%m-%Y')
print(first_name)
print(last_name)
print(birth_date)
#print(fake.date())
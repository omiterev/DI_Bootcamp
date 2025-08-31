#1
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount   

    def __str__(self):
        return f'{self.amount} {self.currency}'
    
    def __int__(self):
        return int(self.amount)
    def __repr__(self):
        return f'{self.__dict__}'
    def __add__(self, other):
        if isinstance(other, int):
            return self.amount+other
        else:
            if self.currency!=other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            else:
                return self.amount+other.amount
    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount+=other
            return self
        else:
            if self.currency!=other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            else:
                self.amount+=other.amount
                return self

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
print(c1)
# '5 dollars'

print(int(c1))
# 5

print(repr(c1))
# '5 dollars'

print(c1 + 5)
# 10

print(c1 + c2)
# 15

c1 += 5
print(c1)
# 10 dollars

c1 += c2
print(c1)
# # 20 dollars

print(c1 + c3)
# TypeError: Cannot add between Currency type <dollar> and <shekel>

#2
def addfunc(number1,number2):
    return print(number1+number2)

from func import addfunc
addfunc(3,8)

#3
import random
import string
random_string=''
letters=string.ascii_letters
#random_string = "".join(random.choice(letters) for _ in range(5))
for n in range(5):
    random_letter=random.choice(letters)
    random_string+=random_letter
print(random_string)

#4
import datetime
def current_date():
    today=datetime.date.today()
    print(today.strftime('%d/%m/%Y'))
current_date()

#5
def time_until_NY():
    today=datetime.datetime.today()
    str_new_year="01/01/2026"
    new_year=datetime.datetime.strptime(str_new_year,'%d/%m/%Y')
    time_left=new_year-today
    print(time_left)

time_until_NY()

#6
def minutes_lived():
    today=datetime.datetime.today()
    str_time_of_birth=input('Enter your date and time of birth in format(d/m/y h:m): ')
    time_of_birth=datetime.datetime.strptime(str_time_of_birth,'%d/%m/%Y %H:%M')
    time_lived=today-time_of_birth
    print(int(time_lived.total_seconds() // 60))
minutes_lived()

#7
from faker import Faker
fake = Faker()
list_of_users=[]
def fake_user(amount:int):
    for user in range(amount):
        new_dict={'name':fake.name(),
                  'address':fake.address(),
                  'language_code':fake.language_code()}
        list_of_users.append(new_dict)
    return list_of_users
fake_user(3)
print(list_of_users)
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
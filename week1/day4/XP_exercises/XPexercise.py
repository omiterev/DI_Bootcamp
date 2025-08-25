#1
def display_message():
    print('I am learning about functions in Python.')
display_message()
#2
def favorite_book(title:str="Alice in Wonderland"):
    print("One of my favorite books is", title)
favorite_book()
#3
def describe_city(sity:str='Unknown', country:str='Unknown'):
    print(f'{sity} is in {country}')
describe_city()
#4
import random
def random_numbers(num1:int=0):
    num2=random.randint(1,100)
    if num1==num2:
        print('Success!')
    else:
        print(f'Fail! Your number: {num1}, Random number: {num2}')
random_numbers()
#5
def make_shirt(size:str="Large", text:str="I love Python"):
    print(f'The size of the shirt is {size} and the text is {text}.')
make_shirt("small","Custom message")
make_shirt(size="medium")
#6
magician_names=['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(names):
    for name in names:
        print(name)

def make_great(names):
    for i, name in enumerate(names):
        names[i]=f'The Great {name}'
make_great(magician_names)
show_magicians(magician_names)
#7
get_random_temp=lambda: random.uniform(-10, 40)
def main():
    temp=get_random_temp()
    print(f'The temperature right now is {temp} degrees Celsius')
    if temp<0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif 0<=temp<16:
        print("Quite chilly! Don't forget your coat")
    elif 16<=temp<=23:
        print('Nice weather.')
    elif 24<=temp<32:
        print('A bit warm, stay hydrated')
    else:
        print('It’s really hot! Stay cool.')
main()
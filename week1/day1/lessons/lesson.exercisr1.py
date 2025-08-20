description ="strings are..."
description2 = description.upper()
print(description2)
description3=description.replace("are", "is")
print(description3)
description4 = description.strip(" are...")
print(description4)
print(description[0:7])
first_name = "Olga"
last_name = "Miterev"
print(f"My name is {first_name} {last_name}.")

name=input("Enter your name: ")
if len(name)<5:
    print('You have a short name :)')

number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")   
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print("Neither Fizz nor Buzz")
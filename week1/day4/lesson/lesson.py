# def say_hello(language:str):
#     '''prints a greeting depending on the language argument'''
#     if language == "English":
#         print("Hello!")
#     elif language == "Spanish":
#         print("¡Hola!")
#     elif language == "French":
#         print("Bonjour!")
#     else:
#         print("Language not supported.")

# def say_hello_adv(language:str = "EN", name:str = 'John'):
#     '''prints a greeting depending on the language argument'''
#     if language == "EN":
#         print(f"Hello, {name}")
#     elif language == "SP":
#         print(f"Hola, {name}")
#     elif language == "FR":
#         print(f"Bonjour, {name}")
#     else:
#         print("Language not supported.")
# # say_hello_adv("EN", "Bob")
# # say_hello_adv(name='Sarah',language='SP')

# def country_info(country:str='Naboo'):
#     '''This function return the capital of country'''
#     if country == 'France':
#         capital='Paris'
#     elif country =='US':
#         capital='Washington, D.C'
#     elif country =='India':
#         capital='Paris'
#     else:
#         print('I dont know this country')
#         capital='Unknown'
#     return capital, country
# cap, coun=country_info('Blala')
# print (cap, coun)

# #scope
# bar_mitzva=13

# def c_age():
#     # age =13
#     # if age == bar_mitzva:
#         # print('mazal tov')
#     global bar_mitzva
#     bar_mitzva+=1

#     # return age
# c_age()
# #print(bar_mitzva)
# age=c_age()
# print(age)

# #Data structures
students=['Harry','Hermoione','Ron','Luna']
# def welcome():
#     for name in students:
#         print(f'{name}, Welcome')
# welcome()

def get_house():
    #?????????
    for i, name in enumerate(students):
        students[i] = f'{name}-Grifindor'
    if name== 'Luna':
        students[i] = f'{name}-Ravenclaw'

get_house()
students[0]=f'{students[0]}-Grifindor'
print(students)

#*args=argument(str, list, tuple, set) and **kwargs=key word arguments(dict)

students=['Harry','Hermoione','Ron','Luna']
def welcome(*args):
    if args:
        for arg in args:
          print(f'{arg}, Welcome')
welcome('Harry','Hermoione')
welcome(students)

def format_info(**kwargs):
    if kwargs:
        print(kwargs)
    if kwargs['parseltonge']:
        print(f'{kwargs["name"]} can talk to snakes')

format_info(name = 'Harry', email="harry@gmail.com", age=14, parseltonge=True)

#1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
#general_dict = {keys[i]: values[i] for i in range(len(keys))}
general_dict = dict(zip(keys, values))
print(general_dict)

#2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
ticket_cost = 0
while True:
    family_inp_name=input("Enter the family member's name or quit: ")
    if family_inp_name == "quit":
        break
    family_inp_age=int(input("Enter the family member's age: "))
    family[family_inp_name] = family_inp_age
for name, age in family.items():
    if age < 3:
        print(f"{name} the ticket is free.")
    elif 3<=age<=12:
        ticket_cost += 10
        print(f"For {name} the ticket is {ticket_cost} $.")
    elif age > 12:
        ticket_cost += 15
        print(f"For {name} the ticket is {ticket_cost} $.")
#3
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}
brand['number_stores']=2
print(f'In Zara you can find different types of things for: {brand["type_of_clothes"][0]}, {brand["type_of_clothes"][1]}, {brand["type_of_clothes"][2]}, {brand["type_of_clothes"][3]}')
brand['country_creation']="Spain"
if 'international_competitors' in brand:
    brand["international_competitors"].append("Desigual")
del brand["creation_date"]
print(brand['international_competitors'][-1])
print(brand['major_color']['US'])
print(len(brand))
print(brand.keys())
more_on_zara={
    'creation_date':1945,
    'number_stores': 450
}
brand.update(more_on_zara)
print(brand)
#4
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
dict1={num: user for user, num in enumerate(users)}
print(dict1)
dict2={num: user for num, user in enumerate(users)}
print(dict2)
users.sort()
dict3={num: user for num, user in enumerate(users)}
print(dict3)
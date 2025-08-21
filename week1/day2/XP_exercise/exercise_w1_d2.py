#1
my_fav_numbers={11,9,7,8,11,3,19}
my_fav_numbers.add(34)
my_fav_numbers.add(88)
my_fav_numbers.remove(88)
print(my_fav_numbers)
friend_fav_numbers={3,9,12,64,7,22}
our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers) 
#2
x=(2,4,6,9,0)
#x.append(3)  # This will raise an AttributeError since tuples are immutable 
#3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove('Banana')
basket.remove("Blueberries")
basket.append("Kiwi")
basket.append("Apples")
print(basket.count("Apples"))
basket.clear()
print(basket)
#4
i=1
list_f=[]
while i<=5:
    list_f.append(i)    
    i+=0.5
print(list_f)
#5
for i in range(1,21):
    print(i)
numbers = []
for i in range(1,21):
    numbers.append(i)
    if numbers.index(i) % 2 == 0:
        print(i)
#6
u_name=input("Enter your name: ")
while u_name != "Olga":
    u_name=input("Please enter your name: ")
#7
u_fav_fruit_string=input("Enter your favorite fruits separated by space: ")
u_fav_fruit_l=u_fav_fruit_string.split(" ")
u_frute=input("Enter any fruit: ")
if u_frute in u_fav_fruit_l:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")
#8
topping_count = 0
topping_list = []
while True:
    u_topping=input("Enter pizza topping or enter 'quit' to finish: ")
    if u_topping == "quit":
       break
    print(f"Adding {u_topping} to your pizza.")
    topping_list.append(u_topping)
    topping_count += 1
topping_string = ", ".join(topping_list)
print(f"You added {topping_string} to your pizza: ")
print("The pizza will cost ",(10 + (topping_count * 2.5)), "$")
#9
ask_user=input("Do you want to see a restricted movie? (yes/no)")
ticket_price = 0
if ask_user.lower() == "yes":
    age=input("Enter your age separated by commas: ")
    age_list = [int(a.strip()) for a in age.split(",")]
    restricted_list=range(16, 22)
    allowed_list=[i for i in age_list if i in restricted_list]
    print(f"Allowed ages: {allowed_list}")
    for b in allowed_list:
        if b < 3:
         ticket_price+=0
        elif b >= 3 and b <= 12:
            ticket_price+=10
        else:
            ticket_price+=15
    print(f"The total ticket cost is: {ticket_price}")
elif ask_user.lower() == "no":
    age=input("Enter your age separated by commas: ")
    #age_list = age.split(",")
    age_list = [int(a.strip()) for a in age.split(",")]
    restricted_list=range(16, 22)
    allowed_list=[i for i in age_list if i in restricted_list]
    print(f"Allowed ages: {allowed_list}")
    for b in age_list:
        if b < 3:
         ticket_price+=0
        elif b >= 3 and b <= 12:
            ticket_price+=10
        else:
            ticket_price+=15
    print(f"The total ticket cost is: {ticket_price}")
 #10
sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]
finished_sandwiches=[]
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
for s in sandwich_orders:
    finished_sandwiches.append(s)
    print(f"I made your {s} sandwich.")
print(finished_sandwiches)
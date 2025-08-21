import random
u_string=input("Enter a string: ")
if len(u_string) < 10:
    print("String not long enough.")
elif len(u_string) > 10:
    print("String too long.")
else:
    print("Perfect string")
    print(u_string[0], u_string[-1])
    new_string =""
for l in u_string:
    new_string += l
    print(new_string)

list_string = list(u_string)
random.shuffle(list_string)
shuffle_string = "".join(list_string)
print(shuffle_string)

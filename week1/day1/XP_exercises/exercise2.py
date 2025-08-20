print("Hello world\n"*4 +"I love python\n"*4)
season = int(input("Enter a number on the month "))
if season in (3,4,5):
    print("Spring")
elif season in (6,7,8):
    print("Summer")
elif season in (9,10,11):
    print("Autumn")
elif season in (12,1,2):
    print("Winter")
else:
    print("Wrong number")

print(3 <= 3 < 9)
print(3 == 3 == 3)
print(bool(0))
print(bool(5 == "5"))
print(bool(4 == 4) == bool("4" == "4"))
print(bool(bool(None)))

my_text = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
    "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco "
    "laboris nisi ut aliquip ex ea commodo consequat. "
    "Duis aute irure dolor in reprehenderit in voluptate velit "
    "esse cillum dolore eu fugiat nulla pariatur. "
    "Excepteur sint occaecat cupidatat non proident, "
    "sunt in culpa qui officia deserunt mollit anim id est laborum.")
print(len(my_text))

sentence = input("Enter a sentence without 'a' in it: ")
if sentence.find("a") == -1:
    print("Good job!")
else:
    print("Try again!")

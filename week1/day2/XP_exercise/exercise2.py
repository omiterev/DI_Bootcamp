#1
list1=[1,2,3]
list2=[4,5,6,7]
for i in list2:
    list1.append(i)
print(list1)
#2
list4=range(1500,2501)
for i in list4:
    if i % 5 == 0 and i % 7 == 0:
        print(i)
#3
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
u_name=input("Enter your name: ")
if u_name in names:
    print(names.index(u_name))
#4
number_count=1
u_number_list=[]
while number_count<4:
    u_number=input(f"Input the {number_count} number: ")
    u_number_list.append(u_number)
    number_count+=1
u_number_list.sort()
print("The greatest number is: " + u_number_list[-1])
#5
alfabet_list=""
for i in range(97,123):
    alfabet_list+=chr(i)
print(alfabet_list)
for l in alfabet_list:
    if l in "aeiou":
        print(f"{l} is a vowel")
    else:
        print(f"{l} is a consonant")
#6
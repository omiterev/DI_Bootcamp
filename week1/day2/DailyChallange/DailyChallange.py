#1
number=int(input("Enter a number: "))
length=int(input("Enter the length: ")) 
multiples=[]
for i in range(1, length + 1):
    multiples.append(number*i)
print(multiples)
#2
u_string=input("Enter a string: ")
string_list=[]
string_list.append(u_string[0])
for u in range(1,len(u_string)):
    if u_string[u]!= u_string[u-1]:
        string_list.append(u_string[u])
n_string="".join(string_list)
print(n_string)

list1 = [5, 10, 15, 20, 25, 50, 20]
if list1.index(20) != -1:
    list1[list1.index(20)] = 200    
print(list1)

fav_colors={'green', 'blue', 'orange'}
fav_colors.add('white')
friend_fav_colors = {'red', 'purple','blue', 'white'}
common_colors=fav_colors.intersection(friend_fav_colors)
print(common_colors)
fav_colors.clear()
print(fav_colors)

for i in range(1,21):
    print(i)
numbers = []
for i in range(1,21):
    numbers.append(i)
    if numbers.index(i) % 2 == 0:
        print(i)


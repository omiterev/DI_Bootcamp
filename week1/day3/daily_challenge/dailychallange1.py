#1
word=input('enter a word: ')
dict1={}
for num, l in enumerate(word):
    if l not in dict1:
        dict1[l]=[num]
    else:
        dict1[l].append(num)
print(dict1)

#2
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"
int_purchase={}
affordable_items=[]
for i, p in items_purchase.items():
    price=int(p.replace("$","").replace(",",""))
    int_purchase[i]=price
int_wallet=int(wallet.replace("$","").replace(",",""))
for item, price in int_purchase.items():
    if price<=int_wallet:
        affordable_items.append(item)
affordable_items.sort()
if affordable_items==None:
    print("Nothing")
print(affordable_items)
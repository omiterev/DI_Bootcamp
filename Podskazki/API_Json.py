# pip install requests

import requests
import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))#ishet directory
file_path = os.path.join(dir_path, "jokes.json")
jokes=[]
for _ in range(10):
    respons=requests.get('https://api.chucknorris.io/jokes/random')
    #print(respons)#Response [200]
    data=respons.json()#Convert to dict
    #print(data['value'])#beret no ne proveryaet esli key sushestvuet
    #print(data.get('joke'))#no crashs the code
    #print(data.get('value'))
    jokes.append(data.get('value'))

# with open(file_path,'w',encoding='utf-8') as f:
#     json.dump(data,f, indent=2, sort_keys=True) sozdaet file json
with open(file_path,'w',encoding='utf-8') as f:
     json.dump(jokes,f, indent=2, sort_keys=True)



dir_path = os.path.dirname(os.path.realpath(__file__))
#convert json fime
my_family = {
    'parents':['Beth', 'Jerry'],
    'children': ['Summer', 'Morty']
}
with open(f'{dir_path}/family.json','w',encoding = 'utf-8' ) as f:
    json.dump(my_family, f)

#convert json string
json_family=json.dumps(my_family)
print(type(json_family))


#load() Loads()

with open(f'{dir_path}/family.json','r',encoding = 'utf-8' ) as f:
    my_family2=json.load(f)
print(type(my_family2))

#from a json string o a dict
parsed_family=json.loads(json_family)
print(type(parsed_family))
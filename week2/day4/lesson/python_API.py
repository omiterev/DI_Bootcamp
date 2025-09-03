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
    data=respons.json()
    #print(data['value'])#beret no ne proveryaet esli key sushestvuet
    #print(data.get('joke'))#no crashs the code
    #print(data.get('value'))
    jokes.append(data.get('value'))

# with open(file_path,'w',encoding='utf-8') as f:
#     json.dump(data,f, indent=2, sort_keys=True) sozdaet fajl
with open(file_path,'w',encoding='utf-8') as f:
     json.dump(jokes,f, indent=2, sort_keys=True)
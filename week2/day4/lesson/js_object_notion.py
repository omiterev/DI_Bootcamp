import json
import os
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
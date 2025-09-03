import json
import os
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
data=json.loads(sampleJson)
print(data["company"]["employee"]["payable"]["salary"])
data["company"]["employee"]["birth_date"]='YYYY-MM-DD'
print(data)
data["company"]["employee"]["birth_date"]='1999-10-24'
print(data)
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(f'{dir_path}/sample.json','w',encoding='utf-8')as f:
    json.dump(data, f, indent=2) 
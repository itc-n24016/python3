import json
name = {'tanaka':{'age': 20, 'bloodtype': 'A', 'gender': 'male'},
        'satou': {'age': 19, 'bloodtype': 'O', 'gender': 'female'},
        'suzuki':{'age': 20, 'bloodtype': 'AB', 'gender': 'male'}}
with open('name.json', 'w') as f1:
    json.dump(name, f1)

with open('name.json', 'r') as f2:
    name_a = json.load(f2)

for key, val in name_a.items():
    print(key, val)


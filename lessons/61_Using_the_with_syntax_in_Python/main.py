import json

with open('data.json', 'r') as file:
	file_content = json.load(file)

cars = [
	{'make': 'Ford', 'model': 'Fiesta'},
	{'make': 'Ford', 'model': 'Focus'}
]

with open('data.json', 'w') as file:
	json.dump(cars, file)

print('2.', file_content)

my_json_string = '[{"model": "Alfa Romero", "release": 1950}]'

incorrect_car = json.loads(my_json_string)

print('3.', incorrect_car[0]['model'])

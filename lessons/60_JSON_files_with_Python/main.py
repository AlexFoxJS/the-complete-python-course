import json

file = open('data.json', 'r')
file_content = json.load(file)
file.close()

cars = [
	{'make': 'Ford', 'model': 'Fiesta'},
	{'make': 'Ford', 'model': 'Focus'}
]

file = open('data.json', 'w')
json.dump(cars, file)
file.close()

print('1.', file_content)

my_json_string = '[{"model": "Alfa Romero", "release": 1950}]'

incorrect_car = json.loads(my_json_string)

print('2.', incorrect_car[0]['model'])

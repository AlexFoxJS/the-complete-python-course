class Student:
	def __init__(self, name):
		self.name = name


movie = ['The Matrix', 'Oblivion']
print('1.', movie.__class__)
print('2.', len(movie))


class Garage:
	def __init__(self):
		self.cars = []

	def __len__(self):
		return len(self.cars)

	def __getitem__(self, i):
		return self.cars[i]

	def __repr__(self):
		return f'Garage with {len(self)} cars.'


ford = Garage()
print('3.', ford.cars)
ford.cars.append('Test_1')
ford.cars.append('Test_2')
ford.cars.append('Test_3')
print('4.', ford.cars)
print('5.', len(ford))
print('6.', ford[1]) # Garage._getitem__(ford, 0)

for i in range(len(ford)):
	print(f"7_{i}. {ford.cars[i]}")

print('8.', ford)

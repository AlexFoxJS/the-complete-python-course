file = open('csv_data.txt.txt', 'r')
lines = file.readlines()
file.close()

print(f'1.{lines}')
lines = [line.strip() for line in lines[1:]]
print(f'2.{lines}\n')

for i in range(len(lines)):
	person_data = lines[i].split(',')
	name = person_data[0].title()
	age = person_data[1]
	university = person_data[2].title()
	degrees = person_data[3].capitalize()

	print(f'{i+1}) {name} is {age} years old, studying {degrees} at {university}.')

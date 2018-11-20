# Ask the user for list of 3 frends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to 'people.txt'

friends = input('Enter three friends names, separate by commas (no space please): ').split(',')
file = open('people.txt', 'r')
people_nearby = [line.strip() for line in file.readlines()]
file.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)

nearby_friends_file = open('nearby_friends_file.txt', 'w')

for friend in friends_nearby_set:
	print(f'{friend} is nearby! Meet up with them.')
	nearby_friends_file.write(f'{friend} ')

nearby_friends_file.close()

"""
- Enter 'a' to add a movie, '1' to see your movies, 'f' to find a movie, and 'q' to quit:

- Add movies
- See movies
- Find a movie
- Stop running program

Tasks:
[]: Decide where to store movies
[]: What is the format movies
[x]: Show the user the main interface and get their input
[]: Allow users to add movies
[]: Show all their movies
[]: Find movie
[x]: Stop running the program when they type 'q'
"""


movies = []

"""
movie = {
	'name': ...(str),
	'direction': ...(str),
	'year': ...(int),
}
"""


def menu():
	user_input = input("Enter 'a' to add a movie, '1' to see your movies, 'f' to find a movie, and 'q' to quit:")

	while user_input != 'q':
		if user_input == 'a':
			add_movie()
		elif user_input == 'l':
			show_movie()
		elif user_input == 'f':
			find_movie()
		else:
			print('Unknown command, try again.')

		user_input = input("Enter 'a' to add a movie, '1' to see your movies, 'f' to find a movie, and 'q' to quit:")


def add_movie():
	name = input('Enter the movie name:')
	direction = input('Enter the movie direction:')
	year = int(input('Enter the movie year:'))

	movies.append({
		'name': name,
		'direction': direction,
		'year': year
	})


# def show_movie():
#
#
#
# def find_movie():


menu()

print(movies)

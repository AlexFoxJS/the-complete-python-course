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
	user_input_desc_text = "Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: "
	user_input = input(user_input_desc_text)

	while user_input != 'q':
		if user_input == 'a':
			add_movie()
		elif user_input == 'l':
			show_movie(movies)
		elif user_input == 'f':
			find_movie()
		else:
			print('Unknown command, try again.')

		user_input = input(f"\n{user_input_desc_text}")


def add_movie():
	name = input('Enter the movie name:')
	direction = input('Enter the movie direction:')
	year = input('Enter the movie year:')

	movies.append({
		'name': name,
		'direction': direction,
		'year': year
	})


def show_movie(movies_list):
	for movie in movies_list:
		show_movie_details(movie)


def show_movie_details(movie):
	print(f"\nName: {movie['name']}")
	print(f"Director: {movie['direction']}")
	print(f"Release year: {movie['year']}")


def find_movie():
	find_by = input('What property of the movie are you looking for? ')
	looking_for = input('What are you searching for? ')

	found_movies = find_by_attributes(movies, looking_for, lambda x: x[find_by])

	show_movie(found_movies)


def find_by_attributes(items, expected, finder):
	found = []

	for i in items:
		if finder(i) == expected:
			found.append(i)

	return found


menu()

print(movies)

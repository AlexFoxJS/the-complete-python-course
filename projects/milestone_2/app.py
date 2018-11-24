from projects.milestone_2.utils import database

USER_CHOICE = """
Enter:
- "a" add new book
- "l" list of books
- "r" mark book to read
- "d" delete book
- "q" quit


Your choice: """


def menu():
	user_input = input(USER_CHOICE)

	while user_input != 'q':
		if user_input == 'a':
			prompt_add_book()
		elif user_input == 'l':
			list_books()
		elif user_input == 'r':
			prompt_read_book()
		elif user_input == 'd':
			prompt_delete_book()
		else:
			print('Unknown command. Please try again.')

		user_input = input(USER_CHOICE)


def prompt_add_book():
	name = input('Enter book name: ')
	author = input('Enter book author: ')

	database.add_book(name, author)


def list_books():
	books = database.show_books()

	print('\nBooks list:')
	for i in range(int(len(books))):
		read = 'Yes' if books[i]["read"] else 'No'
		print(f'{i+1}. {books[i]["name"]} by {books[i]["author"]}, read: {read}')


def prompt_read_book():
	name = input('Enter name of the book you just finished reading: ')

	database.read_book(name)


def prompt_delete_book():
	name = input('Enter name of the book you want to delete: ')

	database.delete_book(name)


menu()

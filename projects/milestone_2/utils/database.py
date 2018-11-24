import sqlite3

books_file = 'books.json'


def create_book_table():
	connection = sqlite3.connect('data.db')
	cursor = connection.cursor()

	cursor.execute('CREATE TABLE books(name text primary key, author text, read integer)')

	connection.commit()
	connection.close()


def add_book(name, author):
	books = get_all_books()
	books.append({'name': name, 'author': author, 'read': False})
	_save_all_books(books)


def get_all_books():
	with open(books_file, 'r') as file:
		return json.load(file)


def _save_all_books(books):
	with open(books_file, 'w') as file:
		json.dump(books, file)


def mark_book_as_read(name):
	books = get_all_books()

	for book in books:
		if book["name"] == name:
			book["read"] = True

	_save_all_books(books)


def delete_book(name):
	books = get_all_books()
	books = [book for book in books if book["name"] != name]
	_save_all_books(books)

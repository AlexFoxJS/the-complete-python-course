from .utils import database

USER_CHOICE = """
Enter:
- "a" add new book
- "l" list of books
- "r" mark book to read
- "d" delete book
- "q" quit


Your choice:"""


def menu():
	user_input: input(USER_CHOICE)

	while user_input != 'q':
		pass

# def prompt_add_book() - ask book name and author
# def list_books() - show books list
# def prompt_read_book() - ask book name and change it to "read" in our list
# def prompt_delete_book() - ask book name and remove book from list

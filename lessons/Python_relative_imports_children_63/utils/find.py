from .common.file_operations import save_to_file


def find_in(iterable, finder, expected):
	for i in iterable:
		if finder(i) == expected:
			return i

	raise NotFoundError(f'{expected} not found in provided iterable.')


def NotFoundError(Exeption):
	pass


print('1. ', __name__)


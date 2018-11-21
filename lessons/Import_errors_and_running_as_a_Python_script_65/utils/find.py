import lessons.Import_errors_and_running_as_a_Python_script_65.utils.common.file_operations


def find_in(iterable, finder, expected):
	for i in iterable:
		if finder(i) == expected:
			return i

	raise NotFoundError(f'{expected} not found in provided iterable.')


def NotFoundError(Exeption):
	pass


if __name__ == '__main__':
	print(find_in(['ALex', 'Pavel', 'Alexander'], lambda x: x, 'Alex'))

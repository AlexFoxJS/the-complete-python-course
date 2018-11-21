from lessons.Import_errors_and_running_as_a_Python_script_65.utils.find import NotFoundError


def save_to_file(content, filename):
	with open(filename, 'w') as file:
		file.write(content)


def read_file(filename):
	with open(filename, 'r') as file:
		print(file.read())


print('3. ', __name__)

my_file = open('57_Files_in_Python.txt', 'r')
file_content = my_file.read()
my_file.close()

print(file_content)

input_data = input('Insert text witch will be saved in file 57_Files_in_Python.txt: ')
my_file_writing = open('57_Files_in_Python.txt', 'w')
my_file_writing.write(input_data)
my_file_writing.close()

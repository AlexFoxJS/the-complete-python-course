from utils.file_operations import save_to_file, read_file

user_input_data = input('Please insert some text: ')
user_select_file = input('Please insert name one of next files: file_1.txt, file_3.txt, file_3.txt to write them: ')

save_to_file(user_input_data, user_select_file)
read_file(user_select_file)

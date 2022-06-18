import os

def files_glue(file_name, format='.txt'):
    with open((file_name + format), 'a') as file_writable:
        files_dict = {}
        for file_open in os.listdir('sorted'):
            with open(os.path.join('sorted', file_open), 'r') as file_opened:
                string_count = len(file_opened.readlines())
                files_dict[file_open] = string_count
        files_dict_sorted = dict(sorted(files_dict.items(), key=lambda item: item[1]))
        for file_name_in_dict_sorted, string_count_in_dict_sorted in files_dict_sorted.items():
            with open(os.path.join('sorted', file_name_in_dict_sorted)) as file_readable:
                file_writable.write(f'{file_name_in_dict_sorted}\n')
                file_writable.write(f'{str(string_count_in_dict_sorted)}\n')
                file_content = file_readable.read()
                file_writable.write(f'{file_content}\n')
    print('Программа выполнена')

files_glue(input('Введите имя файла: '))
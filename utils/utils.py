import csv
import os
from constants.constants import number_of_string_for_read, default_text


def select_mode():
    mode = input('Выберите метод: read, write')

    if mode != 'read' and mode != 'write':
        print('Нераспознаный метод')
        return select_mode()

    return mode


def get_file_path():
    file_path = input('Путь к файлу: ')
    return check_file(file_path)


def check_file(file_path):
    file_status = os.path.exists(file_path)
    file_extension = os.path.splitext(file_path)[1]

    if not file_status:
        print('Такого файла или пути не существует')
        return get_file_path()

    elif file_extension != '.csv' and file_extension != '.txt':
        print('Неверное расширение файла. Валидные расширения .csv и .txt')
        return get_file_path()

    else:
        return file_path


def read_file(file_path):
    with open(file_path, newline='') as File:
        content_of_file = csv.reader(File)
        counter = 0

        for row in content_of_file:
            print(row)
            counter += 1

            if counter == number_of_string_for_read:
                break


def write_to_file(file_path):
    with open(file_path, 'a', newline='') as File:
        content_of_file = csv.writer(File)

        for row in default_text.split('\n'):
            content_of_file.writerow([row])
